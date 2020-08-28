from .abstract import AbstractModel
from .misc import ManifestInterfaceData
from ..utilities import rgbHex
# from .spell import SpecializationSpells

class ChrClasses (AbstractModel):
    TABLE = {"table":"ChrClasses", "id_field":"id"}
    COLORS = {1: (199, 156, 110), 2: (245, 140, 186), 3: (171, 212, 115), 4: (255, 245, 105), 5: (255, 255, 255), 6: (196, 30, 59), 7: (0, 112, 222), 8: (105, 204, 240), 9: (148, 130, 201), 10: (0, 255, 150), 11: (255, 125, 10), 12: (163, 48, 201)}
    def __init__ (self, id, **kwargs):
        super (ChrClasses, self).__init__(id, **kwargs)
    
    def getColor (self):
        return self.COLORS.get(self.id, None)
    
    def getIcon (self, size=35,**kwargs):
        uiData = ManifestInterfaceData(self.iconFileDataID)
        return uiData.getIcon(size, **kwargs)
        
    def getShortText (self, iconSize = 15):
        return '<span style="text-align: right;">{icon}</span> <span style="color:{color};">{name}</span>'.format(icon=self.getIcon(size=iconSize, html=True), name=self.name, color=rgbHex(self.getColor()))

class ChrSpecialization (AbstractModel):
    TABLE = {"table":"ChrSpecialization", "id_field":"id", "id_parent_field":"id_parent"}
    def __init__ (self, id, **kwargs):
        super (ChrSpecialization, self).__init__(id, **kwargs)
    
    def getClass (self):
        if self.classID !=0 :
            chrClass = ChrClasses(self.classID)
            if chrClass.exists():
                return chrClass
    
    # def getSpecializationSpells (self):
    #     return SpecializationSpells.FromParent(self.id, parent=self)

class SpecSetMember (AbstractModel):
    TABLE = {"table":"SpecSetMember", "id_field":"id", "id_parent_field":"id_parent"}
    def __init__ (self, id, **kwargs):
        super (SpecSetMember, self).__init__(id, **kwargs)
    
    def getSpec (self):
        return ChrSpecialization[self.chrSpecializationID]

preload = (
    ChrClasses,
    ChrSpecialization,
    SpecSetMember,
) 
for tbl in preload:
    tbl.All() 
