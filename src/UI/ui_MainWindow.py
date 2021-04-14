# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from Config.UIConstantListEn import *
#from Config.UIConstantList import *
from PyQt5.QtGui import QRegExpValidator, QIntValidator, QDoubleValidator


from UI.myFigureCanvas import QmyFigureCanvas
import UI.res_rc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(201, 633)

        font = QtGui.QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        MainWindow.setCentralWidget(self.centralWidget)

        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout_13.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_13.setSpacing(6)
        self.verticalLayout_13.setObjectName("verticalLayout_13")

        self.splitter_2 = QtWidgets.QSplitter(self.centralWidget)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setContentsMargins(11,11,11,11)
        self.splitter_2.setObjectName("splitter_2")

        self.tabWidget = QtWidgets.QTabWidget(self.splitter_2)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setObjectName("tabWidget")

        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_9.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_9.setSpacing(6)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.widget = QtWidgets.QWidget(self.tab)
        self.widget.setObjectName("widget")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")

        self.frame1 = QtWidgets.QFrame(self.widget)
        self.frame1.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame1.setObjectName("frame1")

        self.horizontalLayout1 = QtWidgets.QHBoxLayout(self.frame1)
        self.horizontalLayout1.setContentsMargins(11, 5, 11, 5)
        self.horizontalLayout1.setSpacing(12)
        self.horizontalLayout1.setObjectName("horizontalLayout1")

        self.labLoadTxt = QtWidgets.QLabel(self.frame1)
        self.labLoadTxt.setObjectName("labLoadTxt")
        self.horizontalLayout1.addWidget(self.labLoadTxt)

        self.comboFile = QtWidgets.QComboBox(self.frame1)
        self.comboFile.setMinimumSize(QtCore.QSize(100, 10))
        self.comboFile.setObjectName("comboFile")
        self.comboFile.addItem("")
        self.comboFile.addItem("")
        self.horizontalLayout1.addWidget(self.comboFile)

        self.labMethodTxt = QtWidgets.QLabel(self.frame1)
        self.labMethodTxt.setObjectName("labMethodTxt")
        self.horizontalLayout1.addWidget(self.labMethodTxt)

        self.comboMethod = QtWidgets.QComboBox(self.frame1)
        self.comboMethod.setMinimumSize(QtCore.QSize(120, 10))
        self.comboMethod.setObjectName("comboMethod")
        self.comboMethod.addItem("")
        self.comboMethod.addItem("")
        self.horizontalLayout1.addWidget(self.comboMethod)

        self.frame = QtWidgets.QFrame(self.widget)
        self.frame.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(11, 5, 11, 5)
        self.horizontalLayout.setSpacing(12)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.btnBuildBarChart = QtWidgets.QPushButton(self.frame)
        self.btnBuildBarChart.setMinimumSize(QtCore.QSize(150, 10))
        self.btnBuildBarChart.setObjectName("btnBuildBarChart")
        self.horizontalLayout.addWidget(self.btnBuildBarChart)

        self.btnBuildBarEditMS = QtWidgets.QLineEdit(self.frame)
        self.btnBuildBarEditMS.setMinimumSize(QtCore.QSize(150, 10))
        self.btnBuildBarEditMS.setObjectName("btnBuildBarEditMS")
        self.horizontalLayout.addWidget(self.btnBuildBarEditMS)

        self.label0_S1=QtWidgets.QLabel(self.frame)
        self.label0_S1.setObjectName("label0_S1")
        self.horizontalLayout.addWidget(self.label0_S1)

        self.btnBuildBarChartH = QtWidgets.QPushButton(self.frame)
        self.btnBuildBarChartH.setMinimumSize(QtCore.QSize(150, 10))
        self.btnBuildBarChartH.setObjectName("btnBuildBarChartH")
        self.horizontalLayout.addWidget(self.btnBuildBarChartH)

        self.btnBuildBarEditMM = QtWidgets.QLineEdit(self.frame)
        self.btnBuildBarEditMM.setMinimumSize(QtCore.QSize(150, 10))
        self.btnBuildBarEditMM.setObjectName("btnBuildBarEditMM")
        self.horizontalLayout.addWidget(self.btnBuildBarEditMM)

        self.label0_S2 = QtWidgets.QLabel(self.frame)
        self.label0_S2.setObjectName("label0_S2")
        self.horizontalLayout.addWidget(self.label0_S2)

        self.lableresult1 = QtWidgets.QLabel(self.frame)
        self.lableresult1.setObjectName("lableresult1")
        self.horizontalLayout.addWidget(self.lableresult1)

        self.frame3 = QtWidgets.QFrame(self.widget)
        self.frame3.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame3.setObjectName("frame3")

        self.horizontalLayout3 = QtWidgets.QHBoxLayout(self.frame3)
        self.horizontalLayout3.setContentsMargins(11, 5, 11, 5)
        self.horizontalLayout3.setSpacing(12)
        self.horizontalLayout3.setObjectName("horizontalLayout3")

        self.label31=QtWidgets.QLabel(self.frame3)
        self.label31.setObjectName("label31")
        self.horizontalLayout3.addWidget(self.label31)

        self.btnIteration = QtWidgets.QLineEdit(self.frame3)
        self.btnIteration.setMinimumSize(QtCore.QSize(60, 10))
        self.btnIteration.setObjectName("btnIteration")
        self.horizontalLayout3.addWidget(self.btnIteration)

        self.label32 = QtWidgets.QLabel(self.frame3)
        self.label32.setObjectName("label32")
        self.horizontalLayout3.addWidget(self.label32)

        self.btnTheta = QtWidgets.QLineEdit(self.frame3)
        self.btnTheta.setMinimumSize(QtCore.QSize(90, 10))
        self.btnTheta.setObjectName("btnTheta")
        self.horizontalLayout3.addWidget(self.btnTheta)

        self.label33 = QtWidgets.QLabel(self.frame3)
        self.label33.setObjectName("label33")
        self.horizontalLayout3.addWidget(self.label33)

        self.btnTheta5 = QtWidgets.QLineEdit(self.frame3)
        self.btnTheta5.setMinimumSize(QtCore.QSize(60, 10))
        self.btnTheta5.setObjectName("btnTheta5")
        self.horizontalLayout3.addWidget(self.btnTheta5)

        self.frame4 = QtWidgets.QFrame(self.widget)
        self.frame4.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame4.setObjectName("frame4")

        self.horizontalLayout4 = QtWidgets.QHBoxLayout(self.frame4)
        self.horizontalLayout4.setContentsMargins(11, 5, 11, 5)
        self.horizontalLayout4.setSpacing(12)
        self.horizontalLayout4.setObjectName("horizontalLayout4")

        self.btnBuildBarChartS = QtWidgets.QPushButton(self.frame4)
        # self.btnBuildBarChartS.setMinimumSize(100, 10)
        self.btnBuildBarChartS.setObjectName("btnBuildBarChartS")
        self.horizontalLayout4.addWidget(self.btnBuildBarChartS)

        spacerItem2 = QtWidgets.QSpacerItem(662, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        spacerItem3 = QtWidgets.QSpacerItem(662, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout1.addItem(spacerItem3)
        spacerItem4 = QtWidgets.QSpacerItem(662, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout3.addItem(spacerItem4)
        # spacerItem5 = QtWidgets.QSpacerItem(662, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        # self.horizontalLayout4.addItem(spacerItem5)
        self.verticalLayout_8.addWidget(self.frame1)
        self.verticalLayout_8.addWidget(self.frame)
        self.verticalLayout_8.addWidget(self.frame3)
        self.verticalLayout_8.addWidget(self.frame4)

        self.chartViewBar = QmyFigureCanvas(self.frame)
        # self.chartViewBar.setRenderHints(QtGui.QPainter.Antialiasing|QtGui.QPainter.TextAntialiasing)
        self.chartViewBar.setObjectName("chartViewBar")

        self.verticalLayout_8.addWidget(self.chartViewBar)
        self.verticalLayout_9.addWidget(self.widget)

        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/images/3.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab, icon3, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_10.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_10.setSpacing(6)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.widget_2 = QtWidgets.QWidget(self.tab_3)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_3 = QtWidgets.QFrame(self.widget_2)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setContentsMargins(11, 5, 11, 5)
        self.horizontalLayout_3.setSpacing(12)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem4 = QtWidgets.QSpacerItem(523, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)

        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/images/f4.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_11.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_11.setSpacing(6)
        self.verticalLayout_11.setObjectName("verticalLayout_11")

        self.widget_3 = QtWidgets.QWidget(self.tab_2)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")

        self.frame_4 = QtWidgets.QFrame(self.widget_3)
        self.frame_4.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setContentsMargins(11, 5, 11, 5)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.label = QtWidgets.QLabel(self.frame_4)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)

        self.comboCourse = QtWidgets.QComboBox(self.frame_4)
        self.comboCourse.setMinimumSize(QtCore.QSize(90, 0))
        self.comboCourse.setObjectName("comboCourse")
        self.comboCourse.addItem("")
        self.comboCourse.addItem("")
        self.horizontalLayout_2.addWidget(self.comboCourse)

        self.label_S4 = QtWidgets.QLabel(self.frame_4)
        self.label_S4.setObjectName("label_S4")
        self.horizontalLayout_2.addWidget(self.label_S4)

        self.label_2 = QtWidgets.QLabel(self.frame_4)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)

        self.pieEdit_2 = QtWidgets.QLineEdit(self.frame_4)
        self.pieEdit_2.setMinimumSize(QtCore.QSize(70, 0))
        self.pieEdit_2.setObjectName("pieEdit_2")
        self.horizontalLayout_2.addWidget(self.pieEdit_2)

        self.label_22 = QtWidgets.QLabel(self.frame_4)
        self.label_22.setObjectName("label_22")
        self.horizontalLayout_2.addWidget(self.label_22)

        self.label_S1 = QtWidgets.QLabel(self.frame_4)
        self.label_S1.setObjectName("label_S1")
        self.horizontalLayout_2.addWidget(self.label_S1)

        self.label_3 = QtWidgets.QLabel(self.frame_4)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)

        self.pieEdit_3 = QtWidgets.QLineEdit(self.frame_4)
        self.pieEdit_3.setMinimumSize(QtCore.QSize(70, 0))
        self.pieEdit_3.setObjectName("pieEdit_3")
        self.horizontalLayout_2.addWidget(self.pieEdit_3)

        self.label_33 = QtWidgets.QLabel(self.frame_4)
        self.label_33.setObjectName("label_33")
        self.horizontalLayout_2.addWidget(self.label_33)

        self.label_S2 = QtWidgets.QLabel(self.frame_4)
        self.label_S2.setObjectName("label_S2")
        self.horizontalLayout_2.addWidget(self.label_S2)

        self.label_4 = QtWidgets.QLabel(self.frame_4)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)

        self.pieEdit_4 = QtWidgets.QLineEdit(self.frame_4)
        self.pieEdit_4.setMinimumSize(QtCore.QSize(70, 0))
        self.pieEdit_4.setObjectName("pieEdit_4")
        self.horizontalLayout_2.addWidget(self.pieEdit_4)

        self.label_44 = QtWidgets.QLabel(self.frame_4)
        self.label_44.setObjectName("label_44")
        self.horizontalLayout_2.addWidget(self.label_44)

        self.label_S3 = QtWidgets.QLabel(self.frame_4)
        self.label_S3.setObjectName("label_S3")
        self.horizontalLayout_2.addWidget(self.label_S3)

        self.label_5 = QtWidgets.QLabel(self.frame_4)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)

        self.pieEdit_5 = QtWidgets.QLineEdit(self.frame_4)
        self.pieEdit_5.setMinimumSize(QtCore.QSize(70, 0))
        self.pieEdit_5.setObjectName("pieEdit_5")
        self.horizontalLayout_2.addWidget(self.pieEdit_5)

        self.label_55 = QtWidgets.QLabel(self.frame_4)
        self.label_55.setObjectName("label_55")
        self.horizontalLayout_2.addWidget(self.label_55)

        # spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        # self.horizontalLayout_2.addItem(spacerItem5)

        self.frame_5 = QtWidgets.QFrame(self.widget_3)
        self.frame_5.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")

        self.horizontalLayout_4 = QtWidgets.QGridLayout(self.frame_5)
        self.horizontalLayout_4.setContentsMargins(11, 5, 11, 5)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")

        self.label2_2 = QtWidgets.QLabel(self.frame_5)
        self.label2_2.setObjectName("label2_2")
        self.horizontalLayout_4.addWidget(self.label2_2,0,0)

        self.pieEdit2_2 = QtWidgets.QLineEdit(self.frame_5)
        self.pieEdit2_2.setBaseSize(QtCore.QSize(70, 0))
        self.pieEdit2_2.setObjectName("pieEdit2_2")
        self.horizontalLayout_4.addWidget(self.pieEdit2_2,0,1)

        self.label2_22 = QtWidgets.QLabel(self.frame_5)
        self.label2_22.setObjectName("label2_22")
        self.horizontalLayout_4.addWidget(self.label2_22,0,2)

        self.label2_S2 = QtWidgets.QLabel(self.frame_5)
        self.label2_S2.setObjectName("label2_S2")
        self.horizontalLayout_4.addWidget(self.label2_S2,0,3)

        self.label3_2 = QtWidgets.QLabel(self.frame_5)
        self.label3_2.setObjectName("label3_2")
        self.horizontalLayout_4.addWidget(self.label3_2,0,4)

        self.pieEdit3_2 = QtWidgets.QLineEdit(self.frame_5)
        self.pieEdit3_2.setBaseSize(QtCore.QSize(70, 0))
        self.pieEdit3_2.setObjectName("pieEdit3_2")
        self.horizontalLayout_4.addWidget(self.pieEdit3_2,0,5)

        self.label3_22 = QtWidgets.QLabel(self.frame_5)
        self.label3_22.setObjectName("label3_22")
        self.horizontalLayout_4.addWidget(self.label3_22,0,6)

        self.label3_S2 = QtWidgets.QLabel(self.frame_5)
        self.label3_S2.setObjectName("label3_S2")
        self.horizontalLayout_4.addWidget(self.label3_S2,0,7)

        self.label4_2 = QtWidgets.QLabel(self.frame_5)
        self.label4_2.setObjectName("label4_2")
        self.horizontalLayout_4.addWidget(self.label4_2,0,8)

        self.pieEdit4_2 = QtWidgets.QLineEdit(self.frame_5)
        self.pieEdit4_2.setBaseSize(QtCore.QSize(70, 0))
        self.pieEdit4_2.setObjectName("pieEdit4_2")
        self.horizontalLayout_4.addWidget(self.pieEdit4_2,0,9)

        self.label4_22 = QtWidgets.QLabel(self.frame_5)
        self.label4_22.setObjectName("label4_22")
        self.horizontalLayout_4.addWidget(self.label4_22,0,10)

        self.label4_S2 = QtWidgets.QLabel(self.frame_5)
        self.label4_S2.setObjectName("label4_S2")
        self.horizontalLayout_4.addWidget(self.label4_S2,0,11)

        self.label5_2 = QtWidgets.QLabel(self.frame_5)
        self.label5_2.setObjectName("label5_2")
        self.horizontalLayout_4.addWidget(self.label5_2)

        self.pieEdit5_2 = QtWidgets.QLineEdit(self.frame_5)
        self.pieEdit5_2.setBaseSize(QtCore.QSize(70, 0))
        self.pieEdit5_2.setObjectName("pieEdit5_2")
        self.horizontalLayout_4.addWidget(self.pieEdit5_2)

        self.label5_22 = QtWidgets.QLabel(self.frame_5)
        self.label5_22.setObjectName("label5_22")
        self.horizontalLayout_4.addWidget(self.label5_22)

        self.label5_S2 = QtWidgets.QLabel(self.frame_5)
        self.label5_S2.setObjectName("label5_S2")
        self.horizontalLayout_4.addWidget(self.label5_S2)

        self.label6_2 = QtWidgets.QLabel(self.frame_5)
        self.label6_2.setObjectName("label6_2")
        self.horizontalLayout_4.addWidget(self.label6_2)

        self.pieEdit6_2 = QtWidgets.QLineEdit(self.frame_5)
        self.pieEdit6_2.setBaseSize(QtCore.QSize(70, 0))
        self.pieEdit6_2.setObjectName("pieEdit6_2")
        self.horizontalLayout_4.addWidget(self.pieEdit6_2)

        self.label6_22 = QtWidgets.QLabel(self.frame_5)
        self.label6_22.setObjectName("label6_22")
        self.horizontalLayout_4.addWidget(self.label6_22)

        self.label6_S2 = QtWidgets.QLabel(self.frame_5)
        self.label6_S2.setObjectName("label6_S2")
        self.horizontalLayout_4.addWidget(self.label6_S2)

        self.label7_2 = QtWidgets.QLabel(self.frame_5)
        self.label7_2.setObjectName("label7_2")
        self.horizontalLayout_4.addWidget(self.label7_2)

        self.pieEdit7_2 = QtWidgets.QLineEdit(self.frame_5)
        self.pieEdit7_2.setBaseSize(QtCore.QSize(70, 0))
        self.pieEdit7_2.setObjectName("pieEdit7_2")
        self.horizontalLayout_4.addWidget(self.pieEdit7_2)

        self.label7_22 = QtWidgets.QLabel(self.frame_5)
        self.label7_22.setObjectName("label7_22")
        self.horizontalLayout_4.addWidget(self.label7_22)

        self.label7_S2 = QtWidgets.QLabel(self.frame_5)
        self.label7_S2.setObjectName("label7_S2")
        self.horizontalLayout_4.addWidget(self.label7_S2)

        self.label8_2 = QtWidgets.QLabel(self.frame_5)
        self.label8_2.setObjectName("label8_2")
        self.horizontalLayout_4.addWidget(self.label8_2)

        self.pieEdit8_2 = QtWidgets.QLineEdit(self.frame_5)
        self.pieEdit8_2.setBaseSize(QtCore.QSize(70, 0))
        self.pieEdit8_2.setObjectName("pieEdit8_2")
        self.horizontalLayout_4.addWidget(self.pieEdit8_2)

        self.label8_22 = QtWidgets.QLabel(self.frame_5)
        self.label8_22.setObjectName("label8_22")
        self.horizontalLayout_4.addWidget(self.label8_22)

        self.label8_S2 = QtWidgets.QLabel(self.frame_5)
        self.label8_S2.setObjectName("label8_S2")
        self.horizontalLayout_4.addWidget(self.label8_S2)

        self.label9_2 = QtWidgets.QLabel(self.frame_5)
        self.label9_2.setObjectName("label9_2")
        self.horizontalLayout_4.addWidget(self.label9_2)

        self.pieEdit9_2 = QtWidgets.QLineEdit(self.frame_5)
        self.pieEdit9_2.setBaseSize(QtCore.QSize(70, 0))
        self.pieEdit9_2.setObjectName("pieEdit9_2")
        self.horizontalLayout_4.addWidget(self.pieEdit9_2)

        self.label9_22 = QtWidgets.QLabel(self.frame_5)
        self.label9_22.setObjectName("label9_22")
        self.horizontalLayout_4.addWidget(self.label9_22)

        self.label9_S2 = QtWidgets.QLabel(self.frame_5)
        self.label9_S2.setObjectName("label9_S2")
        self.horizontalLayout_4.addWidget(self.label9_S2)

        self.lableresult2 = QtWidgets.QLabel(self.frame)
        self.lableresult2.setObjectName("lableresult2")
        self.horizontalLayout_4.addWidget(self.lableresult2)

        self.frame_6 = QtWidgets.QFrame(self.widget_3)
        self.frame_6.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")

        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_5.setContentsMargins(11, 5, 11, 5)
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")


        self.btnDrawPieChart = QtWidgets.QPushButton(self.frame_6)
        self.btnDrawPieChart.setObjectName("btnDrawPieChart")
        self.horizontalLayout_5.addWidget(self.btnDrawPieChart)

        self.frame_7 = QtWidgets.QFrame(self.widget_3)
        self.frame_7.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")

        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_6.setContentsMargins(11, 5, 11, 5)
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")

        self.labMethodTxt2 = QtWidgets.QLabel(self.frame_7)
        self.labMethodTxt2.setObjectName("labMethodTxt2")
        self.horizontalLayout_6.addWidget(self.labMethodTxt2)

        self.comboMethod2 = QtWidgets.QComboBox(self.frame_7)
        self.comboMethod2.setMinimumSize(QtCore.QSize(120, 10))
        self.comboMethod2.setObjectName("comboMethod2")
        self.comboMethod2.addItem("")
        self.comboMethod2.addItem("")
        self.horizontalLayout_6.addWidget(self.comboMethod2)

        self.label231 = QtWidgets.QLabel(self.frame_7)
        self.label231.setObjectName("label231")
        self.horizontalLayout_6.addWidget(self.label231)

        self.btnIteration2 = QtWidgets.QLineEdit(self.frame_7)
        self.btnIteration2.setMinimumSize(QtCore.QSize(60, 10))
        self.btnIteration2.setObjectName("btnIteration2")
        self.horizontalLayout_6.addWidget(self.btnIteration2)

        self.label232 = QtWidgets.QLabel(self.frame_7)
        self.label232.setObjectName("label232")
        self.horizontalLayout_6.addWidget(self.label232)

        self.btnTheta2 = QtWidgets.QLineEdit(self.frame_7)
        self.btnTheta2.setMinimumSize(QtCore.QSize(60, 10))
        self.btnTheta2.setObjectName("btnTheta")
        self.horizontalLayout_6.addWidget(self.btnTheta2)

        self.label233 = QtWidgets.QLabel(self.frame_7)
        self.label233.setObjectName("label233")
        self.horizontalLayout_6.addWidget(self.label233)

        self.btnDelta2 = QtWidgets.QLineEdit(self.frame_7)
        self.btnDelta2.setMinimumSize(QtCore.QSize(60, 10))
        self.btnDelta2.setObjectName("btnTheta")
        self.horizontalLayout_6.addWidget(self.btnDelta2)

        self.label234 = QtWidgets.QLabel(self.frame_7)
        self.label234.setObjectName("label234")
        self.horizontalLayout_6.addWidget(self.label234)

        self.label235 = QtWidgets.QLabel(self.frame_7)
        self.label235.setObjectName("label235")
        self.horizontalLayout_6.addWidget(self.label235)

        self.btnDelta3 = QtWidgets.QLineEdit(self.frame_7)
        self.btnDelta3.setMinimumSize(QtCore.QSize(60, 10))
        self.btnDelta3.setObjectName("btnThreshold")
        self.horizontalLayout_6.addWidget(self.btnDelta3)

        spacerItem4 = QtWidgets.QSpacerItem(662, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem4)
        self.verticalLayout_4.addWidget(self.frame_4)
        self.verticalLayout_4.addWidget(self.frame_5)
        self.verticalLayout_4.addWidget(self.frame_7)
        self.verticalLayout_4.addWidget(self.frame_6)

        self.chartViewPie = QmyFigureCanvas(self.frame_4)
        self.chartViewPie.setObjectName("chartViewPie")
        self.verticalLayout_4.addWidget(self.chartViewPie)

        self.verticalLayout_11.addWidget(self.widget_3)

        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/images/43.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_2, icon6, "")
        self.verticalLayout_13.addWidget(self.splitter_2)

        MainWindow.setCentralWidget(self.centralWidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate

        self.labLoadTxt.setText(_translate("MainWindow",FILETYPE))
        self.comboFile.setItemText(0, _translate("MainWindow", "MDF"))
        self.comboFile.setItemText(1, _translate("MainWindow", "JSON"))
        self.labMethodTxt.setText(_translate("MainWindow", RECONMETHOD))
        self.comboMethod.setItemText(0, _translate("MainWindow", "System Matrix"))
        self.comboMethod.setItemText(1, _translate("MainWindow", "XSpace"))


        self.btnBuildBarChart.setText(_translate("MainWindow", SMDIR))
        self.btnBuildBarChartH.setText(_translate("MainWindow", MEADIR))
        self.btnBuildBarChartS.setText(_translate("MainWindow", RECONBTN))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", FILERECON))
        self.label0_S1.setText(_translate("MainWindow", "|"))
        self.label0_S2.setText(_translate("MainWindow", "|"))
        # self.label0_S3.setText(_translate("MainWindow", "|"))

        self.label31.setText(_translate("MainWindow",NUMITERA))
        self.label32.setText(_translate("MainWindow", REGPARAM))
        self.label33.setText(_translate("MainWindow", THRESHOLDSEG2))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", SIMURECON))
        self.label.setText(_translate("MainWindow", PHANSHAPE))
        self.comboCourse.setItemText(0, _translate("MainWindow", "P Shape"))
        self.comboCourse.setItemText(1, _translate("MainWindow", "E Shape"))
        self.btnDrawPieChart.setText(_translate("MainWindow", SIMUBTN))
        self.label_2.setText(_translate("MainWindow", PARTTEMPE))
        self.label_22.setText(_translate("MainWindow", "℃"))
        self.label_3.setText(_translate("MainWindow", PARTDIA))
        self.label_33.setText(_translate("MainWindow", "nm"))
        self.label_4.setText(_translate("MainWindow", PARTSATMAG))
        self.label_44.setText(_translate("MainWindow", "KA/m"))
        self.label_5.setText(_translate("MainWindow", PARTCON))
        self.label_55.setText(_translate("MainWindow", "mmol/L"))
        self.label_S1.setText(_translate("MainWindow", "|"))
        self.label_S2.setText(_translate("MainWindow", "|"))
        self.label_S3.setText(_translate("MainWindow", "|"))
        self.label_S4.setText(_translate("MainWindow", "|"))

        self.label2_2.setText(_translate("MainWindow", SELECTFIELDGRADX))
        self.label2_22.setText(_translate("MainWindow", "T/m"))
        self.label2_S2.setText(_translate("MainWindow", "|"))
        self.label3_2.setText(_translate("MainWindow", SELECTFIELDGRADY))
        self.label3_22.setText(_translate("MainWindow", "T/m"))
        self.label3_S2.setText(_translate("MainWindow", "|"))
        self.label4_2.setText(_translate("MainWindow", DRIVEFIELDFREQX))
        self.label4_22.setText(_translate("MainWindow", "KHz"))
        self.label4_S2.setText(_translate("MainWindow", "|"))
        self.label5_2.setText(_translate("MainWindow", DRIVEFIELDFREQY))
        self.label5_22.setText(_translate("MainWindow", "KHz"))
        self.label5_S2.setText(_translate("MainWindow", "|"))
        self.label6_2.setText(_translate("MainWindow", DRIVEFIELDAMPX))
        self.label6_22.setText(_translate("MainWindow", "mT"))
        self.label6_S2.setText(_translate("MainWindow", "|"))
        self.label7_2.setText(_translate("MainWindow", DRIVEFIELDAMPY))
        self.label7_22.setText(_translate("MainWindow", "mT"))
        self.label7_S2.setText(_translate("MainWindow", "|"))
        self.label8_2.setText(_translate("MainWindow", REPEATTIME))
        self.label8_22.setText(_translate("MainWindow", "us"))
        self.label8_S2.setText(_translate("MainWindow", "|"))
        self.label9_2.setText(_translate("MainWindow", SAMPLEREQ))
        self.label9_22.setText(_translate("MainWindow", "MHz"))
        self.label9_S2.setText(_translate("MainWindow", "|"))

        self.labMethodTxt2.setText(_translate("MainWindow", RECONMETHOD2))
        self.comboMethod2.setItemText(0, _translate("MainWindow", "System Matrix"))
        self.comboMethod2.setItemText(1, _translate("MainWindow", "XSpace"))
        self.label231.setText(_translate("MainWindow", NUMITERA2))
        self.label232.setText(_translate("MainWindow", REGPARAM2))
        self.label233.setText(_translate("MainWindow", DELTASAMPLECON))
        self.label234.setText(_translate("MainWindow", "mmol/L"))
        self.label235.setText(_translate("MainWindow", THRESHOLDSEG))

        self.pieEdit_2.setText("20")
        self.pieEdit_3.setText("30")
        self.pieEdit_4.setText("800")
        self.pieEdit_5.setText("50")

        self.pieEdit2_2.setText("2")
        self.pieEdit3_2.setText("2")
        self.pieEdit4_2.setText("24.51")
        self.pieEdit5_2.setText("26.042")
        self.pieEdit6_2.setText("12")
        self.pieEdit7_2.setText("12")
        self.pieEdit8_2.setText("652.8")
        self.pieEdit9_2.setText("2.5")

        self.btnIteration.setText("1")
        self.btnIteration2.setText("1")
        self.btnTheta.setText("0.000001")
        self.btnTheta2.setText("0.000001")
        self.btnDelta2.setText("1")
        self.btnDelta3.setText("150")
        self.btnTheta5.setText("150")

        doubleValidator = QDoubleValidator()
        doubleValidator.setNotation(QDoubleValidator.StandardNotation)
        self.pieEdit_2.setValidator(doubleValidator)
        self.pieEdit_3.setValidator(doubleValidator)
        self.pieEdit_4.setValidator(doubleValidator)
        self.pieEdit_5.setValidator(doubleValidator)

        self.pieEdit2_2.setValidator(doubleValidator)
        self.pieEdit3_2.setValidator(doubleValidator)
        self.pieEdit4_2.setValidator(doubleValidator)
        self.pieEdit5_2.setValidator(doubleValidator)
        self.pieEdit6_2.setValidator(doubleValidator)
        self.pieEdit7_2.setValidator(doubleValidator)
        self.pieEdit8_2.setValidator(doubleValidator)
        self.pieEdit9_2.setValidator(doubleValidator)

        self.btnTheta.setValidator(doubleValidator)
        self.btnTheta2.setValidator(doubleValidator)
        self.btnDelta2.setValidator(doubleValidator)

        intValidator = QIntValidator()
        self.btnIteration.setValidator(intValidator)
        self.btnIteration2.setValidator(intValidator)
        self.btnDelta3.setValidator(intValidator)
        self.btnTheta5.setValidator(intValidator)
