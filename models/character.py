from .abstract import AbstractModel
# from .spell import SpecializationSpells

class ChrClasses (AbstractModel):
    TABLE = {"table":"ChrClasses", "id_field":"SpellClassSet"}
    def __init__ (self, id, **kwargs):
        super (ChrClasses, self).__init__(id, **kwargs)

class ChrSpecialization (AbstractModel):
    TABLE = {"table":"ChrSpecialization", "id_field":"id", "id_parent_field":"id_parent"}
    def __init__ (self, id, **kwargs):
        super (ChrSpecialization, self).__init__(id, **kwargs)
    
    # def getSpecializationSpells (self):
    #     return SpecializationSpells.FromParent(self.id, parent=self)