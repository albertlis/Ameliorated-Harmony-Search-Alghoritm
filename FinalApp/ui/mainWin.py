# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWin(object):
    def setupUi(self, MainWin):
        MainWin.setObjectName("MainWin")
        MainWin.resize(939, 523)
        self.centralwidget = QtWidgets.QWidget(MainWin)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(55, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.functionBox = QtWidgets.QLineEdit(self.centralwidget)
        self.functionBox.setMinimumSize(QtCore.QSize(200, 0))
        self.functionBox.setObjectName("functionBox")
        self.horizontalLayout.addWidget(self.functionBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.iterationsBox = QtWidgets.QSpinBox(self.centralwidget)
        self.iterationsBox.setMouseTracking(False)
        self.iterationsBox.setToolTip("")
        self.iterationsBox.setToolTipDuration(-1)
        self.iterationsBox.setStatusTip("")
        self.iterationsBox.setWhatsThis("")
        self.iterationsBox.setSpecialValueText("")
        self.iterationsBox.setMinimum(1)
        self.iterationsBox.setMaximum(999999999)
        self.iterationsBox.setProperty("value", 2000)
        self.iterationsBox.setObjectName("iterationsBox")
        self.horizontalLayout_3.addWidget(self.iterationsBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        self.hmsBox = QtWidgets.QSpinBox(self.centralwidget)
        self.hmsBox.setMinimum(1)
        self.hmsBox.setMaximum(99999999)
        self.hmsBox.setProperty("value", 10)
        self.hmsBox.setObjectName("hmsBox")
        self.horizontalLayout_6.addWidget(self.hmsBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.hcmrMinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.hcmrMinBox.setMaximum(1.0)
        self.hcmrMinBox.setSingleStep(0.1)
        self.hcmrMinBox.setProperty("value", 0.2)
        self.hcmrMinBox.setObjectName("hcmrMinBox")
        self.horizontalLayout_4.addWidget(self.hcmrMinBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_10.addWidget(self.label_10)
        self.hcmrMaxBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.hcmrMaxBox.setMaximum(1.0)
        self.hcmrMaxBox.setSingleStep(0.1)
        self.hcmrMaxBox.setProperty("value", 0.8)
        self.hcmrMaxBox.setObjectName("hcmrMaxBox")
        self.horizontalLayout_10.addWidget(self.hcmrMaxBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.parMinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.parMinBox.setMaximum(1.0)
        self.parMinBox.setSingleStep(0.1)
        self.parMinBox.setProperty("value", 0.2)
        self.parMinBox.setObjectName("parMinBox")
        self.horizontalLayout_5.addWidget(self.parMinBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_8.addWidget(self.label_8)
        self.parMaxBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.parMaxBox.setMaximum(1.0)
        self.parMaxBox.setSingleStep(0.1)
        self.parMaxBox.setProperty("value", 0.8)
        self.parMaxBox.setObjectName("parMaxBox")
        self.horizontalLayout_8.addWidget(self.parMaxBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.nextButton = QtWidgets.QPushButton(self.centralwidget)
        self.nextButton.setAutoFillBackground(False)
        self.nextButton.setStyleSheet("")
        self.nextButton.setAutoDefault(False)
        self.nextButton.setDefault(True)
        self.nextButton.setObjectName("nextButton")
        self.verticalLayout_3.addWidget(self.nextButton)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 1, 1, 1)
        self.plotWidget = PlotWidget(self.centralwidget)
        self.plotWidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.plotWidget.sizePolicy().hasHeightForWidth())
        self.plotWidget.setSizePolicy(sizePolicy)
        self.plotWidget.setMinimumSize(QtCore.QSize(600, 0))
        self.plotWidget.setToolTip("")
        self.plotWidget.setWhatsThis("")
        self.plotWidget.setAccessibleDescription("")
        self.plotWidget.setObjectName("plotWidget")
        self.gridLayout.addWidget(self.plotWidget, 0, 2, 2, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 146, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 1, 0, 1, 1)
        MainWin.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWin)
        self.statusbar.setObjectName("statusbar")
        MainWin.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWin)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 939, 26))
        self.menubar.setObjectName("menubar")
        MainWin.setMenuBar(self.menubar)

        self.retranslateUi(MainWin)
        QtCore.QMetaObject.connectSlotsByName(MainWin)

    def retranslateUi(self, MainWin):
        _translate = QtCore.QCoreApplication.translate
        MainWin.setWindowTitle(_translate("MainWin", "Ulepszony Algorytm Poszukiwania Harmonii"))
        self.label_2.setText(_translate("MainWin", "Podaj funkcję"))
        self.label.setText(_translate("MainWin", "f(x)"))
        self.label_3.setText(_translate("MainWin", "Ilość iteracji:"))
        self.label_6.setText(_translate("MainWin", "HMS"))
        self.label_4.setText(_translate("MainWin", "HMCR min"))
        self.label_10.setText(_translate("MainWin", "HMCR max"))
        self.label_5.setText(_translate("MainWin", "PAR min"))
        self.label_8.setText(_translate("MainWin", "PAR max"))
        self.nextButton.setText(_translate("MainWin", "Dalej"))
from plotwidget import PlotWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWin = QtWidgets.QMainWindow()
    ui = Ui_MainWin()
    ui.setupUi(MainWin)
    MainWin.show()
    sys.exit(app.exec_())