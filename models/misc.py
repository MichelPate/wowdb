from .abstract import AbstractModel
from ..utilities import iconBase64Html

class ManifestInterfaceData (AbstractModel):
    TABLE = {"table":"ManifestInterfaceData", "id_field":"id"}
    def __init__ (self, id, **kwargs):
        super (ManifestInterfaceData, self).__init__(id, **kwargs)

    def getIcon (self, size=False, html=False, **kwargs):
        filename = ""
        if self.exists():
            filename = self.fileName.replace(".blp", "")
        return iconBase64Html(filename, size=size, html=html, **kwargs)
    
    def getFullpath (self):
        return "{}{}".format(self.filePath, self.fileName)

class Map (AbstractModel):
    TABLE = {"table":"Map", "id_field":"id"}
    def __init__ (self, id, **kwargs):
        super (Map, self).__init__(id, **kwargs)

class Difficulty (AbstractModel):
    TABLE = {"table":"Difficulty", "id_field":"id"}
    def __init__ (self, id, **kwargs):
        super (Difficulty, self).__init__(id, **kwargs)

class PowerType (AbstractModel):
    TABLE = {"table":"PowerType", "id_field":"PowerTypeEnum"}
    def __init__ (self, id, **kwargs):
        super (PowerType, self).__init__(id, **kwargs)

class RandPropPoints (AbstractModel):
    TABLE = {"table":"RandPropPoints", "id_field":"id"}
    def __init__ (self, id, **kwargs):
        super (RandPropPoints, self).__init__(id, **kwargs)

def closest(lst, K): 
        return lst[min(range(len(lst)), key = lambda i: abs(lst[i]-K))] 

class CurvePoint (AbstractModel):
    TABLE = {"table":"CurvePoint", "id_field":"id"}
    def __init__ (self, id, **kwargs):
        super (CurvePoint, self).__init__(id, **kwargs)
    
    @classmethod
    def getCurve (cls, idx):
        curveUnsorted = cls.Find({"CurveID":idx})
        sortedCurve = sorted(curveUnsorted, key=lambda x: x.orderIndex)
        return sortedCurve
    
    @classmethod
    def getInterpolation (cls, value, curveID=0):
        curve = cls.getCurve(curveID)
        d = {}
        for p in curve :
            d[int(p.pos[1])]=int(p.pos[2])
        
        if value in d.keys():
            return d[value]
        else:
            l = list(d.keys())
            clo = closest(l, value)
            idx = l.index(clo)
            if clo > value:
                mi, ma = l[idx-1], clo
            else :
                mi, ma = clo, l[idx+1]
            deltaIlvl =  d[ma] - d[mi]
            deltaLvl =  ma - mi
            mult = deltaIlvl/deltaLvl
            deltaDrop = value-mi
            v = deltaDrop*mult
            return d[mi]+v

preload = (
    RandPropPoints,
) 
for tbl in preload:
    tbl.All() 