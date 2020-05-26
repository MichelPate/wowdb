from .abstract import AbstractModel
from .misc import ManifestInterfaceData
from .gametable import CombatRatings, CombatRatingsMultByILvl, StaminaMultByILvl
from ..constants import CHR_STATS
from ..utilities import s
import math

class Item (AbstractModel):
    TABLE = {"table":"Item", "id_field":"id"}
    def __init__ (self, id, **kwargs):
        self.bonuses = kwargs.get("bonuses", [])
        super (Item, self).__init__(id, **kwargs)
    
    @property
    def name (self):
        sparse = self.getSparse()
        if sparse :
            return sparse.display
        return ""
    
    def modifiedAppearance(self):
        return ItemModifiedAppearance.FromParent(self.id, parent=self)

    def getModifiedAppearance (self):
        ma = self.modifiedAppearance()
        if ma : 
            return ma[0]

    def getSparse (self):
        sparse = ItemSparse(self.id)
        if sparse.exists():
            return sparse
    
    def getIcon (self, size=35, html=True):
        if self.iconFileDataID != 0 :
            uiData = ManifestInterfaceData(self.iconFileDataID)
            return uiData.getIcon(size)
        else :
            ma = self.getModifiedAppearance()
            return ma.getIcon(size)
            
    
    def getShortText(self, iconSize = 15):
        return '<span style="text-align: right;">{icon}</span> {name}'.format(icon=self.getIcon(size=iconSize, html=True), name=self.name)

    def getTooltipText (self, displayLevel=1):
        lines = ""
        sparse = self.getSparse()
        # Header
        lines += '<table width="100%">'
        lines += '<tr>'
        lines += '<td {style}>{name}</td>'.format(name=self.name, style = s(size=14, weight=700))
        lines += '<td style="text-align: right;">{icon}</td>'.format(icon=self.getIcon(size=35, html=True))
        lines += '</tr>'
        lines += '</table>'

        stats = sparse.getStats()

        lines += '<table width="100%">'
        for stat in stats :
            lines += '<tr>'
            lines += '<td {style}>{}</td>'.format("+{} {}".format(stat["amount"], stat["name"]) , style=s(size=12) )
            lines += '</tr>'
        lines += '</table>'

        return lines

class ItemSparse (AbstractModel):
    TABLE = {"table":"ItemSparse", "id_field":"id"}
    def __init__ (self, id, **kwargs):
        super (ItemSparse, self).__init__(id, **kwargs)
    
    def getStats (self):
        print (self.itemLevel)
        propPoints = RandPropPoints[self.itemLevel]
        crMult = CombatRatingsMultByILvl[self.itemLevel]
        stamMult = StaminaMultByILvl[self.itemLevel]
        budgets = propPoints.epic

        # This must be somewhere in DB
        INVTYPE = {
            0: -1,
            1: 0, #Head	
            2: 2, #Neck
            3: 1, #Shoulder	
            4: -1, #Shirt
            5: 0, #Chest
            6: 1, #Waist
            7: 0, #Legs	
            8: 1, #Feet
            9: 2, #Wrist
            10: 1, #Hands
            11: 2, #Finger	
            12: 1, #Trinket
            13: 3, #One-Hand	
            14: 3, #Shield	
            15: 0, #Bow
            16: 2, #Cloak	
            17: 0, #2hands
            20: 0, #Chest
            21: 0, #Main Hand
            22: 3, # Weapon Off Hand	
            23: 3, # Held Off Hand	
            26: 3, # Ranged
        }
        PRIMARY_STATS = [3,4,5,6,71,72,73,74]
        stats = [{"name":CHR_STATS[k], "id":k, "alloc":v} for k, v in zip(self.statModifierBonusStat.values(), self.statPercentEditor.values()) if k!=-1]
        # print (crMult, budgets, stats)

        
        if self.inventoryType in [11,2] : # Neck and Rings
            staminaPenalty = stamMult.jewelryMultiplier
            crPenalty = crMult.jewelryMultiplier
        else:
            staminaPenalty = stamMult.armorMultiplier
            crPenalty = crMult.armorMultiplier
        
        for i, stat in enumerate(stats):
            amount = budgets[INVTYPE[self.inventoryType]+1]*stat["alloc"]
            if stat["id"] == 7 : 
                amount *= staminaPenalty
            elif stat["id"] not in PRIMARY_STATS :
                amount *= crPenalty
            amount=amount*0.0001
            stats[i]["amount"] = int(math.floor(amount)) 
        
        return stats

class ItemAppearance (AbstractModel):
    TABLE = {"table":"ItemAppearance", "id_field":"id"}
    def __init__ (self, id, **kwargs):
        super (ItemAppearance, self).__init__(id, **kwargs)
    def getIcon (self, size):
        uiData = ManifestInterfaceData(self.defaultIconFileDataID) 
        return uiData.getIcon(size)

class ItemModifiedAppearance (AbstractModel):
    TABLE = {"table":"ItemModifiedAppearance", "id_field":"id", "id_parent_field":"id_parent"}
    def __init__ (self, id, **kwargs):
        super (ItemModifiedAppearance, self).__init__(id, **kwargs)
    
    def getIcon (self, size) :
        itemAppeareance = ItemAppearance(self.itemAppearanceID)
        return itemAppeareance.getIcon(size)

class ItemNameDescription (AbstractModel):
    TABLE = {"table":"ItemNameDescription", "id_field":"id"}
    def __init__ (self, id, **kwargs):
        super (ItemNameDescription, self).__init__(id, **kwargs)

class ItemBonus (AbstractModel):
    TABLE = {"table":"ItemBonus", "id_field":"id", "id_parent_field":"id_parent"}
    def __init__ (self, id, **kwargs):
        super (ItemBonus, self).__init__(id, **kwargs)

class ItemBonusListLevelDelta (AbstractModel):
    TABLE = {"table":"ItemBonusListLevelDelta", "id_field":"id"}
    def __init__ (self, id, **kwargs):
        super (ItemBonusListLevelDelta, self).__init__(id, **kwargs)

class ItemBonusTreeNode (AbstractModel):
    TABLE = {"table":"ItemBonusTreeNode", "id_field":"id", "id_parent_field":"id_parent"}
    def __init__ (self, id, **kwargs):
        super (ItemBonusTreeNode, self).__init__(id, **kwargs)

class ItemXBonusTree (AbstractModel):
    TABLE = {"table":"ItemXBonusTree", "id_field":"id", "id_parent_field":"id_parent"}
    def __init__ (self, id, **kwargs):
        super (ItemXBonusTree, self).__init__(id, **kwargs)

class ItemClass (AbstractModel):
    TABLE = {"table":"ItemClass", "id_field":"id"}
    def __init__ (self, id, **kwargs):
        super (ItemClass, self).__init__(id, **kwargs)

class ItemSubClass (AbstractModel):
    TABLE = {"table":"ItemSubClass", "id_field":"id"}
    def __init__ (self, id, **kwargs):
        super (ItemSubClass, self).__init__(id, **kwargs)

class RandPropPoints (AbstractModel):
    TABLE = {"table":"RandPropPoints", "id_field":"id"}
    def __init__ (self, id, **kwargs):
        super (RandPropPoints, self).__init__(id, **kwargs)

preload = (
    ItemClass, 
    ItemSubClass, 
    ItemNameDescription,
    ItemBonus,
    ItemBonusListLevelDelta,
    RandPropPoints,
) 
for tbl in preload:
    tbl.All() 