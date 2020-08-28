from PySide2 import QtWidgets, QtGui, QtCore
from .tooltips import TooltipDialog

class IconLabel (QtWidgets.QLabel):
    def __init__ (self, obj, parent=None, **kwargs):
        super(IconLabel, self).__init__(parent)
        self.setTextFormat(QtCore.Qt.RichText)
        self.iconSize = kwargs.get("size", 35)
        self.count = kwargs.get("count", False)
        icon = obj.getIcon(self.iconSize)

        self.setText (icon)
        self.tooltip = TooltipDialog(obj, self, **kwargs)
    
    def paintEvent(self, event):
        super(IconLabel, self).paintEvent(event)
        if self.count :
            painter = QtGui.QPainter(self)
            rect = QtCore.QRect(0,0,self.iconSize, self.iconSize+2)
            font = QtGui.QFont ()
            font.setBold(True)

            # path = QtGui.QPainterPath()
            # path.addText(rect, QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight, font, self.count["text"])
            # painter.drawPath(path)

            painter.setFont(font)
            painter.setPen(QtGui.QColor(255, 255, 255))
            painter.drawText(rect, QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight, self.count["text"])
            
            
    def enterEvent(self, event):
        if self.tooltip:
            self.tooltip.show()
        super(IconLabel, self).enterEvent(event)
    
    def leaveEvent(self, event):
        if self.tooltip:
            self.tooltip.hide()
        super(IconLabel, self).leaveEvent(event)