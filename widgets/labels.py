from PySide2 import QtWidgets, QtGui, QtCore
from .tooltips import TooltipDialog

class SpellLabel (QtWidgets.QLabel):
    def __init__ (self, spell, parent=None, **kwargs):
        super(SpellLabel, self).__init__(parent)
        self.setTextFormat(QtCore.Qt.RichText)
        self.setText (spell.getShortText())
        self.tooltip = TooltipDialog(spell.getTooltipText(displayLevel=2), self)
        
    def enterEvent(self, event):
        if self.tooltip:
            self.tooltip.show()
        super(SpellLabel, self).enterEvent(event)
    
    def leaveEvent(self, event):
        if self.tooltip:
            self.tooltip.hide()
        super(SpellLabel, self).leaveEvent(event)