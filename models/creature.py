from .abstract import AbstractModel

class CreatureType (AbstractModel):
    TABLE = {"table":"CreatureType", "id_field":"id"}
    def __init__ (self, id, **kwargs):
        super (CreatureType, self).__init__(id, **kwargs)

class CreatureCache (AbstractModel):
    TABLE = {"table":"creaturecache", "id_field":"ID"}
    def __init__ (self, id, **kwargs):
        super (CreatureCache, self).__init__(id, **kwargs)