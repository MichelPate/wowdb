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

preload = (
    CombatRatings,
    CombatRatingsMultByILvl,
    StaminaMultByILvl,
) 
for tbl in preload:
    tbl.All() 