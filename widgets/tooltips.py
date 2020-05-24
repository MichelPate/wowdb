from PySide2 import QtWidgets, QtGui, QtCore

class TooltipDialog (QtWidgets.QDialog):
    SIZE = 10
    COLOR = {"Default": (255,255,255), "Background":(20,20,20), "Border":(20,20,20)}
    def __init__ (self, text, parent=None):
        super(TooltipDialog, self).__init__(parent)
        self.setWindowFlags(QtCore.Qt.ToolTip | QtCore.Qt.WindowStaysOnTopHint |  QtCore.Qt.FramelessWindowHint)
        self.setFocusPolicy(QtCore.Qt.NoFocus)
        self.setAutoFillBackground(True)

        self.setStyleSheet("""QDialog { 
            border: 1px solid rgb(125,125,125); 
            background-color: rgb(20,20,20); 
        }""")

        self.layout = QtWidgets.QFormLayout()
        self.setLayout(self.layout)
        self.setMaximumWidth(350)

        label = QtWidgets.QLabel()
        label.setTextFormat(QtCore.Qt.RichText)
        label.setText (text)
        label.setWordWrap(True)
        label.setAlignment(QtCore.Qt.AlignJustify)
        self.layout.addRow (label)

    def showEvent (self, event):
        self.move(QtGui.QCursor.pos())
        super(TooltipDialog, self).showEvent(event)