from .abstract import AbstractModel
from .spell import Spell
from .mount import Mount

class ItemEffect (AbstractModel):
    TABLE = {"table":"ItemEffect", "id_field":"id", "id_parent_field":"id_parent"}
    def __init__ (self, id, **kwargs):
        super (ItemEffect, self).__init__(id, **kwargs)
        self.ilevel = 1

    def setItemLevel (self, ilvl):
        self.ilevel = ilvl

    def getSpell (self):
        spell = Spell(self.spellID)
        spell.setItemLevel(self.ilevel)
        return spell
    
    def getMount(self):
        spell = self.getSpell()
        if spell.exists():
            mount = next(iter(Mount.Find({"SourceSpellID":spell.id})), None)
            return mount