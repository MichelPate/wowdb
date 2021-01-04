from PySide2 import QtWidgets, QtGui, QtCore

class TooltipDialog (QtWidgets.QDialog):
    SIZE = 10
    COLOR = {"Default": (255,255,255), "Background":(20,20,20), "Border":(20,20,20)}
    def __init__ (self, obj=None, parent=None, **kwargs):
        super(TooltipDialog, self).__init__(parent)
        self.setWindowFlags(QtCore.Qt.ToolTip | QtCore.Qt.WindowStaysOnTopHint |  QtCore.Qt.FramelessWindowHint)
        self.setFocusPolicy(QtCore.Qt.NoFocus)
        self.setAutoFillBackground(True)
        self.text = kwargs.get("text", None)
        self.setStyleSheet("""QDialog { 
            border: 1px solid rgb(125,125,125); 
            background-color: rgb(20,20,20); 
        }""")

        self.obj = obj
        self.kwargs = kwargs
        self.layout = QtWidgets.QFormLayout()
        self.setLayout(self.layout)
        self.setMinimumWidth(280)
        self.setMaximumWidth(320)

        self.label = QtWidgets.QLabel()
        self.label.setTextFormat(QtCore.Qt.RichText)
        
        self.label.setWordWrap(True)
        self.label.setAlignment(QtCore.Qt.AlignJustify)
        self.layout.addRow (self.label)

    def showEvent (self, event):
        self.move(QtGui.QCursor.pos())
        super(TooltipDialog, self).showEvent(event)
        if not self.text:
            self.text = self.obj.getTooltipText(displayLevel=self.kwargs.get("displayLevel", 1))
        self.label.setText (self.text)