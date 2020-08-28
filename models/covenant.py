from .abstract import AbstractModel

class Covenant (AbstractModel):
    TABLE = {"table":"Covenant", "id_field":"id"}
    def __init__ (self, id, **kwargs):
        super (Covenant, self).__init__(id, **kwargs)


class UICovenantAbility (AbstractModel):
    TABLE = {"table":"UICovenantAbility", "id_field":"id"}
    def __init__ (self, id, **kwargs):
        super (UICovenantAbility, self).__init__(id, **kwargs)
