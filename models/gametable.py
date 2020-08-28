from .abstract import AbstractModel

class CombatRatings (AbstractModel):
    TABLE = {"table":"Table_CombatRatings", "id_field":"level"}
    def __init__ (self, id, **kwargs):
        super (CombatRatings, self).__init__(id, **kwargs)

class CombatRatingsMultByILvl (AbstractModel):
    TABLE = {"table":"Table_CombatRatingsMultByILvl", "id_field":"item_level"}
    def __init__ (self, id, **kwargs):
        super (CombatRatingsMultByILvl, self).__init__(id, **kwargs)

class StaminaMultByILvl (AbstractModel):
    TABLE = {"table":"Table_StaminaMultByILvl", "id_field":"item_level"}
    def __init__ (self, id, **kwargs):
        super (StaminaMultByILvl, self).__init__(id, **kwargs)


class SpellScaling (AbstractModel):
    TABLE = {"table":"Table_SpellScaling", "id_field":"level"}
    TYPE_TBL = ["", "item", "consumable", "gem1", "gem2", "gem3", "health", "damagereplacestat", "damagesecondary"]
    def __init__ (self, id, **kwargs):
        super (SpellScaling, self).__init__(id, **kwargs)
    
    def getTypeValue (self, v):
        attr =  self.TYPE_TBL [abs(v)]
        if hasattr (self, attr):
            return getattr(self,attr)
        

preload = (
    # CombatRatings,
    CombatRatingsMultByILvl,
    StaminaMultByILvl,
    SpellScaling,
) 
for tbl in preload:
    tbl.All() 