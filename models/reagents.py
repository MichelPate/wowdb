from .abstract import AbstractModel
from .item import Item

class SpellReagents (AbstractModel):
    TABLE = {"table":"SpellReagents", "id_field":"id"}
    def __init__ (self, id, **kwargs):
        super (SpellReagents, self).__init__(id, **kwargs)
    
    def getReagents (self):
        return {Item(self.reagent[i]):self.reagentCount[i] for i in range (1,9) if self.reagent[i]}

    @classmethod
    def FromSpellID (self, spellID):
        return next(iter(self.Find ({"SpellID":spellID})), None)