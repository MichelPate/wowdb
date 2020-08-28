from .abstract import AbstractModel
from .gametable import CombatRatingsMultByILvl
from .gametable import SpellScaling as TableSpellScaling
from .misc import PowerType, Difficulty, ManifestInterfaceData, RandPropPoints
from .character import ChrSpecialization, ChrClasses
from .creature import CreatureType
from ..manager import DB
from ..units import ChrUnitBasePoint, ChrUnitSpellPower, ChrUnitAttackPower
from ..utilities import chunks, FormatOutput, formatTime, formatDistance, formatAngle, arrayFromB32, intFloat, s 
from ..parsers import SpellDescriptionParser
from ..constants import SCHOOL_MASKS, SPELLS_FLAGS, SUBEFFECT_TYPES, EFFECT_TYPES, SUBEFFECT_TYPES, EFFECT_MISC_TYPES, ITEM_DEFAULT_ILVL, SPELL_TARGETS

SPELL_CLASS_MASKS_ALL = {i:list(set([x["SpellClassMask_{}".format(i)] for x in DB["SpellClassOptions"].find({"SpellClassMask_{}".format(i):{'$gt': 0}})])) for i in range (1,5)}

class SpellXDescriptionVariables (AbstractModel):
    TABLE = {"table":"SpellXDescriptionVariables", "id_field":"id"}
    def __init__ (self, id, **kwargs):
        super (SpellXDescriptionVariables, self).__init__(id, **kwargs)

class SpellDescriptionVariables (AbstractModel):
    TABLE = {"table":"SpellDescriptionVariables", "id_field":"id"}
    def __init__ (self, id, **kwargs):
        super (SpellDescriptionVariables, self).__init__(id, **kwargs)

class SpellRange (AbstractModel):
    TABLE = {"table":"SpellRange", "id_field":"id"}
    def __init__ (self, id, **kwargs):
        super (SpellRange, self).__init__(id, **kwargs)

class SpellRadius (AbstractModel):
    TABLE = {"table":"SpellRadius", "id_field":"id"}
    def __init__ (self, id, **kwargs):
        super (SpellRadius, self).__init__(id, **kwargs)

class SpellProcsPerMinute (AbstractModel):
    TABLE = {"table":"SpellProcsPerMinute", "id_field":"id"}
    def __init__ (self, id, **kwargs):
        super (SpellProcsPerMinute, self).__init__(id, **kwargs)

class SpellMechanic (AbstractModel):
    TABLE = {"table":"SpellMechanic", "id_field":"id"}
    def __init__ (self, id, **kwargs):
        super (SpellMechanic, self).__init__(id, **kwargs)

class SpellDuration (AbstractModel):
    TABLE = {"table":"SpellDuration", "id_field":"id"}
    def __init__ (self, id, **kwargs):
        super (SpellDuration, self).__init__(id, **kwargs)

class SpellDispelType (AbstractModel):
    TABLE = {"table":"SpellDispelType", "id_field":"id"}
    def __init__ (self, id, **kwargs):
        super (SpellDispelType, self).__init__(id, **kwargs)

class SpellCastTimes (AbstractModel):
    TABLE = {"table":"SpellCastTimes", "id_field":"id"}
    def __init__ (self, id, **kwargs):
        super (SpellCastTimes, self).__init__(id, **kwargs)

class SpellScaling (AbstractModel):
    TABLE = {"table":"SpellScaling", "id_field":"id"}
    def __init__ (self, id, **kwargs):
        super (SpellScaling, self).__init__(id, **kwargs)

class Talent (AbstractModel):
    TABLE = {"table":"Talent", "id_field":"id"}
    def __init__ (self, id, **kwargs):
        super (Talent, self).__init__(id, **kwargs)
    
    def getSpell (self):
        spell = Spell (self.spellID)
        if spell.exists : 
            return spell
    
    def getChrSpecs (self):
        return next(iter(ChrSpecialization.FindReference({"id":self.specID, "classID":self.classID})),None)

    @classmethod
    def getTree (cls, specId):
        spec = ChrSpecialization(specId)
        talents = []
        for row in range(7):
            for col in range (3):
                talent = next(iter(cls.FindReference({"specID":specId, "tierID":row, "columnIndex":col})), False)
                if not talent:
                    talent = next(iter(cls.FindReference({"classID":spec.classID, "specID":0, "tierID":row, "columnIndex":col})), False)
                talents.append(talent.spellID)
        talents = chunks(loadManySpells(talents), 3)
        return talents

class SpellMisc (AbstractModel):
    TABLE = {"table":"SpellMisc", "id_field":"id", "id_parent_field":"id_parent"}
    def __init__ (self, id, **kwargs):
        super (SpellMisc, self).__init__(id, **kwargs)
    
    def getIcon (self, size=35,**kwargs):
        iconId = self.spellIconFileDataID or self.activeIconFileDataID or 134400 #activeIconFileDataID
        uiData = ManifestInterfaceData(iconId)
        return uiData.getIcon(size, **kwargs)
    
    @FormatOutput(formatTime)
    def getCastTime (self):
        data = SpellCastTimes(self.castingTimeIndex)
        if data:
            return data.base
        return None

    @FormatOutput(formatTime)
    def getDuration (self):
        data = SpellDuration[self.durationIndex]
        if data :
            return data.duration
        return None
    
    @FormatOutput(formatDistance)
    def getRange (self):
        data = SpellRange[self.rangeIndex]
        if data :
            return int(data.rangeMax[1])

    def getRangeName (self):
        data = SpellRange[self.rangeIndex]
        if data :
            return data.displayNameShort

    def getSchoolType (self):
        data = SCHOOL_MASKS.get(self.schoolMask, False)
        if data :
            return data
        return None
    
    def getDifficulty (self):
        data = Difficulty[self.difficultyID]
        if data :
            return data
        return None

    def isPassive (self):
        flags = self.getFlags()
        return any(x for x in flags if "passive" in x.lower())

    def getFlags (self, verbose=True):
        enableIndices = []
        for idx, n in self.attributes.items():
            b32 = '{:032b}'.format(n)
            enableIndices += [((idx-1)*32)+int(i) for i,v in enumerate(reversed(b32)) if v == "1"]
        if verbose: 
            return [SPELLS_FLAGS[x] for x in enableIndices if x in SPELLS_FLAGS]
        return enableIndices

class SpellCategory (AbstractModel):
    TABLE = {"table":"SpellCategory", "id_field":"id"}
    def __init__ (self, id, **kwargs):
        super (SpellCategory, self).__init__(id, **kwargs)
    
    def getMaxCharges (self):
        return self.maxCharges
    
    @FormatOutput(formatTime)
    def getChargeRecoveryTime (self, *args, **kwargs):
        return self.chargeRecoveryTime

class SpellCategories (AbstractModel):
    TABLE = {"table":"SpellCategories", "id_field":"id", "id_parent_field":"id_parent"}
    def __init__ (self, id, **kwargs):
        super (SpellCategories, self).__init__(id, **kwargs)
    
    def getDispelType (self, null=None):
        data = SpellDispelType[self.dispelType]
        if data:
            return data.name
        return null

    def getMechanic (self, null=None):
        data = SpellMechanic[self.mechanic]
        if data : 
            return data.stateName.title()
        return null

    def getCategory (self):
        if self.chargeCategory != 0:
            return SpellCategory(self.chargeCategory)
        return None
    
    def getMaxCharges(self, null=None):
        category = self.getCategory()
        if category : 
            return category.getMaxCharges()
        return null
    
    def getChargeRecoveryTime(self, *args, **kwargs):
        category = self.getCategory()
        if category : 
            return category.getChargeRecoveryTime(*args, **kwargs)

class SpellTargetRestrictions (AbstractModel):
    TABLE = {"table":"SpellTargetRestrictions", "id_field":"id", "id_parent_field":"id_parent"}
    def __init__ (self, id, **kwargs):
        super (SpellTargetRestrictions, self).__init__(id, **kwargs)
    
    @FormatOutput(formatAngle)
    def getConeDegrees (self):
        return self.coneDegrees

    def getTargetCreatureType(self):
        creatureType = CreatureType[self.targetCreatureType]
        return creatureType
        
    def getMaxTargets (self):
        if self.maxTargets > 0 :
            return self.maxTargets

class SpellAuraOptions (AbstractModel):
    TABLE = {"table":"SpellAuraOptions", "id_field":"id", "id_parent_field":"id_parent"}
    def __init__ (self, id, **kwargs):
        super (SpellAuraOptions, self).__init__(id, **kwargs)
    
    def getProcsPerMinute (self):
        return SpellProcsPerMinute[self.spellProcsPerMinuteID]

    def getBaseProcRate (self):
        proc = self.getProcsPerMinute()
        if proc :
            return proc.baseProcRate

class SpellClassOptions (AbstractModel):
    TABLE = {"table":"SpellClassOptions", "id_field":"SpellID"}
    def __init__ (self, id, **kwargs):
        super (SpellClassOptions, self).__init__(id, **kwargs)
    
    def getChrClass (self):
        if self.spellClassSet != 0:
            chrCls = next(iter(ChrClasses.FindReference({"spellClassSet":self.spellClassSet})), False)
            if chrCls and chrCls.exists():
                return chrCls
    
    def getChrClassName (self):
        chrClass = self.getChrClass()
        if chrClass :
            return chrClass.name

class SpecializationSpells (AbstractModel):
    TABLE = {"table":"SpecializationSpells", "id_field":"id", "id_parent_field":"id_parent"}
    def __init__ (self, id, **kwargs):
        super (SpecializationSpells, self).__init__(id, **kwargs)
    
    def getChrSpecs (self):
        return ChrSpecialization[self.idParent]

    def getChrSpecsName (self):
        spec = self.getChrSpecs()
        if spec :
            return spec.name
    
    def getSpell (self):
        return Spell(self.spellID)

    @classmethod
    def fromSpec(cls, spec):
        return cls.FromParent(spec.id, parent=spec)

class SpellLevel (AbstractModel):
    TABLE = {"table":"SpellLevel", "id_field":"id"}
    def __init__ (self, id, **kwargs):
        super (SpellLevel, self).__init__(id, **kwargs)

class SpellCooldowns (AbstractModel):
    TABLE = {"table":"SpellCooldowns", "id_field":"id", "id_parent_field":"id_parent"}
    def __init__ (self, id, **kwargs):
        super (SpellCooldowns, self).__init__(id, **kwargs)

    @FormatOutput(formatTime)
    def getText (self):
        return self.recoveryTime or self.categoryRecoveryTime 
    
    @FormatOutput(formatTime)
    def getGCD(self):
        return self.startRecoveryTime
    
    # WIP, must find rule 
    def getGCDCategory(self): 
        gcd = self.getGCD(formatType=None)
        if gcd in [1000,1500] :
            return "Global"
        return "Special Category"

class SpellPower (AbstractModel):
    TABLE = {"table":"SpellPower", "id_field":"id", "id_parent_field":"id_parent"}
    def __init__ (self, id, **kwargs):
        super (SpellPower, self).__init__(id, **kwargs)
    
    def getText (self):
        powerTypeName = ""
        if self.powerType > 0 :
            powerType = PowerType[self.powerType]
            powerTypeName = powerType.nameGlobalStringTag.replace("_", " ")
        if self.powerCostPct :
            return "{}% of base {}".format(round(self.powerCostPct,4), powerTypeName.lower() or "mana")
        elif self.manaCost:
            maxCost = ""
            if self.optionalCost != 0:
                maxCost = " to {}".format(self.optionalCost + self.manaCost)
            return "{cost}{maxCost} {powerType}".format(cost=self.manaCost,maxCost = maxCost, powerType=powerTypeName.title())
        return powerTypeName

class SpellInterrupts (AbstractModel):
    TABLE = {"table":"SpellInterrupts", "id_field":"id", "id_parent_field":"id_parent"}
    def __init__ (self, id, **kwargs):
        super (SpellInterrupts, self).__init__(id, **kwargs)
    
    def getInterruptFlags (self):
        return arrayFromB32(self.interruptFlags)
    
    def getChannelInterruptFlags(self):
        enableIndices = []
        for idx, n in self.channelInterruptFlags.items():
            b32 = '{:032b}'.format(n)
            enableIndices += [((idx-1)*32)+int(i) for i,v in enumerate(reversed(b32)) if v == "1"]
       
        return enableIndices

class SpellLevels (AbstractModel):
    TABLE = {"table":"SpellLevels", "id_field":"id", "id_parent_field":"id_parent"}
    def __init__ (self, id, **kwargs):
        super (SpellLevels, self).__init__(id, **kwargs)

class SpellEffect (AbstractModel):
    TABLE = {"table":"SpellEffect", "id_field":"id", "id_parent_field":"id_parent"}
    def __init__ (self, id, **kwargs):
        super (SpellEffect, self).__init__(id, **kwargs)
    
    def getType (self):
        return EFFECT_TYPES.get(self.effect, "Unk #{}".format(self.effect))

    def getImplicitTargets (self):
        if self.implicitTarget[1] or self.implicitTarget[2] :  
            return (SPELL_TARGETS[self.implicitTarget[1]], SPELL_TARGETS[self.implicitTarget[2]])

    def getSubType (self):
        subEffectName = SUBEFFECT_TYPES.get(self.effectAura, "Unk #{}".format(self.effectAura))
        effectMiscDict = EFFECT_MISC_TYPES.get(self.effectAura, False)
        if effectMiscDict:
            effectMisc = effectMiscDict.get(self.effectMiscValue[1], False)
            if effectMisc:
                miscText = effectMisc
            else :
                miscText = effectMiscDict.get(1, "")
            subEffectName = miscText
        return subEffectName

    def getItem (self):
        if self.effectItemType:
            from .item import Item
            return Item (self.effectItemType)
            
    def getMechanic (self, null=None):
        mechanic = SpellMechanic[self.effectMechanic]
        if mechanic : 
            return mechanic.stateName.title()
        return null
    
    def getValue (self, roundValue=2):
        v = self.effectBasePointsF
        return intFloat(round(v,roundValue))

    def getSPModifier (self, roundValue=6):
        return round(self.effectBonusCoefficient,roundValue)

    def getAPModifier (self, roundValue=6):
        return round(self.bonusCoefficientFromAP,roundValue) 

    @FormatOutput(formatTime)
    def getInterval (self):
        return self.effectAuraPeriod
    
    @FormatOutput(formatDistance)
    def getRadius (self):
        radiusIndices = [self.effectRadiusIndex.get(i) for i in (1,2)]
        radiusObjects = [SpellRadius[x] for x in radiusIndices]
        radiusRange = [x.radius if x else 0 for x in radiusObjects ]
        maxRadius = max(radiusRange)
        return maxRadius

    def getRelatedValue (self):
        flags = self.parent.getFlags(verbose=False)

        # REMOVE THIS ASAP, Make it in a condition when everything else not working
        from .item import ItemEffect
        itemFx = next(iter(ItemEffect.Find({"SpellID":self.parent.id})), None)

        # Scale with ilevel
        if 354 in flags :        
            ilvl = self.parent.ilevel
            propPoints = RandPropPoints[ilvl]
            crMult = CombatRatingsMultByILvl[ilvl]
            scaling = self.parent.getScaling()
            scalingClass = -1
            if scaling :
                scalingClass = getattr(scaling, "class")
            if self.effectAura == 189:
                amount = self.coefficient * propPoints.epic[1] * crMult.armorMultiplier
            elif scalingClass  == -8 :
                amount = self.coefficient * propPoints.damageReplaceStat    
            elif scalingClass == -9 :
                amount = self.coefficient * propPoints.damageSecondary
            else :
                amount = self.coefficient * propPoints.epic[1]
            return (int(round (amount)), int)

        elif itemFx and itemFx.triggerType == 7 and 379 in flags and self.effectAura == 189: # SpellScaling by Item
            tableSpellScaling = TableSpellScaling(60)
            amount = self.coefficient * tableSpellScaling.item
            return (int(round (amount)), int)
        else:
            mapCls = {"effectBasePointsF":ChrUnitBasePoint, "bonusCoefficientFromAP":ChrUnitAttackPower, "effectBonusCoefficient":ChrUnitSpellPower}
            relatedValues = {k:getattr(self, k) for k in mapCls.keys() }
            filteredDict = dict(filter(lambda x:x[1], relatedValues.items()))
            filteredValues = filteredDict.items()
            if filteredValues :
                currentValue = next(iter(filteredValues))
                k, v = currentValue
                return  (v, mapCls[k]())

    def getTriggerSpell (self, verbose=True, default=None):
        spellId = self.effectTriggerSpell
        if spellId != 0:
            spell = Spell(spellId)
            if spell.exists() and verbose:
                iconTxt = spell.getIcon(size=15, html=True)
                return "{icon}  {name} [{id}]".format(icon = iconTxt, name =spell.name, id=spell.id)
            else :
                return spell
        return default  
    
    def getTriggerItem (self):
        return self.effectItemType # Can be cast on cls Item when done

    def getAffectedSpells (self, default=None):
        query = []
        for i, mask in self.effectSpellClassMask.items():
            if mask!= 0 :
                current = arrayFromB32(mask)
                allPerm = SPELL_CLASS_MASKS_ALL[i]
                data = [x for x in allPerm if any(elem in arrayFromB32 (x) for elem in current)]
                if data :
                    query.append({"SpellClassMask_{}".format(i) : {"$in":data}})
        if query :
            f = { "$or": query}
            
            f.update({"SpellClassSet":self.parent.classOptions().spellClassSet})
            affectedIndices = [x["SpellID"] for x in DB["SpellClassOptions"].find(f)]
            return loadManySpells (affectedIndices)
        return default
    
    def getTooltipText(self):
        typ = self.getType()
        subType = self.getSubType()
        percent = next(iter(["%" for x in (typ, subType) if "%" in x or "percent" in x.lower()]), "")
        lines = ""
        lines += '<tr>'
        lines += '<td {style}>Effect #{idx}</td>'.format(idx=self.effectIndex+1, style= s(size=11, weight=700))
        lines += '<td {style}>{effect}</td>'.format(effect = "{type}{subtype}".format(type=typ, subtype=": {}".format(subType) if subType!="None" else ""), style= s(size=11))
        lines += '</tr>'
        for prop, title in {"getValue":"Value","getInterval":"Interval","getMechanic":"Mechanic", "getSPModifier":"SP mod", "getAPModifier":"AP mod", "getRadius":"Radius", "getTriggerSpell":""}.items():
            attr = getattr(self, prop)()
            currentPercent = percent if title == "Value" else ""
            if attr :
                lines += '<tr>'
                lines += '<td></td>'
                lines += '<td {style}>{title}{sep}{value}{percent}</td>'.format(title=title, sep=": " if title else "" , value = attr, percent=currentPercent, style= s(size=11))
                lines += '</tr>'
        affectedSpells = self.getAffectedSpells()
        if affectedSpells :
            spells = [spell.getShortText(iconSize=12) for spell in affectedSpells]
            lines += '<tr>'
            lines += '<td></td>'
            lines += '<td {style}>Affected Spells:</td>'.format(style= s(size=11) )
            lines += '</tr>'
            lines += '<tr>'
            lines += '<td></td>'
            lines += '<td {style}>{affectedSpells}</td>'.format(affectedSpells="<br>".join([", ".join(spells)]), style= s(size=9) ) #x) for x in chunks(spells, 5
            lines += '</tr>'
        return lines

class SpellName (AbstractModel):
    TABLE = {"table":"SpellName", "id_field":"id"}
    def __init__ (self, id, **kwargs):
        super (SpellName, self).__init__(id, **kwargs)
    
class Spell (AbstractModel):
    TABLE = {"table":"Spell", "id_field":"id"}
    def __init__ (self, id, **kwargs):
        super (Spell, self).__init__(id, **kwargs)
        self.currentDifficulty = None
        self.ilevel = kwargs.get("ilevel", ITEM_DEFAULT_ILVL)
        
    @property
    def name (self):
        return SpellName(self.id).name
    
    def setItemLevel (self, ilvl):
        self.ilevel = ilvl

    def miscs(self):
        return SpellMisc.FromParent(self.id, parent=self)

    def effects(self):
        return SpellEffect.FromParent(self.id, parent=self, sort_field="effectIndex")

    def powers(self):
        return SpellPower.FromParent(self.id, parent=self)

    def cooldowns (self):
        return SpellCooldowns.FromParent(self.id, parent=self)

    def categories(self):
        return SpellCategories.FromParent(self.id, parent=self)
    
    def interrupts(self):
        return SpellInterrupts.FromParent(self.id, parent=self)
    
    def levels(self):
        return SpellLevels.FromParent(self.id, parent=self)

    def targetRestrictions(self):
        return SpellTargetRestrictions.FromParent(self.id, parent=self)
    
    def auraOptions (self):
        return SpellAuraOptions.FromParent(self.id, parent=self)
    
    def specialization (self):
        spec = SpecializationSpells.Many([self.id], field="SpellID")
        if spec :
            return spec
    
    def getScaling (self):
        return next(iter(SpellScaling.Find({"SpellID":self.id})), None)

    def getTalent (self):
        return next(iter(Talent.FindReference({"spellID":self.id})),False)

    def getChrSpecs (self):
        spec = self.specialization()
        if spec :
            return [x.getChrSpecs() for x in spec]
        else :
            talent = self.getTalent()
            if talent :
                specs = talent.getChrSpecs()
                if specs :
                    return [specs]
        return []
    
    def getChrSpecsName (self):
        spec = self.getChrSpecs()
        if spec :
            return [x.name for x in spec]
        return []

    def classOptions(self):
        classOptions = SpellClassOptions(self.id)
        if classOptions.exists() :
            return classOptions

    def level(self):
        return SpellLevel(self.id)
    
    def getCurrentMisc (self):
        miscs = self.miscs()
        if miscs :
            return next(iter([x for x in miscs if x.difficultyID == self.getCurrentDifficulty()]), miscs[0])
    
    def getCurrentLevels (self):
        levels = self.levels()
        if levels :
            return next(iter([x for x in levels if x.difficultyID == self.getCurrentDifficulty()]), None)
        
    def getCurrentCategories (self):
        categories = self.categories()
        if categories :
            return next(iter([x for x in categories if x.difficultyID == self.getCurrentDifficulty()]), None)
    
    def getCurrentInterrupts (self):
        interrupts = self.interrupts()
        if interrupts :
            return next(iter([x for x in interrupts if x.difficultyID == self.getCurrentDifficulty()]), None)
    
    
    def getCurrentTargetRestrictions (self):
        targetRestrictions = self.targetRestrictions()
        if targetRestrictions :
            return next(iter([x for x in targetRestrictions if x.difficultyID == self.getCurrentDifficulty()]), None)

    def getCurrentCooldown (self):
        cooldowns = self.cooldowns()
        if cooldowns :
            return next(iter([x for x in cooldowns if x.difficultyID == self.getCurrentDifficulty()]), None)

    def getCurrentAuraOptions (self):
        auraOptions = self.auraOptions()
        if auraOptions :
            return next(iter([x for x in auraOptions if x.difficultyID == self.getCurrentDifficulty()]), None) 

    def getCurrentEffects (self):
        effects = self.effects()
        if effects :
            return [x for x in effects if x.exists() and x.difficultyID == self.getCurrentDifficulty()]
        return []

    def getDescriptionVariables (self):
        descriptionVar = SpellXDescriptionVariablesTbl.get(self.id, False)
        if descriptionVar:
            descVarId = descriptionVar.spellDescriptionVariablesID
            return SpellDescriptionVariables[descVarId]

    def getCurrentLevel (self):
        level = self.getCurrentLevels()
        if level :
            return level.spellLevel

    def setCurrentDifficulty (self, idx):
        self.currentDifficulty = idx
    
    def getCurrentDifficulty (self):
        return self.currentDifficulty or 0

    def getDifficulty (self, *args, **kwargs):
        return self.getCurrentMisc().getDifficulty(*args, **kwargs)

    def getIcon (self, *args, **kwargs):
        misc = self.getCurrentMisc()
        if misc :
            return misc.getIcon(*args, **kwargs)
    
    def getDuration (self, *args, **kwargs):
        return self.getCurrentMisc().getDuration(*args, **kwargs)

    def getRange (self, *args, **kwargs):
        return self.getCurrentMisc().getRange(*args, **kwargs)
    
    def getRangeName (self, *args, **kwargs):
        return self.getCurrentMisc().getRangeName(*args, **kwargs)
    
    def getSchoolType (self, *args, **kwargs):
        return self.getCurrentMisc().getSchoolType(*args, **kwargs)

    def getCastTime (self, *args, **kwargs):
        return self.getCurrentMisc().getCastTime(*args, **kwargs)
    
    def getFlags (self, *args, **kwargs):
        misc = self.getCurrentMisc()
        if misc :
            return misc.getFlags(*args, **kwargs)
        return []

    def getMaxCharges(self, null=None):
        current = self.getCurrentCategories()
        if current : 
            return current.getMaxCharges()
        return null
    
    def getChargeRecoveryTime(self, *args, **kwargs):
        current = self.getCurrentCategories()
        if current : 
            return current.getChargeRecoveryTime(*args, **kwargs)

    def getChrClass (self):
        classOptions = self.classOptions ()
        if classOptions:
            return classOptions.getChrClass()

    def getChrClassName (self):
        classOptions = self.classOptions ()
        if classOptions:
            return classOptions.getChrClassName()

    def getDispelType (self, *args, **kwargs):
        current = self.getCurrentCategories()
        if current :
            return current.getDispelType(*args, **kwargs)

    def getMechanic (self, *args, **kwargs):
        current = self.getCurrentCategories()
        if current :
            return current.getMechanic(*args, **kwargs)

    def getCooldown (self, *args, **kwargs):
        current = self.getCurrentCooldown()
        if current :
            return current.getText(*args, **kwargs)
    
    def getGCD (self, *args, **kwargs):
        current = self.getCurrentCooldown()
        if current :
            return current.getGCD(*args, **kwargs)
    
    def getGCDCategory(self, *args, **kwargs):
        current = self.getCurrentCooldown()
        if current :
            return current.getGCDCategory(*args, **kwargs)
    
    def getConeDegrees (self, *args, **kwargs):
        current = self.getCurrentTargetRestrictions()
        if current :
            return current.getConeDegrees(*args, **kwargs)
    
    def getMaxTargets (self, *args, **kwargs):
        current = self.getCurrentTargetRestrictions()
        if current :
            return current.getMaxTargets(*args, **kwargs)
        
    def getPowers (self, *args, **kwargs):
        powers = self.powers()
        if powers :
            return [power.getText(*args, **kwargs) for power in powers]
        return []

    def getDescription (self, text=None):
        desc = text or self.description
        d = SpellDescriptionParser(desc, parent=self, ilevel=self.ilevel)
        return d.getComputed()
    
    def getAuraDescription (self):
        desc = self.auraDescription
        if desc:
            return self.getDescription (desc)
        return None
    
    def isPassive (self):
        return self.getCurrentMisc().isPassive()

    def getDescriptionSpells (self):
        d = SpellDescriptionParser(self.description, parent=self, ilevel=self.ilevel)
        return d.getRelatedSpells()

    def getShortText (self, iconSize = 15):
        return '<span style="text-align: right;">{icon}</span> {name}'.format(icon=self.getIcon(size=iconSize, html=True), name=self.name)

    def getTooltipText(self, displayLevel=1):
        flags = self.getFlags(verbose=False)
        lines = ""
        
        # Header
        lines += '<table width="100%">'
        lines += '<tr>'
        lines += '<td {style}>{name}</td>'.format(name=self.name, style = s(size=14, weight=700))
        lines += '<td style="text-align: right;">{icon}</td>'.format(icon=self.getIcon(size=35, html=True))
        lines += '</tr>'
        if 354 in flags :
            lines += '<tr>'
            lines += '<td {style}>Item Level {ilvl}</td>'.format(ilvl = self.ilevel , style=s(size=12) )
            lines += '</tr>'
        lines += '</table>'
        
        # Summary
        specs = self.getChrSpecsName ()
        summaryItems = [
            ("{value}",[self.nameSubtext]),
            ("<span style=\"color:#9d9d9d\">Talent</span>", [self.getTalent()]),
            ("{value}",[" / ".join(self.getPowers())]),  
            ("{value}",[self.getCastTime(formatType="short", zero="Instant")]), 
            ("{value} cooldown",[self.getCooldown(formatType="short")]), 
            ("{value} range",[self.getRange(formatType="short")]), 
            ("{value} recharge",[self.getChargeRecoveryTime(formatType="short")]), 
            ("{value} Charges",[self.getMaxCharges()]),
            ("Requires {value}",[self.getChrClassName(), ", ".join(specs)]), 
            ("Requires level {value}",[self.getCurrentLevel()]), 
        ]
        
        lines += '<table width="100%">'
        for item in summaryItems:
            k, v = item
            v = list(filter(None, v))
            if v :
                lines += '<tr>'
                lines += '<td {style}>{}</td>'.format(k.format(value=" ".join(map(str, v))) , style=s(size=12) )
                lines += '</tr>'
        lines += '</table>'

        # Description
        lines += '<p {style}>{description}</p>'.format(description=self.getDescription(), style = s(size=11, color=(255,209,0)))
        
        auraDesc = self.getAuraDescription()
        if auraDesc:
            
            lines += '<p {style}>Buff</p>'.format(style = s(size=12, weight=700))
            lines += '<table style="background-color:rgba(255,255,255,25);">'
            lines += '<tr><td {style}>{name}</td></tr>'.format(name=self.name, style = s(size=11, color=(255,209,0),weight=700))
            lines += '<tr><td {style}>{description}</td></tr>'.format(description=auraDesc, style = s(size=11))
            auraDuration = self.getDuration(formatType="long")
            if auraDuration:
                lines += '<tr><td {style}>{duration}</td></tr>'.format(duration = "{} remaining".format(auraDuration), style= s(size=11,  color=(255,209,0)))
            lines += '</table>'

        if displayLevel > 1 :
            # Details
            lines += '<p {style}>Spell Details</p>'.format(style = s(size=12, weight=700))
            lines += '<table width="100%">'
            lines += '<tr>'
            lines += '<td {style}>{cost}</td>'.format(cost = "Cost: {}".format( " / ".join(self.getPowers()) or None ), style= s(size=11))
            lines += '<td {style}>{duration}</td>'.format(duration = "Duration: {}".format(self.getDuration(formatType="long", null="n/a")), style= s(size=11))
            lines += '</tr>'
            lines += '<tr>'
            lines += '<td {style}>{range}</td>'.format(range="Range: {} ({})".format(self.getRange(), self.getRangeName()), style= s(size=11))
            lines += '<td {style}>{schoolType}</td>'.format(schoolType = "Type: {}".format(self.getSchoolType()), style= s(size=11))
            lines += '</tr>'
            lines += '<tr>'
            lines += '<td {style}>{castime}</td>'.format(castime = "Cast time: {}".format(self.getCastTime(null="n/a", zero="Instant") ), style= s(size=11))
            lines += '<td {style}>{mechanic}</td>'.format(mechanic = "Mechanic: {}".format(self.getMechanic(null="n/a")), style= s(size=11))
            lines += '</tr>'
            lines += '<tr>'
            lines += '<td {style}>{cooldown}</td>'.format(cooldown="Cooldown: {}".format(self.getCooldown(formatType="long", null="n/a")), style= s(size=11))
            lines += '<td {style}>{dispelType}</td>'.format(dispelType = "Dispel type: {}".format(self.getDispelType(null="n/a")), style= s(size=11))
            lines += '</tr>'
            lines += '<tr>'
            lines += '<td {style}>{gcd}</td>'.format(gcd = "GCD: {}".format(self.getGCD(formatType="long")), style= s(size=11))
            lines += '<td {style}>GCD category: {GCDCat}</td>'.format(GCDCat=self.getGCDCategory(), style= s(size=11)) #Don't know where to find this ? if 0 : n/a, 1.5 :normal ?
            lines += '</tr>'
            lines += '</table>'

            # Target Restrictions
            targetRestrictions = self.getCurrentTargetRestrictions()
            if targetRestrictions :
                tr = {"Max Targets":targetRestrictions.getMaxTargets(), "Creature Type":targetRestrictions.getTargetCreatureType(), "Cone":targetRestrictions.getConeDegrees()}
                lines += '<p {style}>Target Restrictions</p>'.format(style = s(size=12, weight=700))
                lines += '<table width="100%">'
                for k, v in tr.items():
                    if v :
                        lines += '<td {style}>{value}</td>'.format(value="{}: {}".format(k, v), style= s(size=11))
                lines += '</table>'
                # print (targetRestrictions.getMaxTargets(), targetRestrictions.getTargetCreatureType(), targetRestrictions.getConeDegrees())
            
            # Aura Options
            auraOptions = self.getCurrentAuraOptions()
            if auraOptions:
                pass

            # Effects
            lines += '<br>'
            lines += '<table width="100%">'
            for fx in self.getCurrentEffects():
                lines += fx.getTooltipText()
            lines += '</table>'

            # Flags
            lines += '<p {style}>Flags</p>'.format(style = s(size=12, weight=700))
            lines += '<ul style="list-style: none;">'
            for flag in self.getFlags():
                lines += "<li {style}>&bull; {flag}</li>".format(flag=flag, style= s(size=11))
            lines += '</ul>'

        #ID 
        lines += '<br>'
        lines += '<p {style}>ID: {}</p>'.format(self.id, style= s(size=11))
        return lines

def loadManySpells (indices):
    spells = Spell.Many(indices)
    SpellName.Many(indices)
    miscs = SpellMisc.Many(indices, field="id_parent")
    ManifestInterfaceData.Many([x.spellIconFileDataID for x in miscs])
    return spells

preload = (
    CreatureType,
    Difficulty, 
    Talent,
    PowerType, 
    SpellDuration, 
    SpellRadius, 
    SpellProcsPerMinute, 
    SpellRadius,
    SpellRange,
    SpellDescriptionVariables, 
    SpellXDescriptionVariables
) 
for tbl in preload:
    tbl.All()
SpellXDescriptionVariablesTbl = {x.spellID:x for x in SpellXDescriptionVariables._REFERENCES.values()}