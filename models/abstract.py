from ..manager import DB, STATICDB
from ..utilities import toCamelCase
from collections import defaultdict
import re

def parseArray (d, default={}):
    if d :
        attrs = {}
        duplicate = d.copy()
        for k,v in d.items():
            key = k
            idx_str = next(iter(re.findall(r'\_\d{1,2}$', k[-3:])), False)
            if idx_str :
                key = key.replace(idx_str, '')
                idx = int(idx_str.replace('_', ''))
                if key in attrs :
                    attrs[key][idx]=v
                else :
                    attrs[key] = {idx:v}
                del duplicate[k]
        duplicate.update(attrs)
        return duplicate
    return default

class MetaModelIndexing (type):
    '''Metaclass for cataloguing and indexing each instance'''

    def __init__(cls, name, bases, attrs, **kwargs):
        super().__init__(name, bases, attrs, **kwargs)
        cls._cache = {}
        cls._REFERENCES = {}
        if cls.TABLE.get("id_parent_field", False):
            cls._REFRENCES_PARENT = defaultdict(list)

    def __call__(cls, *args, **kwargs):
        idx = cls._getIndexFromArgs (*args)
        parentField = cls.TABLE.get("id_parent_field", False)

        if idx in cls._REFERENCES :
            # return cls._REFERENCES[idx]
            s = super()
            instance = s.__call__(cls._REFERENCES[idx]._cache, **kwargs)
            return instance
        else :
            s = super()
            instance = s.__call__(*args, **kwargs)
            # print (args, kwargs, instance._cache)
            cls._REFERENCES[idx] = instance
            if parentField: 
                cls._REFRENCES_PARENT[instance._cache[parentField]].append(instance)
            return instance

    def _getIndexFromArgs (cls, *args):
        field = cls.TABLE.get("id_field", "id")
        if args and isinstance(args[0], int) :
            idx = args[0]
        elif args and isinstance(args[0], dict) :
            idx = args[0].get(field, None)
        else :
            raise AttributeError ("{} only accepts dict or int".format(cls.__name__))
        return idx

    def FindReference (cls, query):
        return [subCls for subCls in cls._REFERENCES.values() if subCls.match(query)]

    def Find (cls, query, **kwargs):
        table = cls.TABLE.get("table")
        parentField = cls.TABLE.get("id_parent_field", False)

        result = cls.DATABASE[table].find(query)
        instances = [cls.__call__(x, **kwargs) for x in result]

        if parentField :
            for item in instances :
                cls._REFRENCES_PARENT[item._cache[parentField]].append(item)
        return instances

    def Many (cls, indices, **kwargs):
        table = cls.TABLE.get("table")
        field = kwargs.pop("field", cls.TABLE.get("id_field"))
        parentField = cls.TABLE.get("id_parent_field", False)
        sortedIndices = sorted(indices)
        query = cls.DATABASE[table].find({field:{"$in":sortedIndices}})
        mapping = {q[field]: q for q in query}
        query=[mapping[i] for i in indices if i in mapping]

        instances = [cls.__call__(x, **kwargs) for x in query]
        if parentField :
            for item in instances :
                cls._REFRENCES_PARENT[item._cache[parentField]].append(item)
        return instances
    
    def All (cls,**kwargs):
        table = cls.TABLE.get("table")
        query = cls.DATABASE[table].find()
        return [cls.__call__(x, **kwargs) for x in query]
    

    def FromParent (cls, *args, **kwargs):
        table = cls.TABLE.get("table", None)
        parentField = cls.TABLE.get("id_parent_field", False)
        sort_field = kwargs.pop("sort_field", False)
        idx = cls._getIndexFromArgs (*args)
        
        instances = []
        if idx in cls._REFRENCES_PARENT:
            instances = cls._REFRENCES_PARENT[idx]
        elif parentField:
            s = super()
            query = cls.DATABASE[table].find({parentField: idx})
            instances = [s.__call__(x, **kwargs) for x in query]
            cls._REFRENCES_PARENT[idx] += instances
        
        if sort_field:
            instances.sort(key=lambda x: getattr(x, sort_field))
        return instances
    
    def __getitem__(cls, idx):
        return cls._REFERENCES.get(idx, None)

class AbstractModel (object, metaclass=MetaModelIndexing):
    '''Database Model'''
    EXCLUDE_FIELDS = ["_id"]
    BLACKLIST_WORDS = ["_lang"]
    TABLE = {}
    DATABASE = DB
    def __init__ (self, data, *args, **kwargs):
        super (AbstractModel, self).__init__()
        # print (self.__class__.__name__, data, args, kwargs)
        self.parent = kwargs.pop("parent", None)

        if isinstance(data, int): 
            table = self.TABLE.get("table", False)
            field = self.TABLE.get("id_field", False)
            if table and field:
                self._cache = self.DATABASE[table].find_one({field: data})
        elif isinstance(data, dict):
            self._cache = data
        properties = {}
        for k, v in parseArray(self._cache).items():
            if k not in self.EXCLUDE_FIELDS :
                key = k
                for word in self.BLACKLIST_WORDS:
                    key = key.replace(word, "")
                properties[toCamelCase(key)] = v
        self.__dict__.update(properties)
    
    def exists (self):
        if self._cache :
            return True
        return False
    
    def match(self, d):
        return all(True if hasattr(self, k) and getattr(self, k)==v else False for k,v in d.items())
            
class GameModel (AbstractModel):
    DATABASE = STATICDB
    def __init__ (self, data, *args, **kwargs):
        super (GameModel, self).__init__(data, *args, **kwargs)