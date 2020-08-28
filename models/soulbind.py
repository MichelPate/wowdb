from .abstract import AbstractModel
from .item import Item
from .spell import Spell

class Soulbind (AbstractModel):
    TABLE = {"table":"Soulbind", "id_field":"id"}
    def __init__ (self, id, **kwargs):
        super (Soulbind, self).__init__(id, **kwargs)

class SoulbindConduit (AbstractModel):
    TABLE = {"table":"SoulbindConduit", "id_field":"id"}
    def __init__ (self, id, **kwargs):
        super (SoulbindConduit, self).__init__(id, **kwargs)

class SoulbindConduitItem (AbstractModel):
    TABLE = {"table":"SoulbindConduitItem", "id_field":"id"}
    def __init__ (self, id, **kwargs):
        super (SoulbindConduitItem, self).__init__(id, **kwargs)

    def getItem (self):
        return Item(self.itemID)

class SoulbindConduitRank (AbstractModel):
    TABLE = {"table":"SoulbindConduitRank", "id_field":"id", "id_parent_field":"id_parent"}
    def __init__ (self, id, **kwargs):
        super (SoulbindConduitRank, self).__init__(id, **kwargs)

    def getSpell (self):
        return Item(self.spellID)

class SoulbindUIDisplayInfo (AbstractModel):
    TABLE = {"table":"SoulbindUIDisplayInfo", "id_field":"id"}
    def __init__ (self, id, **kwargs):
        super (SoulbindUIDisplayInfo, self).__init__(id, **kwargs)