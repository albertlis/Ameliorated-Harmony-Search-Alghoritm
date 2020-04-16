from PyQt5.QtWidgets import QDoubleSpinBox, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QStatusBar, QSpacerItem, \
    QSizePolicy

from ui.bandwidthDialog import Ui_bandwidthDialog
from pprint import pprint


# Na razie nie zabezpieczone, da sie to rozwiazac?


class BandwidthDialog(Ui_bandwidthDialog):
    def __init__(self):
        super(BandwidthDialog, self).__init__()
        self.__minBoxes = []
        self.__maxBoxes = []
        self.__minMaxValues = ((0.0, 0.0), (0.0, 0.0))

    def setupUi(self, variables):
        super().setupUi(self)
        self.__setLayout(self, variables)
        self.calculateButton.clicked.connect(self.__calculateButtonClicked)

    def __setLayout(self, bwDialog, variables):
        # self.variables = variables
        verticalLayout = QVBoxLayout()
        for var in variables:
            verticalLayout.addLayout(self.__addLineWithBandwidthParameters(var))
        self.calculateButton = self.__makeCalculateButton()
        self.statusBar = QStatusBar()
        verticalLayout.addSpacerItem(QSpacerItem(20, 50, QSizePolicy.Expanding, QSizePolicy.Expanding))
        verticalLayout.addWidget(self.calculateButton)
        verticalLayout.addWidget(self.statusBar)
        bwDialog.setLayout(verticalLayout)

    def __makeCalculateButton(self):
        calculateButton = QPushButton()
        calculateButton.setText("Calculate")
        calculateButton.setObjectName("calculateButton")
        return calculateButton

    def __addLineWithBandwidthParameters(self, var):
        horizontalLayout = QHBoxLayout()
        minText = QLabel(var + ' min:')
        maxText = QLabel('max:')
        minBox = QDoubleSpinBox()
        minBox.setMinimum(1e-20)
        self.__minBoxes.append(minBox)
        maxBox = QDoubleSpinBox()
        maxBox.setMinimum(1e-20)
        self.__maxBoxes.append(maxBox)
        horizontalLayout.addWidget(minText)
        horizontalLayout.addWidget(minBox)
        horizontalLayout.addWidget(maxText)
        horizontalLayout.addWidget(maxBox)
        return horizontalLayout

    def __calculateButtonClicked(self):
        minValues = [minBox.value() for minBox in self.__minBoxes]
        maxValues = [maxBox.value() for maxBox in self.__maxBoxes]
        self.__minMaxValues = tuple(zip(minValues, maxValues))
        if not self.__checkMinMaxIsCorrect():
            return
        self.accept()

    def getMinMaxValues(self):
        # if '__minMaxValues' in locals():
        #     self.__minMaxValues = ((0.0, 0.0), (0.0, 0.0))
        return self.__minMaxValues

    def __checkMinMaxIsCorrect(self):
        for min, max in self.__minMaxValues:
            if min >= max:
                self.statusBar.showMessage("Min musi być większe niż max")
                return False
        return True
