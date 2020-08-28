from .abstract import AbstractModel
from .spell import Spell
from .reagents import SpellReagents
import operator

class SkillLine (AbstractModel):
    TABLE = {"table":"SkillLine", "id_field":"id"}
    def __init__ (self, id, **kwargs):
        super (SkillLine, self).__init__(id, **kwargs)

    def getAbilities (self):
        abilities = SkillLineAbility.FromSkillLine(self.id)  
        return list(sorted(abilities, key=operator.attrgetter('trivialSkillLineRankLow')))

class SkillLineAbility (AbstractModel):
    TABLE = {"table":"SkillLineAbility", "id_field":"id", "id_parent_field":"id_parent"}
    def __init__ (self, id, **kwargs):
        super (SkillLineAbility, self).__init__(id, **kwargs)
    
    def getSpell (self):
        return Spell (self.spell)

    def getSpellReagents (self):
        return SpellReagents.FromSpellID(self.spell)

    @classmethod
    def FromSkillLine (self, skillLineID):
        return self.Find ({"SkillupSkillLineID":skillLineID})