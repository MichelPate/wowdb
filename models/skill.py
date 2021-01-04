from .abstract import AbstractModel
from .spell import Spell
from .misc import ManifestInterfaceData
from .reagents import SpellReagents
from ..utilities import s
import operator

class SkillLine (AbstractModel):
    TABLE = {"table":"SkillLine", "id_field":"id"}
    def __init__ (self, id, **kwargs):
        super (SkillLine, self).__init__(id, **kwargs)

    def getAbilities (self):
        abilities = SkillLineAbility.FromSkillLine(self.id)  
        return list(sorted(abilities, key=operator.attrgetter('trivialSkillLineRankLow')))
    
    def getIcon (self, size=35, **kwargs):
        if self.spellIconFileID != 0 :
            uiData = ManifestInterfaceData(self.spellIconFileID)
            return uiData.getIcon(size, **kwargs)
    
    def getTooltipText (self, displayLevel=1):
        lines = ""
        lines += '<table width="100%">'
        lines += '<tr>'
        lines += '<td {style}>{name}</td>'.format(name=self.displayName, style = s(size=14, weight=700))
        lines += '<td style="text-align: right;">{icon}</td>'.format(icon=self.getIcon(size=35, borderColor=(0,0,0)))
        lines += '</tr>'
        if self.description:
            lines += '<tr>'
            lines += '<td {style}>{nameDesc}</td>'.format(nameDesc = self.description , style=s(size=12) )
            lines += '</tr>'
        lines += '</table>'
        return lines

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