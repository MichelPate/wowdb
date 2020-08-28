from .abstract import AbstractModel

class MawPower (AbstractModel):
    TABLE = {"table":"MawPower", "id_field":"id"}
    def __init__ (self, id, **kwargs):
        super (MawPower, self).__init__(id, **kwargs)
