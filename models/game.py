from .abstract import GameModel

class CreatureXSpell (GameModel):
    TABLE = {"table":"CreatureXSpell", "id_field":"id"}
    def __init__ (self, id, **kwargs):
        super (CreatureXSpell, self).__init__(id, **kwargs)

class CreatureXMap (GameModel):
    TABLE = {"table":"CreatureXMap", "id_field":"id"}
    def __init__ (self, id, **kwargs):
        super (CreatureXMap, self).__init__(id, **kwargs)