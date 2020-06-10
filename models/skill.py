from .abstract import AbstractModel

class SkillLine (AbstractModel):
    TABLE = {"table":"SkillLine", "id_field":"id"}
    def __init__ (self, id, **kwargs):
        super (SkillLine, self).__init__(id, **kwargs)


class SkillLineAbility (AbstractModel):
    TABLE = {"table":"SkillLineAbility", "id_field":"id", "id_parent_field":"id_parent"}
    def __init__ (self, id, **kwargs):
        super (SkillLineAbility, self).__init__(id, **kwargs)