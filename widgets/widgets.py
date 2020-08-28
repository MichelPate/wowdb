from PySide2 import QtWidgets, QtGui, QtCore
from .labels import IconLabel

class SkillTableWidget (QtWidgets.QTableWidget ):
    HEADER = ["Name", "Reagents", "Skill"]
    def __init__ (self, skillLine, parent=None, **kwargs):
        abilities = skillLine.getAbilities()
        rowCount = len(abilities)
        columnCount = len(self.HEADER)
        super(SkillTableWidget, self).__init__(rowCount, columnCount, parent)

        self.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.setFocusPolicy(QtCore.Qt.NoFocus)
        self.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

        hheader = QtWidgets.QHeaderView(QtCore.Qt.Orientation.Horizontal)
        hheader.setSectionResizeMode (QtWidgets.QHeaderView.ResizeToContents)
        self.setHorizontalHeader(hheader)
        self.setHorizontalHeaderLabels(self.HEADER)

        vheader = QtWidgets.QHeaderView(QtCore.Qt.Orientation.Vertical)
        vheader.setSectionResizeMode (QtWidgets.QHeaderView.ResizeToContents)
        self.setVerticalHeader(vheader)
        vheader.setVisible(False)
        
        for i, ability in enumerate(abilities) : 
            spellReagents = ability.getSpellReagents()
            if spellReagents :
                reagents = spellReagents.getReagents()

                spell = ability.getSpell()
                effect = spell.getCurrentEffects ()[0]
                item = effect.getItem()
                if item and item.exists():
                    spellLabel = IconLabel(item, size=25)
                else :
                    spellLabel = IconLabel(spell, size=25) 
                self.setCellWidget(i, 0, spellLabel)

                reagentsWidget = QtWidgets.QWidget()
                reagentsLayout = QtWidgets.QHBoxLayout(reagentsWidget)
                for reagent, count in reagents.items():
                    reagentLabel = IconLabel(reagent, size=25, count={"text":str(count)})
                    reagentsLayout.addWidget(reagentLabel)
                reagentsLayout.addStretch(1)
                self.setCellWidget(i, 1, reagentsWidget)

                mid = int((ability.trivialSkillLineRankLow+ability.trivialSkillLineRankHigh)*0.5)
                skillLevel = "<span style=\"color:#FFFF00\">{low}</span> <span style=\"color:#40bf40\">{mid}</span> <span style=\"color:#808080\">{high}</span>".format(low=ability.trivialSkillLineRankLow, mid=mid, high=ability.trivialSkillLineRankHigh)
                skillLevelLabel = QtWidgets.QLabel(skillLevel)
                self.setCellWidget(i, 2, skillLevelLabel)

        size = self.getTableSize()
        self.setMaximumSize(size)
        self.setMinimumSize(size)

    def getTableSize(self):
        w = self.verticalHeader().width() + 4  # +4 seems to be needed
        for i in range(self.columnCount()):
            w += self.columnWidth(i)  # seems to include gridline (on my machine)
        h = self.horizontalHeader().height() + 4
        for i in range(self.rowCount()):
            h += self.rowHeight(i)
        return QtCore.QSize(w, h)
            