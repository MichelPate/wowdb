from .abstract import AbstractModel
from .spell import Spell
from ..parsers import LuaParser

class RuneforgeLegendaryAbility (AbstractModel):
    TABLE = {"table":"RuneforgeLegendaryAbility", "id_field":"id"}
    def __init__ (self, id, **kwargs):
        super (RuneforgeLegendaryAbility, self).__init__(id, **kwargs)
    
    def getSpell (self):
        if self.spellID:
            return Spell(self.spellID)