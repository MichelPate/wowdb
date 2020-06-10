class ChrUnitMeasurement (object):
    _UNIT = ""
    def __init__ (self):
        super (ChrUnitMeasurement, self).__init__()
    def __str__ (self):
        return "{}".format(self._UNIT)

class ChrUnitBasePoint (ChrUnitMeasurement):
    def __init__ (self):
        super (ChrUnitBasePoint, self).__init__()

class ChrUnitPower (ChrUnitMeasurement):
    _UNIT = ""
    def __init__ (self):
        super (ChrUnitPower, self).__init__()
    def __str__ (self):
        return "% of {} power".format(self._UNIT)

class ChrUnitSpellPower (ChrUnitPower):
    _UNIT = "Spell"
    def __init__ (self):
        super (ChrUnitSpellPower, self).__init__()

class ChrUnitAttackPower (ChrUnitPower):
    _UNIT = "Attack"
    def __init__ (self):
        super (ChrUnitAttackPower, self).__init__()