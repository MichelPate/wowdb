from .utilities import iconBase64Html, intFloat
from pyparsing import SkipTo, Suppress, Combine, Optional, OneOrMore, ZeroOrMore, Group, LineEnd, Word,Literal, tokenMap, alphas, alphanums, hexnums, nums, printables
from sympy import simplify, Symbol, Min, Max, Number, Expr, Gt, Ge, Lt, Le
import hashlib
import operator 
import functools
from .models.character import ChrSpecialization
from .models.gametable import SpellScaling
from .models.misc import Difficulty
from .units import ChrUnitBasePoint, ChrUnitSpellPower, ChrUnitAttackPower

def printM(expr, num_digits):
            return expr.xreplace({n.evalf() : round(n, num_digits) for n in expr.atoms(Number)})

class LuaParser (object):
    def __init__ (self, text, parent=None, **kwargs):
        self.setCurrent (text, parent=parent, **kwargs)
        self.formatType = kwargs.get("formatType", "html")

    def compute (self, text, verbose=True):
        vbar = Literal("|")
        eol = LineEnd().suppress()

        # Colors
        result = text
        endTag = ((vbar + (Literal("r")|Literal("R"))|eol))
        parser = (
            Suppress(vbar + (Literal("c")|Literal("C"))) + 
            Word(hexnums, exact=8).setResultsName("hex") + 
            SkipTo(endTag).setResultsName("content") + 
            Suppress(endTag)
        ).addParseAction(self.colorize)

        new_result = parser.transformString(result)
        result = parser.transformString(new_result)

        while(new_result != result):
            new_result = result
            result = parser.transformString(new_result)
        
        # Normalize line breakers
        result = result.replace ("|n", "\n")
        result = result.replace ("\n\n\n", "\n\n").strip("\n")

        if self.formatType == "html" and verbose:
            result = result.replace ("$bullet;", "&bull; ")
            result = result.replace("\r\n", "<br>").replace("\n", "<br>")

        return result

    def setCurrent (self, text, parent=None, **kwargs):
        self.text = text
        self.parent = parent

    def colorize (self, t):
        hexRGB = "".join(list(t.hex)[:6])
        return "<span style=\"color:#{};\">{}</span>".format(hexRGB, t.content)

    def getComputed (self):
        return self.compute(self.text)

class SpellDescriptionParser (LuaParser):
    OPS_MAPPING = {
                    "!=": operator.ne,
                    "==":operator.eq,
                    ">":operator.gt,
                    "<":operator.lt,
                    "+": operator.add,
                    "-": operator.sub,
                    "*": operator.mul,
                    "/": operator.truediv,
                    "&": operator.and_,
                    "|": operator.or_,
                    "!": operator.not_,
                }
    def __init__ (self, text, parent=None, **kwargs):
        super (SpellDescriptionParser, self).__init__(text, parent, **kwargs)
        self.ilevel = kwargs.get("ilevel", None)
        self.staticVariables = {
            'ap':"Attack Power",
            'pri':"Primary Stat",
            'agi':"Agility",
            'oap':"Off-Hand Attack Power", 
            'j1g':"J1G", # What's this ?
            'mhp':"Total health", 
            'mwb':"Main-Hand Damage", 
            'mws':"Main-Hand Speed", 
            'owb':"Off-Hand Damage", 
            'ows':"Off-Hand Speed", 
            'pl': "Player Level",
            'rap':"Ranged Attack Power", 
            'rws':"Raw W Spell", 
            'sp':"Spell Power", 
            'sph':"Spell Power",
            'spfr':"Spell Power Frost", 
            'sph':"Spell Power Holy", 
            'spn':"Spell Power Nature",
            'sps':"Spell Power Shadow", 
            'sta':"Stamina",
            "pcth":"Percent Health", 
            "pctd":"Percent D",
            "procrppm":"Proc RPPM",
            "versadmg":"Versatility",
            }

    def setCurrent (self, text, parent=None, **kwargs):
        super (SpellDescriptionParser, self).setCurrent(text, parent, **kwargs)
        self.descriptionVariables = None
        var = self.parent.getDescriptionVariables()
        if var:
            self.descriptionVariables = var.variables
        self.variables = {}
        self.descVariables = {}

    def getRelatedSpells(self):
        # Will return all the spellIds related in desc
        pass

    def clamp (self, x, minValue, maxValue):
        # Find a way to create a Sympy "clamp" function
        return  Max(Min(x, maxValue), minValue)

    def lt (self, a, b):
        return Lt(a, b)
    def lte (self, a, b):
        return Le(a, b)
    def gt (self, a, b):
        return Gt(a,b)
    def gte (self, a, b):
        return Ge(a, b)
    def min (self, a, b):
        return Min(a, b)
    def max (self, a, b):
        return Max(a, b)
    def abs (self, a):
        return abs(a)

    def compute (self, text, verbose=True):
        
        # Literals
        dollar = Literal('$')
        amper = Literal('&')
        at = Literal('@')
        qm = Literal('?')
        em = Literal('!')
        dot = Literal('.')
        colon = Literal(":")
        vbar = Literal("|")
        lbrack = Literal("[")
        rbrack = Literal("]")
        lcurly = Literal("{")
        rcurly = Literal("}")
        lparen = Literal("(")
        rparen = Literal(")")
        lt = Literal("<")
        gt = Literal(">")
        eq = Literal("=")
        deq = Literal("==")

        # Reusables
        spellId =  Word(nums, min=2, max=6).addParseAction(tokenMap(int)).setResultsName("spellId")
        idx = Word(nums, max=1).addParseAction(tokenMap(int)).setResultsName("id")
        var = Word(alphas).setResultsName("var")
        
        # Spell References
        effectId = Optional(Word(nums,max=2).addParseAction(tokenMap(int)).setResultsName("effectId"))
        references = (
            dollar.suppress() + 
            (
                (at.suppress()+ var + Optional(spellId)) |
                (spellId + var + effectId) | 
                (var + effectId)
            )
        ).addParseAction(self.setReferences)
        
        # Conditions
        brackets = Suppress(lbrack) + SkipTo(rbrack).setResultsName("statement")  + Suppress(rbrack)
        value = Word(nums,max=5).addParseAction(tokenMap(int)).setResultsName("value")
        conditionVar = Group(
                        Optional(em).setResultsName("not") +
                        Optional(var) + (spellId|idx)
                        |Optional("-") + value
                        |Word(alphanums, exact=8).setResultsName("hashVariable")
                    )
        conditions = (
            (dollar+qm).suppress() +
            OneOrMore(Group(
                Optional(Suppress(qm)) +
                Optional(Suppress(lparen))+
                OneOrMore (
                    conditionVar.setResultsName("variables*") +
                    Optional (Combine(em+eq)|amper|vbar|deq|lt|gt).setResultsName("operators*")

                ) +
                Optional(Suppress(rparen)) +
                brackets
            ).setResultsName("conditions*")) +
            brackets
        ).addParseAction(lambda t :self.setConditions(t, verbose=verbose)) + Optional(dot.suppress())

        # Call Variable 
        callVariables = (
            Suppress((lt+dollar)|(dollar+lt)) +
            SkipTo(gt).setResultsName("name") +
            Suppress(gt)
        ).addParseAction(self.callVariables)

        # Expressions
        expressions = (
            Suppress(dollar+lcurly) +
            SkipTo(rcurly).setResultsName("content") +
            rcurly +
            Optional (
                dot.suppress()+
                Word(nums, exact=1).addParseAction(tokenMap(int)).setResultsName("mod"),
            )
        ).addParseAction(lambda t :self.setExpressions(t, verbose=verbose)) 

        # Language Choices
        languageChoices = (
            (Literal('$L')|Literal('$l')).suppress() +
            OneOrMore(
                Word(alphas)+ 
                Optional (Literal(":").suppress())
            ).setResultsName("options*") + 
            Literal(';').suppress()

        ).addParseAction(self.setLanguageChoices) 

        # Icons
        icons = (
            Literal("|T").suppress() +
            SkipTo(colon).setResultsName("path") + 
            colon.suppress() + 
            Word(nums, exact=2).addParseAction(tokenMap(int)).setResultsName("size") + 
            Literal("|t").suppress()
        ).addParseAction(self.setIcons) 

        # Parsing layer by layer
        parsingOrder = [icons, languageChoices, callVariables, references, expressions, conditions ]
        steps = [text]
        for parser in parsingOrder :
            steps.append(parser.transformString(steps[-1]))
        result = steps[-1]
    
        # Replace each Sha1 Hash placeholder by refering value
        if verbose :
            for k, v in self.variables.items():
                result = result.replace(k, str(v))

        # Display fixes 
        displayFixes = [["*% of", "% of"], ["power)%", "power)"]]
        for bef, aft in displayFixes:
            result = result.replace(bef, aft)

        return super (SpellDescriptionParser, self).compute(result, verbose)
    
    def setIcons (self, t):
        if t.path:
            splitted = t.path.split("\\")
            tail = splitted[-1]
            filename = tail.replace(".blp", "")
            return iconBase64Html(filename, size=15, html=True)


    def setLanguageChoices (self, t):
        if t.options :
            return t.options[0][-1]

    def computeVariables (self, text):
        # Literals
        dollar = Literal('$')
        eq = Literal("=")
        eol = LineEnd().suppress()
        
        # Declare Variable 
        startVar = (
            dollar.suppress() +
            Word(alphanums).setResultsName("name") +
            eq.suppress()
        )
        declareVariables = (
            OneOrMore(Group(
            startVar+
            SkipTo(startVar|Literal("--")|eol).setResultsName("content")
            ).setResultsName("variables*"))
        )
        declareVariables.ignore(Literal("=="))
        token = declareVariables.searchString(text)
        for var in token :
            for name, content in var:
                self.descVariables[name]=self.compute(content, verbose=False)

    def getComputed (self):
        if self.descriptionVariables:
            self.computeVariables(self.descriptionVariables)
        return super (SpellDescriptionParser, self).getComputed()

    def colorLua(self, color, content):
        return "|c{}{}|r".format(color, content)

    def registerVariable (self, t):
        # SHA1 Hash, only 8char should be enough
        hashStr = hashlib.sha1(str(t).encode("UTF-8")).hexdigest()[:8]
        self.variables[hashStr] = t
        return hashStr

    def callVariables (self, t):
        if t.name :
            return "({})".format(self.descVariables.get(t.name, None))

    def setReferences (self, t):

        current = self.parent
        result = ""
        if t.spellId :
            spell = self.parent.__class__(t.spellId)
            spell.setItemLevel (self.ilevel)
            if spell.exists():
                current = spell

        if t.var :
            t.var = t.var.lower() 

            if t.var == "procrppm":
                auraOptions = self.parent.getCurrentAuraOptions()
                if auraOptions :
                    result = round(auraOptions.getBaseProcRate(),4)

            elif t.var in self.staticVariables:
                value = self.staticVariables.get(t.var, None)
                result = self.registerVariable(value)

            elif "spell" in t.var :
                if t.var == "spellname" :
                    result = self.colorLua("ffffffff", current.name)
                elif t.var == "spellicon":
                    result = current.getIcon (size=15, html=True)
                elif t.var == "spellaura":
                    result = current.getAuraDescription()
                elif t.var == "spelldesc":
                    result = current.getDescription()

            elif t.var in ["clamp", "min", "max", "lt", "lte", "gt", "gte", "abs"]:
                result = "self.{}".format(t.var)

            elif t.var in ["ec", "eci"]:
                if t.var == "ec":
                    from .models.spellItemEnchantment import SpellItemEnchantment
                    effects = current.getCurrentEffects()
                    if effects :
                        enchant = SpellItemEnchantment(effects[0].effectMiscValue[1])
                        spellScaling = SpellScaling[enchant.maxLevel]
                        scalingBase = spellScaling.getTypeValue(enchant.scalingClass)
                        v = scalingBase * enchant.effectScalingPoints[1]
                        result = int(round(v))
        
            elif t.var in ["u", "n", "h"]:
                auraOptions = current.getCurrentAuraOptions()
                if auraOptions:
                    if t.var =="u":
                        result = auraOptions.cumulativeAura
                    elif t.var =="n":
                        result = auraOptions.procCharges
                    elif t.var =="h":
                        result = auraOptions.procChance

            elif  t.var in ["b", "i", "c", "s", "m", "w", "sw", "o", "bc"] :        
                t.effectId = t.effectId or 1

                effects = current.effects()
                if len (effects) < t.effectId and effects :
                    effect = effects[-1]
                else :
                    effect = effects[t.effectId-1]

                if t.var == "b":
                    return intFloat(round(effect.effectPointsPerResource,4))

                elif t.var in ["s", "m", "w", "sw", "o", "bc"] :
                    value, unit = effect.getRelatedValue() or (0, int)
                    if isinstance(unit, (ChrUnitAttackPower, ChrUnitSpellPower)) :
                        value *= 100

                    if t.var == "o":
                        duration = current.getDuration(formatType=None)
                        intervals = effect.getInterval(formatType=None)
                        durationMod = (duration*0.001)
                        if intervals:
                            durationMod /= (intervals*0.001)
                        value*=durationMod 

                    value = intFloat(round(value,4))

                    if unit in (float, int) or isinstance(unit, ChrUnitBasePoint):
                        result = value
                    else :
                        var = self.registerVariable(unit)
                        if value:
                            result = "({}*{})".format(value, var)
                        else :
                            result = value

                elif t.var == "t":
                    # Not sure about this ? why 0.4 ? check spell 320639
                    result = effect.getInterval(formatType=None)*0.001 or 0.4 
                elif t.var == "x":
                    result = effect.effectChainTargets
                elif t.var == "a":
                    result = effect.getRadius(formatType=None)

            elif t.var == "d":
                duration = current.getDuration(formatType = "short")
                if duration :
                    result = duration

            elif t.var == "i":
                result = current.getMaxTargets()

            elif t.var == "c":
                powers = current.powers()
                powersCost = [x.powerCostPct for x in powers ]
                if powersCost:
                    result = powersCost[0]
            
        return str(result)

    def setExpressions(self, t, verbose=True):
        result = ""
        if t.content:
            # Modifier
            modifier = False
            if t.mod :
                contentVars = t.content
                for k,v in self.variables.items():
                    contentVars = contentVars.replace(k, str(v))
                if t.mod == 1:
                    modifier = 1 #did they change this from 10 to 1 ?
                if t.mod == 1 or t.mod == 2:
                    if "%" in contentVars :
                        if t.mod == 2:
                            # {}.x is equivalent to *0.08 apparently for % AP/SP
                            modifier = 0.08

            # Remove blacklist words from expression
            blacklist=[" sec", " secs"]
            for b in blacklist :
                t.content = t.content.replace(b, "")
            
            # Replace variables by Sympy Symbols
            for k in self.variables.keys():
                t.content = t.content.replace(k, "Symbol(\"{}\")".format(k))
            # print ("Before Eval:", t.content)
            try :
                result = eval("simplify(({}){})".format(t.content, "*{}".format(modifier) if modifier else ""))
            except :
                pass
            rounding = 4
            if isinstance (result, Expr) :
                if result.is_number:
                    result = round(float(result), rounding)
                else :
                    result = printM(result, rounding)
            # print ("After Eval:", result)
            if isinstance (result, (int, float)):
                result = str(intFloat(result))
            else :
                result = "({})".format(result)
        if not t.mod:
            result+=" "
        return result

    def conditionsOutput (self, header, statement, footer, verbose=True):
        result = ""
        punctuation = r".,"

        statement = statement.strip().strip(punctuation)
        header = header.strip()
        
        statementTxt = statement if not header else self.colorLua("71d5ffff", statement)
        footerTxt= "\n{}".format(self.parent.name) if footer else "\n"
        if verbose and statement:
            result += "\n"
            if header :
                result += "\n{header}".format(header=self.colorLua("1eff00ff", header))
            result += "\n{statment}{footer}".format(statment = statementTxt, footer = footerTxt)
        elif statement:
            result += statement
        
        if result and not header:
            result+="\n"
        return result

    def setConditions (self, t, verbose=True):
        result = ""
        elseHeader = ""
        header = ""
        status = False

        for c in t.conditions :
            footer = False
            compare = []
            for v in c.variables :
                if isinstance (v.value, (int, float)):
                    compare.append(v.value)
                elif v.var:
                    if v.spellId :
                        spell = self.parent.__class__(v.spellId)
                        spell.setItemLevel (self.ilevel)
                        if spell.exists():
                            current = spell
                        else :
                            compare.append(False)
                            continue
                    if v.var in ["a", "s"]:
                        currentClass = current.getChrClass()
                        if currentClass:
                            allClassSpecs = ChrSpecialization.FromParent(currentClass.id, parent=currentClass)
                            currentsSpecs = [x for x in current.getChrSpecs()]

                            specsNames = ", ".join([x.name for x in currentsSpecs])
                            if [x for x in allClassSpecs if x in currentsSpecs and x.name != "Initial"]:
                                elseHeader = ", ".join([ x.name for x in allClassSpecs if x not in currentsSpecs])

                            if v.var == "s":
                                footer = not bool(specsNames) and current.name == self.parent.name
                                if ( specsNames and specsNames in current.name) or current.name == self.parent.name: # 
                                    v.var = "a"
                                else :
                                    header  = specsNames or current.name
                                    
                            if v.var == "a":
                                specLevel = current.getCurrentLevel()
                                
                                levelStr = " (Level {})".format(specLevel) if specLevel else ""
                                specStr = "{specName}{level}".format(specName=specsNames, level=levelStr)
                                header =  specStr

                    elif v.var == "c" and v.id:
                        chrCls = self.parent.getChrClass()
                        if chrCls and chrCls.exists():
                            clsId = chrCls.id
                            chrSpec = [x for x in ChrSpecialization._REFERENCES.values() if x.classID == clsId and x.orderIndex == v.id-1]
                            if chrSpec :
                                header = chrSpec[0].name
                    
                    compare.append(bool(header))

                elif v.hashVariable :
                    # Converting any static variables into 0 for compare, may be should show all
                    compare.append(True)
                else :
                    compare.append(False)

            # Convert string operators into python
            ops = [self.OPS_MAPPING[x]  for x in c.operators]
            # Compare all
            status = functools.reduce(lambda a, b: b[0](a, b[1]), zip(ops, compare[1:]), compare[0])

            if status:
                result += self.conditionsOutput (header, c.statement, footer, verbose=verbose)

        if not status :
            result += self.conditionsOutput (elseHeader, t.statement, None, verbose=verbose)

        if result: 
            result += "\n"

        if not header and not elseHeader:
            result = result.strip("\n")
            result+=" "
        elif t.statement and not elseHeader:
            result = result.rstrip("\n")
            result+=" "
        if self.parent.name in t.statement :
            result = result.rstrip("\n")
        if not verbose :
            result = result.replace("\n", "")
        return result

class EnchantmentDescriptionParser(SpellDescriptionParser):
    def __init__ (self, text, parent=None):
        super (EnchantmentDescriptionParser, self).__init__ (text, parent)
    
    def setReferences (self, t):
        current = self.parent
        result = ""
        if t.var :
            t.var = t.var.lower()
            if isinstance (t.effectId, int) and t.effectId>=0 :
                if t.var == "k" :
                    spellScaling = SpellScaling[current.maxLevel]
                    scalingBase = spellScaling.getTypeValue(current.scalingClass)
                    v = scalingBase * current.effectScalingPoints[1]
                    result = int(round(v))
            
        return str(result)
    
    def setCurrent (self, text, parent=None, **kwargs):
        self.text = text
        self.parent = parent
        self.descriptionVariables = None
        self.variables = {}
        self.descVariables = {}


class EncounterSectionParser(LuaParser):
    def __init__ (self, text, parent=None):
        super (EncounterSectionParser, self).__init__ (text, parent)
    
    def compute (self, text, verbose=True):
        
        vbar = Literal("|")
        hlinkCap = vbar + Literal("H")
        hlink = vbar + Literal("h")
        dollar = Literal('$')
        lbrack = Literal("[")
        rbrack = Literal("]")
        exclamationMark = Literal("!")

        numberInt =Word(nums).addParseAction(tokenMap(int))
        #Condition
        conditionParser = (
            dollar + 
            lbrack + 
            exclamationMark +
            OneOrMore(
                numberInt + 
                Optional(Literal(",").suppress())
                ).setResultsName("difficulties") +
            SkipTo(dollar).setResultsName("text") + 
            Suppress(dollar + rbrack)
        ).addParseAction(self.setCondition)

        # Hyperlink
        hyperlinkParser = (
            Suppress(hlinkCap) + 
            SkipTo(hlink).setResultsName("link") + 
            Suppress(hlink) + 
            SkipTo(hlink).setResultsName("anchor") + 
            Suppress(hlink)
            ).addParseAction(self.setHyperlink)
       
        # Parsing layer by layer
        parsingOrder = [conditionParser, hyperlinkParser]
        steps = [text]
        for parser in parsingOrder :
            steps.append(parser.transformString(steps[-1]))
        result = steps[-1]
        return super (EncounterSectionParser, self).compute(result, verbose)
    
    def setHyperlink(self, t):
        linkType, linkId = t.link.split(":")
        if linkType == "spell":
            from .models.spell import Spell
            return Spell(int(linkId)).getShortText()
    
    def setCondition(self, t):
        difficulties = ", ".join([Difficulty(x).name for x in t.difficulties])
        return "{difficulties}:\n{text}".format(difficulties=difficulties, text=t.text)
