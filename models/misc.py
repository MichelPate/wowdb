from .abstract import AbstractModel
from ..utilities import iconBase64Html

class ManifestInterfaceData (AbstractModel):
    TABLE = {"table":"ManifestInterfaceData", "id_field":"id"}
    def __init__ (self, id, **kwargs):
        super (ManifestInterfaceData, self).__init__(id, **kwargs)

    def getIcon (self, size=False, html=False):
        filename = self.fileName.replace(".blp", "")
        return iconBase64Html(filename, size=size, html=html)

class Difficulty (AbstractModel):
    TABLE = {"table":"Difficulty", "id_field":"id"}
    def __init__ (self, id, **kwargs):
        super (Difficulty, self).__init__(id, **kwargs)

class PowerType (AbstractModel):
    TABLE = {"table":"PowerType", "id_field":"PowerTypeEnum"}
    def __init__ (self, id, **kwargs):
        super (PowerType, self).__init__(id, **kwargs)