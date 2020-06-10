from .abstract import AbstractModel
from ..parsers import EnchantmentDescriptionParser
from ..utilities import arrayFromB32
class SpellItemEnchantment (AbstractModel):
    TABLE = {"table":"SpellItemEnchantment", "id_field":"id"}
    def __init__ (self, id, **kwargs):
        super (SpellItemEnchantment, self).__init__(id, **kwargs)
    
    def getName (self):
        parsed = EnchantmentDescriptionParser(self.name, self)
        return parsed.getComputed()

    def getFlags (self):
        return arrayFromB32 (self.flags)