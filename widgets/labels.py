from PySide2 import QtWidgets, QtGui, QtCore
from .tooltips import TooltipDialog

class IconLabel (QtWidgets.QLabel):
    def __init__ (self, obj, parent=None, **kwargs):
        super(IconLabel, self).__init__(parent)
        self.setTextFormat(QtCore.Qt.RichText)
        self.setText (obj.getIcon(kwargs.get("size", 35)))
        self.tooltip = TooltipDialog(obj, self, **kwargs)
        
    def enterEvent(self, event):
        if self.tooltip:
            self.tooltip.show()
        super(IconLabel, self).enterEvent(event)
    
    def leaveEvent(self, event):
        if self.tooltip:
            self.tooltip.hide()
        super(IconLabel, self).leaveEvent(event)