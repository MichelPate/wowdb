from .abstract import AbstractModel
from .misc import ManifestInterfaceData

class GarrTalent (AbstractModel):
    TABLE = {"table":"GarrTalent", "id_field":"id", "id_parent_field":"id_parent"}
    def __init__ (self, id, **kwargs):
        super (GarrTalent, self).__init__(id, **kwargs)
    
    def getIcon (self, size=35, **kwargs):
        if self.iconFileDataID != 0 :
            uiData = ManifestInterfaceData(self.iconFileDataID)
            return uiData.getIcon(size, **kwargs)

class GarrTalentRank (AbstractModel):
    TABLE = {"table":"GarrTalentRank", "id_field":"id", "id_parent_field":"id_parent"}
    def __init__ (self, id, **kwargs):
        super (GarrTalentRank, self).__init__(id, **kwargs)

class GarrTalentTree (AbstractModel):
    TABLE = {"table":"GarrTalentTree", "id_field":"id"}
    def __init__ (self, id, **kwargs):
        super (GarrTalentTree, self).__init__(id, **kwargs)