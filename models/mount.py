from .abstract import AbstractModel
from .spell import Spell
from ..parsers import LuaParser

class Mount (AbstractModel):
    TABLE = {"table":"Mount", "id_field":"id"}
    def __init__ (self, id, **kwargs):
        super (Mount, self).__init__(id, **kwargs)
    
    def getSourceText (self):
        parser = LuaParser(self.sourceText, self)
        return parser.getComputed()
    
    def getCapability (self):
        capability = MountCapability(self.mountTypeID)
        if capability.exists():
            return capability
    
class MountCapability (AbstractModel):
    TABLE = {"table":"MountCapability", "id_field":"id"}
    def __init__ (self, id, **kwargs):
        super (MountCapability, self).__init__(id, **kwargs)
    
    def getSpellAura (self):
        spell = Spell(self.modSpellAuraID)
        if spell.exists ():
            return spell
    
    def getReqRidingSkillLabel (self):
        labelMapping = {0:"", 75:"Apprentice", 150:"Journeyman", 225:"Artisan", 300:"Expert", 375:"Master"}
        return "{} Riding".format(labelMapping[self.reqRidingSkill]).strip()