from .abstract import AbstractModel
from .item import Item
from .spell import Spell, loadManySpells
from .garrison import GarrTalentTree, GarrTalent, GarrTalentRank
from .character import SpecSetMember
import difflib

class Soulbind (AbstractModel):
    TABLE = {"table":"Soulbind", "id_field":"id"}
    def __init__ (self, id, **kwargs):
        super (Soulbind, self).__init__(id, **kwargs)
    
    def getTree (self):
        garrTalents = GarrTalent.FromParent(self.garrTalentTreeID)
        orderedTalents = [[None for c in range(3)] for r in range(8)]
        for talent in garrTalents:
            orderedTalents[talent.tier][talent.uiOrder] = talent
        garrTalentsRanks = [next(iter(GarrTalentRank.FromParent(x.id)), None)for x in garrTalents]
        loadManySpells ([x.perkSpellID for x in garrTalentsRanks if x.perkSpellID])
        return orderedTalents

class SoulbindConduit (AbstractModel):
    soulbindType = ["Finesse", "Potency", "Endurance"]
    TABLE = {"table":"SoulbindConduit", "id_field":"id"}
    def __init__ (self, id, **kwargs):
        super (SoulbindConduit, self).__init__(id, **kwargs)

    def getTypeName (self):
        return self.soulbindType[self.type]

    def getSpecsIDs (self):
        specSets = SpecSetMember.Find({"id_parent":self.specSetID})
        return [x.chrSpecializationID for x in specSets]

class SoulbindConduitItem (AbstractModel):
    TABLE = {"table":"SoulbindConduitItem", "id_field":"id"}
    def __init__ (self, id, **kwargs):
        super (SoulbindConduitItem, self).__init__(id, **kwargs)

    def getItem (self, rank=0):
        return Item(self.itemID, conduit_rank=rank)

class SoulbindConduitRankProperties (AbstractModel):
    TABLE = {"table":"SoulbindConduitRankProperties", "id_field":"id"}
    def __init__ (self, id, **kwargs):
        super (SoulbindConduitRankProperties, self).__init__(id, **kwargs)

class SoulbindConduitRank (AbstractModel):
    TABLE = {"table":"SoulbindConduitRank", "id_field":"id", "id_parent_field":"id_parent"}
    def __init__ (self, id, **kwargs):
        super (SoulbindConduitRank, self).__init__(id, **kwargs)

    def getSpell (self):
        return Spell(self.spellID)


class SoulbindUIDisplayInfo (AbstractModel):
    TABLE = {"table":"SoulbindUIDisplayInfo", "id_field":"id"}
    def __init__ (self, id, **kwargs):
        super (SoulbindUIDisplayInfo, self).__init__(id, **kwargs)

class RenownRewards (AbstractModel):
    TABLE = {"table":"RenownRewards", "id_field":"id", "id_parent_field":"id_parent"}
    def __init__ (self, id, **kwargs):
        super (RenownRewards, self).__init__(id, **kwargs)

    @classmethod
    def getSoulbindUnlockTree (cls):
        # Hacky way to get covenant's rows unlocking levels
        soulbindMapping = {x.name:x.id for x in Soulbind.All()}
        ordinalsMapping = {"first":1, "second":2, "third":3, "fourth":4, "fifth":5, "sixth":6, "seventh":7, "final":8}
        allRewards = cls.All()
        rowEntries = [x for x in allRewards if "Soulbind Row Unlocked" in x.toastDescription]

        finalStr = "Completing the Campaign will allow you to soulbind with "
        rowFinals = [x for x in allRewards if finalStr in x.description]
        
        tree = {i:[1 for row in range (8)] for i in soulbindMapping.values() }

        for entry in rowEntries:
            splitted = entry.description.split()
            soulbindName = entry.description.split("'s")[0].split("You may access ")[-1]
            soulbindNameBis = entry.name.split("Soulbind Upgrade: ")[-1]
            rowIdx = splitted.index("row")
            ordinalID = splitted[rowIdx-1]
            idx = ordinalsMapping[ordinalID]
            soulbindID = soulbindMapping.get(soulbindName, False)
            if not soulbindID :
                allNames = soulbindMapping.keys()
                match = None
                for name in allNames:
                    closestMatch = difflib.get_close_matches(soulbindNameBis, name.split())
                    if closestMatch:
                        match=name
                        break
                if match :
                    soulbindID = soulbindMapping.get(match, False)
            if soulbindID :
                tree[soulbindID][idx-1]=entry.level

        for entry in rowFinals:
            splitted = entry.description.split(finalStr)
            soulbindName = splitted[-1][:-1]
            allNames = soulbindMapping.keys()
            match = None
            soulbindID = soulbindMapping.get(soulbindName, False)
            if not soulbindID:
                for name in allNames:
                    closestMatch = difflib.get_close_matches(name, soulbindName.split())
                    if closestMatch:
                        match=name
                        break
                if match :
                    soulbindID = soulbindMapping.get(match, False)
            if soulbindID:
                tree[soulbindID] = [entry.level if x==1 else x for x in tree[soulbindID] ]

        return tree