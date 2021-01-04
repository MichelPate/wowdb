from .abstract import AbstractModel
from .skill import SkillLine

class Covenant (AbstractModel):
    TABLE = {"table":"Covenant", "id_field":"id"}
    def __init__ (self, id, **kwargs):
        super (Covenant, self).__init__(id, **kwargs)
    
    def getSkillLine (self):
        return SkillLine(self.skillLineID)

class UICovenantAbility (AbstractModel):
    TABLE = {"table":"UICovenantAbility", "id_field":"id"}
    def __init__ (self, id, **kwargs):
        super (UICovenantAbility, self).__init__(id, **kwargs)
