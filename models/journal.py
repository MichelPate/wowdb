from .abstract import AbstractModel
from ..parsers import EncounterSectionParser
import operator

class JournalEncounter (AbstractModel):
    TABLE = {"table":"JournalEncounter", "id_field":"id"}
    def __init__ (self, id, **kwargs):
        super (JournalEncounter, self).__init__(id, **kwargs)
    
    def getSections (self):
        sections = JournalEncounterSection.Find({"JournalEncounterID":self.id}) 
        sortedSections = sorted(sections, key=operator.attrgetter('orderIndex'))
        return sortedSections
    
    def getItems (self):
        items = JournalEncounterItem.Find({"id_encounter":self.id})
        return items

    def getOverviewSections (self):
        sections = self.getSections()
        overviewSections = [x for x in sections if x.type==3]
        return overviewSections
    
    def getAbilitiesSections (self):
        pass

class JournalEncounterCreature (AbstractModel):
    TABLE = {"table":"JournalEncounterCreature", "id_field":"id"}
    def __init__ (self, id, **kwargs):
        super (JournalEncounterCreature, self).__init__(id, **kwargs)

class JournalEncounterItem (AbstractModel):
    TABLE = {"table":"JournalEncounterItem", "id_field":"id"}
    def __init__ (self, id, **kwargs):
        super (JournalEncounterItem, self).__init__(id, **kwargs)

class JournalEncounterSection (AbstractModel):
    TABLE = {"table":"JournalEncounterSection", "id_field":"id"}
    def __init__ (self, id, **kwargs):
        super (JournalEncounterSection, self).__init__(id, **kwargs)
    
    def getDescription (self):
        parser = EncounterSectionParser(self.bodyText, self)
        return parser.getComputed().strip()

class JournalEncounterXDifficulty (AbstractModel):
    TABLE = {"table":"JournalEncounterXDifficulty", "id_field":"id"}
    def __init__ (self, id, **kwargs):
        super (JournalEncounterXDifficulty, self).__init__(id, **kwargs)

class JournalInstance (AbstractModel):
    TABLE = {"table":"JournalInstance", "id_field":"id"}
    def __init__ (self, id, **kwargs):
        super (JournalInstance, self).__init__(id, **kwargs)
    
    def getEncounters (self):
        encounters = JournalEncounter.Find({"JournalInstanceID":self.id}) 
        sortedEncounters = sorted(encounters, key=operator.attrgetter('orderIndex'))
        return sortedEncounters

class JournalItemXDifficulty (AbstractModel):
    TABLE = {"table":"JournalItemXDifficulty", "id_field":"id"}
    def __init__ (self, id, **kwargs):
        super (JournalItemXDifficulty, self).__init__(id, **kwargs)

class JournalTier (AbstractModel):
    TABLE = {"table":"JournalTier", "id_field":"id"}
    def __init__ (self, id, **kwargs):
        super (JournalTier, self).__init__(id, **kwargs)

class JournalTierXInstance (AbstractModel):
    TABLE = {"table":"JournalTierXInstance", "id_field":"id"}
    def __init__ (self, id, **kwargs):
        super (JournalTierXInstance, self).__init__(id, **kwargs)