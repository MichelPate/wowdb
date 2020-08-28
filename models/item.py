from .abstract import AbstractModel
from .character import ChrClasses
from .misc import ManifestInterfaceData, RandPropPoints
from .itemEffect import ItemEffect
from .spellItemEnchantment import SpellItemEnchantment
from .gametable import CombatRatingsMultByILvl, StaminaMultByILvl
from ..constants import CHR_STATS, ITEM_INVTYPE, INVENTORY_TYPES, CHR_PRIMARY_STATS, ITEM_MATERIAL_TYPES, ITEM_QUALITY_COLORS, ITEM_FLAGS
from ..utilities import iconBase64Html, FormatOutput, formatGold, arrayFromB32, s
import math
import itertools
import operator


def loadManyItems (data):
    indices = [x["id"] for x in data]
    items = Item.Many(indices)
    sparses = ItemSparse.Many(indices)
    modifiedAppearance = ItemModifiedAppearance.Many(indices, field="id_parent")
    ManifestInterfaceData.Many([x.itemAppearanceID for x in modifiedAppearance])
    return [Item(x.pop("id"), **x) for x in data]

class Item (AbstractModel):
    TABLE = {"table":"Item", "id_field":"id"}
    def __init__ (self, id, **kwargs):
        super (Item, self).__init__(id, **kwargs)
        self.bl = kwargs.get ("bl", [])
        self.enchant = None
        self.gems = None
        gemsIds = kwargs.get("gems", None)
        enchantId = kwargs.get("enchant", None)
        if enchantId :
            self.setEnchantment (enchantId)
        if gemsIds :
            self.setGems (gemsIds)


    @property
    def name (self):
        sparse = self.getSparse()
        if sparse :
            return sparse.display
        return ""
    
    def setEnchantment (self, enchantId):
        itemEchantment = SpellItemEnchantment(enchantId)
        if itemEchantment.exists() :
            self.enchant = itemEchantment

    def setGems (self, gems):
        if isinstance (gems, int):
            gems = [gems]
        self.gems = []
        for gem in gems:
            item = Item(gem)
            sparse = item.getSparse()
            if item.exists() and sparse.gemProperties:
                self.gems.append(item)
            
    def getArmor (self):
        sparse = self.getSparse()
        if sparse :
            # All ItemArmorQuality entries are the same
            # Let's just always use the same one to avoid queries
            
            quality = sparse.getQuality()
            ilvl = sparse.getItemLevel()
            subClass = self.getSubclass()
            armorType = subClass.displayName.lower ()

            if armorType == "shield":
                sparse = self.getSparse()
                ilvl = sparse.getItemLevel()
                armorShield = ItemArmorShield[ilvl]
                armorValue = armorShield.quality[quality]
                return math.floor(armorValue+0.5)
            
            armorQuality = ItemArmorQuality(1)
            armorQualityMod = armorQuality.qualitymod[quality]
            armorLocation = ArmorLocation[self.inventoryType]
            armorTotal = ItemArmorTotal[ilvl]

            if hasattr(armorTotal, armorType) :
                attrArmorLoc = "{}modifier".format(armorType)
                invTypMod = getattr(armorLocation, attrArmorLoc.replace("mail", "chain"))
                armorValue = getattr(armorTotal, armorType)
                return math.floor(armorValue*armorQualityMod*invTypMod+0.5)
            

    def getBonusList (self):
        return [ItemBonus[idx] for idx in self.bl]
           
    def getMaterial (self):
        return ITEM_MATERIAL_TYPES.get(self.material, None)

    def effects(self):
        effects = ItemEffect.FromParent(self.id, parent=self)
        sparse = self.getSparse()
        if sparse :
            ilvl = sparse.getItemLevel()
            for effect in effects :
                effect.setItemLevel (ilvl)
        return effects

    def modifiedAppearance(self):
        return ItemModifiedAppearance.FromParent(self.id, parent=self)

    def getModifiedAppearance (self):
        ma = self.modifiedAppearance()
        if ma : 
            return ma[0]
    
    def xBonusTree (self):
        return ItemXBonusTree.FromParent(self.id, parent=self)
    
    def getEffects (self):
        effects = self.effects()
        if effects : 
            return effects
        return []
    
    def getBonusTrees (self):
        effects = self.effects()
        if effects : 
            return effects
        return []

    def getSearchName (self):
        return ItemSearchName(self.id)

    def getSparse (self):
        sparse = ItemSparse(self.id, bl=self.bl)
        if sparse.exists():
            return sparse
        else :
            searchName = self.getSearchName()
            if searchName.exists():
                items = ItemSearchName.Find({"Display_lang":searchName.display})
                for item in items:
                    sparse = item.getSparse()
                    if sparse :
                        return sparse
    
    def getIcon (self, size=35, **kwargs):
        sparse = self.getSparse()
        d = kwargs
        if sparse:
            qualityColor = sparse.getQualityColor()
            d.update({"borderColor":qualityColor})
        if self.iconFileDataID != 0 :
            uiData = ManifestInterfaceData(self.iconFileDataID)
            return uiData.getIcon(size, **d)
        else :
            ma = self.getModifiedAppearance()
            return ma.getIcon(size, **d)
        
    def getShortText(self, iconSize = 15, **kwargs):
        icon = self.getIcon(size=iconSize, **kwargs)
        return '<p {style}><span style="text-align: right;">{icon}</span> {name}</p>'.format(icon=icon, name=self.name, style=s(size=12, color=qualityColor))

    def getSubclass (self):
        return next(iter(ItemSubClass.FindReference({"classID":self.classID, "subClassID":self.subclassID})), None)

    def getWeaponDps (self):
        if self.classID == 2 :
            sparse = self.getSparse()
            ilvl = sparse.getItemLevel()
            WEAPON_DAMAGE_TYPES = {1:ItemDamageTwoHand, 2:ItemDamageTwoHandCaster ,3:ItemDamageOneHand, 8:ItemDamageOneHand}
            # Change sheatheType to SubClass
            damageType = WEAPON_DAMAGE_TYPES[sparse.sheatheType][ilvl]
            return round(damageType.quality[sparse.overallQualityID+1], 1)
    
    def getWeaponSpeed(self):
        if self.classID == 2 :
            sparse = self.getSparse()
            return sparse.itemDelay * 0.001
    
    def getWeaponDamageRange (self):
        if self.classID == 2 :
            sparse = self.getSparse()
            dps = self.getWeaponDps()
            speed = self.getWeaponSpeed()
            minDmg = math.floor( dps * speed * ( 1 - sparse.dmgVariance * 0.5 ) ) 
            maxDmg = math.ceil( dps * speed * ( 1 + sparse.dmgVariance * 0.5 ) )
            return (minDmg, maxDmg)

    def getTooltipText (self, displayLevel=1):
        lines = ""
        BONDING_TYPES = ["No bounds", "Binds when picked up", "Binds when equipped", "Binds when used", "Quest item", "Quest Item1"]
        # Get elements
        sparse = self.getSparse()
        subClass = self.getSubclass()
        effects = self.getEffects()
        ilvl = sparse.getItemLevel()
        nameDesc = sparse.getNameDescription()
        flags = sparse.getFlags()
        mount = next(filter(None, [x.getMount() for x in effects if x.exists()]), False)

        # Header
        lines += '<table width="100%">'
        lines += '<tr>'
        lines += '<td {style}>{name}</td>'.format(name=self.name, style = s(size=14, weight=700, color=sparse.getQualityColor()))
        lines += '<td style="text-align: right;">{icon}</td>'.format(icon=self.getIcon(size=35, borderColor=(0,0,0)))
        lines += '</tr>'
        if nameDesc :
            lines += '<tr>'
            lines += '<td {style}>{nameDesc}</td>'.format(nameDesc = nameDesc.description , style=s(size=12, color=(30,255,0)) )
            lines += '</tr>'
        lines += '<tr>'
        lines += '<td {style}>Item Level {ilvl}</td>'.format(ilvl = ilvl , style=s(size=12, color=(255, 209, 0)) )
        lines += '</tr>'
        if mount :
            lines += '<tr>'
            lines += '<td {style}>Mount <span style="color:#9d9d9d">(Account-wide)</span></td>'.format(style=s(size=12) )
            lines += '</tr>'
        if sparse.bonding >0:
            lines += '<tr>'
            lines += '<td {style}>{bonding}</td>'.format(bonding = BONDING_TYPES[sparse.bonding] , style=s(size=12) )
            lines += '</tr>'
        if sparse.description and (26 in flags or mount):
            lines += '<tr>'
            lines += '<td {style}>Use: {description}</td>'.format(description = sparse.description , style=s(size=12, color=(30,255,0)) )
            lines += '</tr>'
        lines += '</table>'

        # Equipment
        if sparse.inventoryType != 0 :
            lines += '<table width="100%">'
            if 20 in flags :
                lines += '<tr>'
                lines += '<td {style}>Unique-Equipped</td>'.format(style=s(size=12) )
                lines += '</tr>'

            lines += '<tr>'
            lines += '<td {style}>{invType}</td>'.format(invType = INVENTORY_TYPES[sparse.inventoryType] , style=s(size=12) )
            lines += '<td {style}>{subclass}</td>'.format(subclass = subClass.displayName , style=s(size=12) )
            lines += '</tr>'

            # Weapon
            if self.classID == 2 : 
                dps = self.getWeaponDps()
                speed = self.getWeaponSpeed()
                minDmg, maxDmg = self.getWeaponDamageRange()

                lines += '<tr>'
                lines += '<td {style}>{minDmg} - {maxDmg} Damage</td>'.format(minDmg=minDmg,maxDmg=maxDmg, style=s(size=12) )
                lines += '</tr>'
                lines += '<tr>'
                lines += '<td {style}>({dps} damage per second)</td>'.format(dps=dps, style=s(size=12) )
                lines += '<td {style}>Speed {speed:.2f}</td>'.format(speed=speed, style=s(size=12) )
                lines += '</tr>'   
            lines += '</table>'

            armor = self.getArmor()
            stats = sparse.getStats()
            lines += '<table width="100%">'
            if armor :
                lines += '<tr>'
                lines += '<td {style}>{armor} Armor</td>'.format(armor=int(armor), style=s(size=12) )
                lines += '</tr>'
            for stat in stats :
                statColor = (30,255,0)
                if stat["id"] in CHR_PRIMARY_STATS+[7]:
                    statColor = (255,255,255)
                lines += '<tr>'
                lines += '<td {style}>{}</td>'.format("+{} {}".format(stat["amount"], stat["name"]) , style=s(size=12, color=statColor) )
                lines += '</tr>'
            
            if sparse.isIndestructible() :
                lines += '<tr>'
                lines += '<td {style}>Indestructible</td>'.format(style=s(size=12, color=statColor) )
                lines += '</tr>'

            if self.enchant :
                lines += '<tr>'
                lines += '<td {style}>Enchanted: {enchantment}</td>'.format(enchantment = self.enchant.getName() , style=s(size=12, color=(30,255,0)) )
                lines += '</tr>'

            lines += '</table>'
        
        sockets = sparse.getSockets()
        if sockets :
            lines += '<table width="100%">'
            if self.gems :
                for gem in self.gems :
                    gemSparse = gem.getSparse()
                    gemProp = GemProperties (gemSparse.gemProperties)
                    gemEnchant = SpellItemEnchantment (gemProp.enchantID)
                    
                    lines += '<tr>'
                    lines += '<td {style}>{}</td>'.format("{icon} {text}".format(icon=gem.getIcon(size=15), text=gemEnchant.getName()), style=s(size=12, color=(163,53,206)) )
                    lines += '</tr>'
            else :
                
                for socket in sockets:
                    lines += '<tr>'
                    lines += '<td {style}>{}</td>'.format(socket, style=s(size=12) )
                    lines += '</tr>'
            
            if sparse.socketMatchEnchantmentID :
                socketBonus = SpellItemEnchantment (sparse.socketMatchEnchantmentID)
                lines += '<tr>'
                lines += '<td {style}>{}</td>'.format("{text}".format(text=socketBonus.getName()), style=s(size=12, color=(150,150,150)) )
                lines += '</tr>'

            lines += '</table>'

        
        triggersTypes = ["Use", "Equip", "UNK2", "UNK3", "UNK4", "UNK5", "Use"]
        skill = sparse.getSkill()
        lines += '<table width="100%">'
        
        for effect in effects :
            spell = effect.getSpell()

            spellEffect = spell.getCurrentEffects()[0]
            spellEffectItemID = spellEffect.effectItemType
            if spellEffectItemID and spellEffectItemID != self.id:
                spellEffectItem = Item(spellEffectItemID)
                lines += "<br>"
                lines += spellEffectItem.getTooltipText()

            if spell.description and not mount:
                cd=False
                triggerType = triggersTypes[effect.triggerType]
                if effect.triggerType == 0 :
                    cd = spell.getCooldown(formatType="short")
                cooldown = " ({} cooldown)".format(cd) if cd else ""
                lines += '<tr>'
                lines += '<td {style}>{triggerType}: {description}{cooldown}</td>'.format(triggerType=triggerType,description=spell.getDescription(),cooldown=cooldown, style=s(size=12, color=(30,255,0)) )
                lines += '</tr>'
        if skill :
            lines += '<tr>'
            lines += '<td {style}>Requires {skill} ({skillLevel})</td>'.format(skill=skill.displayName, skillLevel=sparse.requiredSkillRank, style=s(size=12))
            lines += '</tr>'
        if 64 in flags :
            lines += '<tr>'
            lines += '<td {style}>Crafting Reagent</td>'.format(style=s(size=12, color=(102,187,255)))
            lines += '</tr>'
        if sparse.stackable > 1:
            lines += '<tr>'
            lines += '<td {style}>Max Stack: {maxStack}</td>'.format(maxStack=sparse.stackable, style=s(size=12))
            lines += '</tr>'
        if sparse.requiredLevel:
            lines += '<tr>'
            lines += '<td {style}>Requires Level {level}</td>'.format(level=sparse.requiredLevel, style=s(size=12))
            lines += '</tr>'
        if sparse.allowableClass:
            chrClasse = ChrClasses(sparse.allowableClass)
            if chrClasse.exists() :
                lines += '<tr>'
                lines += '<td {style}>Requires {chrClass}</td>'.format(chrClass=chrClasse.name, style=s(size=12))
                lines += '</tr>'
        if 3 in flags :
            lines += '<tr>'
            lines += '<td {style}>&lt;Right Click to Open&gt;</td>'.format(style=s(size=12, color=(30,255,0)))
            lines += '</tr>'
        if mount :
            mountCapability = mount.getCapability()
            ridingLabel = mountCapability.getReqRidingSkillLabel()
            lines += '<tr>'
            lines += '<td {style}>Requires {ridingLabel}</td>'.format(ridingLabel = ridingLabel, style=s(size=12) )
            lines += '</tr>'
        if sparse.description and not (26 in flags or mount):
            lines += '<tr>'
            lines += '<td {style}>"{description}"</td>'.format(description = sparse.description , style=s(size=12, color=(255, 209, 0)) )
            lines += '</tr>'
        if mount :
            lines += '<tr>'
            lines += '<td {style}>"{mountDesc}"</td>'.format(mountDesc = mount.description , style=s(size=12, color=(255, 209, 0)) )
            lines += '</tr>'
            lines += '<tr>'
            lines += '<td {style}>{mountSource}</td>'.format(mountSource = mount.getSourceText() , style=s(size=12) )
            lines += '</tr>'
        if sparse.sellPrice:
            lines += '<tr>'
            lines += '<td {style}>Sell Price: {sellPrice}</td>'.format(sellPrice=sparse.getSellPrice(), style=s(size=12))
            lines += '</tr>'
        lines += '</table>'
        
        if displayLevel > 1:
            # Flags
            lines += '<p {style}>Flags</p>'.format(style = s(size=12, weight=700))
            lines += '<ul style="list-style: none;">'
            for flag in flags:
                lines += "<li {style}>&bull; {flag}</li>".format(flag=ITEM_FLAGS.get(flag, "UNK FLAG {}".format(flag)), style= s(size=11))
            lines += '</ul>'

        #ID 
        lines += '<br>'
        lines += '<p {style}>ID: {}</p>'.format(self.id, style= s(size=11))
        return lines

class ItemSearchName (AbstractModel):
    TABLE = {"table":"ItemSearchName", "id_field":"id"}
    def __init__ (self, id, **kwargs):
        super (ItemSearchName, self).__init__(id, **kwargs)
        self.bl = kwargs.get ("bl", [])

    def getNameDescription (self):
        bl = self.getBonusList()
        nameDescId = 0
        for bonus in bl :
            if bonus.exists() and bonus.type == 4:
                nameDescId = bonus.value[1]
        if nameDescId :
            return ItemNameDescription[nameDescId]

    def getBonusList (self):
        return sum([ItemBonus.FromParent(idx, self) for idx in self.bl], [])

    def getItemLevel (self):
        bl = self.getBonusList()
        ilvl = self.itemLevel
        for bonus in bl :
            if bonus.exists() and bonus.type == 1:
                ilvl+=sum(bonus.value.values())
        return ilvl

    def getFlags (self):
        return sum([[f+(i*32) for f in arrayFromB32(x)] for i, x in enumerate(self.flags.values())], [])

    def getQuality (self):
        bl = self.getBonusList()
        quality = self.overallQualityID
        for bonus in bl :
            if bonus.exists() and bonus.type == 3:
                bonusQuality = max(bonus.value.values())
                if bonusQuality > quality:
                    quality = bonusQuality
        return quality
    def getQualityColor (self):
        quality = self.getQuality()
        if quality < len(ITEM_QUALITY_COLORS):
            return ITEM_QUALITY_COLORS[quality]
        return (255,255,255)
    
    def getSparse (self):
        sparse = ItemSparse(self.id)
        if sparse.exists():
            return sparse

class ItemSparse (ItemSearchName):
    TABLE = {"table":"ItemSparse", "id_field":"id"}
    def __init__ (self, id, **kwargs):
        super (ItemSparse, self).__init__(id, **kwargs)
        
    def getMaterial (self):
        return ITEM_MATERIAL_TYPES.get(self.material, None)

    def getAllowableClass (self):
        return arrayFromB32(self.allowableClass)

    def getInventoryTypeName (self):
        return INVENTORY_TYPES[self.inventoryType]

    def getSkill (self):
        if self.requiredSkill :
            from .skill import SkillLine
            return SkillLine(self.requiredSkill)

    def getSockets (self, size=15, html=True):
        result = []
        sockets = list(self.socketType.values())

        bl = self.getBonusList()
        for bonus in bl :
            if bonus.exists() and bonus.type == 6:
                count = bonus.value[1]
                for i in range (count):
                    sockets.append(bonus.value[2])

        socketTypesMapping = {1:"meta", 2:"red", 4:"yellow", 7:"prismatic", 8:"blue", 19:"punchcardred", 20:"punchcardyellow", 21:"punchcardblue"}
        for socketType in sockets:
            if socketType!=0:
                socketName = socketTypesMapping[socketType]
                filename = "ui-emptysocket-{socketType}".format(socketType=socketName)
                icon = iconBase64Html(filename, size=size, html=html)
                result.append( '{icon} <span style="color:#9d9d9d">{name} Socket</span>'.format(icon=icon, name=socketName.title()))
        return result

    def isIndestructible (self):
        bl = self.getBonusList()
        return any( bonus for bonus in bl if bonus.type==2 and bonus.value[1] == 64 )

    @FormatOutput(formatGold)
    def getSellPrice (self):
        return self.sellPrice

    def getStats (self):
        ilvl = self.getItemLevel()
        bl = self.getBonusList()
        
        propPoints = RandPropPoints[ilvl]
        crMult = CombatRatingsMultByILvl[ilvl] #GameTable
        stamMult = StaminaMultByILvl[ilvl]
        budgets = propPoints.epic

        stats = [{"name":CHR_STATS[k], "id":k, "alloc":v} for k, v in zip(self.statModifierBonusStat.values(), self.statPercentEditor.values()) if k!=-1]

        # Tertiary Stats
        excludeTertiaries = (22,23, 64) 
        stats += [{"name":CHR_STATS[bonus.value[1]], "id":bonus.value[1], "alloc":bonus.value[2]} for bonus in bl if bonus.type==2 and bonus.value[1] not in excludeTertiaries]

        if self.inventoryType in [11,2] : # Neck and Rings
            staminaPenalty = stamMult.jewelryMultiplier
            crPenalty = crMult.jewelryMultiplier
        else:
            staminaPenalty = stamMult.armorMultiplier
            crPenalty = crMult.armorMultiplier
        
        for i, stat in enumerate(stats):
            amount = budgets[ITEM_INVTYPE[self.inventoryType]+1]*stat["alloc"]
            if stat["id"] == 7 : 
                amount *= staminaPenalty
            elif stat["id"] not in CHR_PRIMARY_STATS :
                amount *= crPenalty
            amount*=0.0001
            stats[i]["amount"] = int(amount)

        # Merge same stats
        stats.sort(key=operator.itemgetter("id"))
        statsOutput = []
        for k, grp in itertools.groupby(stats, lambda item: item["id"]):
            grp = list(grp)
            if len (grp) > 1:
                d = {"id":0, "name":"", "amount":0, "alloc":0}
                for items in grp :
                    d["id"] = items["id"]
                    d["name"] = items["name"]
                    d["amount"] += items["amount"]
                    d["alloc"] += items["alloc"]
                statsOutput.append(d)
            else :
                statsOutput.append(grp[0])
        # Reorder
        output = [x for x in statsOutput if x["id"] in CHR_PRIMARY_STATS]
        output+= [x for x in statsOutput if x["id"] == 7 ]
        output+= [x for x in statsOutput if x["id"] not in CHR_PRIMARY_STATS+[7] ]           
        return output

class ItemAppearance (AbstractModel):
    TABLE = {"table":"ItemAppearance", "id_field":"id"}
    def __init__ (self, id, **kwargs):
        super (ItemAppearance, self).__init__(id, **kwargs)
    def getIcon (self, size, **kwargs):
        uiData = ManifestInterfaceData(self.defaultIconFileDataID) 
        return uiData.getIcon(size, **kwargs)

class ItemModifiedAppearance (AbstractModel):
    TABLE = {"table":"ItemModifiedAppearance", "id_field":"id", "id_parent_field":"id_parent"}
    def __init__ (self, id, **kwargs):
        super (ItemModifiedAppearance, self).__init__(id, **kwargs)
    
    def getIcon (self, size, **kwargs) :
        itemAppeareance = ItemAppearance(self.itemAppearanceID)
        return itemAppeareance.getIcon(size, **kwargs)

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

class ItemArmorTotal (AbstractModel):
    TABLE = {"table":"ItemArmorTotal", "id_field":"id"}
    def __init__ (self, id, **kwargs):
        super (ItemArmorTotal, self).__init__(id, **kwargs)

class ItemArmorShield (AbstractModel):
    TABLE = {"table":"ItemArmorShield", "id_field":"id"}
    def __init__ (self, id, **kwargs):
        super (ItemArmorShield, self).__init__(id, **kwargs)

class ItemDamageOneHand (AbstractModel):
    TABLE = {"table":"ItemDamageOneHand", "id_field":"id"}
    def __init__ (self, id, **kwargs):
        super (ItemDamageOneHand, self).__init__(id, **kwargs)

class ItemDamageOneHandCaster (AbstractModel):
    TABLE = {"table":"ItemDamageOneHandCaster", "id_field":"id"}
    def __init__ (self, id, **kwargs):
        super (ItemDamageOneHandCaster, self).__init__(id, **kwargs)

class ItemDamageTwoHand (AbstractModel):
    TABLE = {"table":"ItemDamageTwoHand", "id_field":"id"}
    def __init__ (self, id, **kwargs):
        super (ItemDamageTwoHand, self).__init__(id, **kwargs)

class ItemDamageTwoHandCaster (AbstractModel):
    TABLE = {"table":"ItemDamageTwoHandCaster", "id_field":"id"}
    def __init__ (self, id, **kwargs):
        super (ItemDamageTwoHandCaster, self).__init__(id, **kwargs)

class ArmorLocation (AbstractModel):
    TABLE = {"table":"ArmorLocation", "id_field":"id"}
    def __init__ (self, id, **kwargs):
        super (ArmorLocation, self).__init__(id, **kwargs)

class ItemArmorQuality (AbstractModel):
    TABLE = {"table":"ItemArmorQuality", "id_field":"id"}
    def __init__ (self, id, **kwargs):
        super (ItemArmorQuality, self).__init__(id, **kwargs)

class GemProperties (AbstractModel):
    TABLE = {"table":"GemProperties", "id_field":"id"}
    def __init__ (self, id, **kwargs):
        super (GemProperties, self).__init__(id, **kwargs)

preload = (
    ArmorLocation,
    # ItemClass,
    ItemSubClass, 
    ItemNameDescription,
    ItemBonus,
    # ItemBonusListLevelDelta,
    ItemArmorTotal,
    ItemArmorShield,
    ItemDamageOneHand, 
    ItemDamageOneHandCaster,
    ItemDamageTwoHand,
    ItemDamageTwoHandCaster,
) 
for tbl in preload:
    tbl.All() 