from .abstract import AbstractModel

class UiModelSceneActor (AbstractModel):
    TABLE = {"table":"UiModelSceneActor", "id_field":"id"}
    def __init__ (self, id, **kwargs):
        super (UiModelSceneActor, self).__init__(id, **kwargs)

class UiTextureAtlas (AbstractModel):
    TABLE = {"table":"UiTextureAtlas", "id_field":"id"}
    def __init__ (self, id, **kwargs):
        super (UiTextureAtlas, self).__init__(id, **kwargs)

class UiTextureAtlasElement (AbstractModel):
    TABLE = {"table":"UiTextureAtlasElement", "id_field":"id"}
    def __init__ (self, id, **kwargs):
        super (UiTextureAtlasElement, self).__init__(id, **kwargs)

class UiTextureAtlasMember (AbstractModel):
    TABLE = {"table":"UiTextureAtlasMember", "id_field":"id"}
    def __init__ (self, id, **kwargs):
        super (UiTextureAtlasMember, self).__init__(id, **kwargs)

class UIMap (AbstractModel):
    TABLE = {"table":"UIMap", "id_field":"id"}
    def __init__ (self, id, **kwargs):
        super (UIMap, self).__init__(id, **kwargs)

class UIMapAssignment (AbstractModel):
    TABLE = {"table":"UIMapAssignment", "id_field":"id"}
    def __init__ (self, id, **kwargs):
        super (UIMapAssignment, self).__init__(id, **kwargs)

class UiMapXMapArt (AbstractModel):
    TABLE = {"table":"UiMapXMapArt", "id_field":"id", "id_parent_field":"id_parent"}
    def __init__ (self, id, **kwargs):
        super (UiMapXMapArt, self).__init__(id, **kwargs)

class UiMapArtTile (AbstractModel):
    TABLE = {"table":"UiMapArtTile", "id_field":"id", "id_parent_field":"id_parent"}
    def __init__ (self, id, **kwargs):
        super (UiMapArtTile, self).__init__(id, **kwargs)