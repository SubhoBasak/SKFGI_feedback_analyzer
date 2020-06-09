# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setting_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Setting(object):
    def setupUi(self, Setting):
        Setting.setObjectName("Setting")
        Setting.resize(578, 387)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Setting.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(Setting)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(Setting)
        self.tabWidget.setObjectName("tabWidget")
        self.rating_5 = QtWidgets.QWidget()
        self.rating_5.setObjectName("rating_5")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.rating_5)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        spacerItem = QtWidgets.QSpacerItem(96, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem)
        self.my_label_3 = QtWidgets.QLabel(self.rating_5)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.my_label_3.setFont(font)
        self.my_label_3.setStyleSheet("color: rgb(100, 62, 255);")
        self.my_label_3.setObjectName("my_label_3")
        self.horizontalLayout_13.addWidget(self.my_label_3)
        spacerItem1 = QtWidgets.QSpacerItem(95, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem1)
        self.my_label_4 = QtWidgets.QLabel(self.rating_5)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.my_label_4.setFont(font)
        self.my_label_4.setStyleSheet("color: rgb(100, 62, 255);")
        self.my_label_4.setObjectName("my_label_4")
        self.horizontalLayout_13.addWidget(self.my_label_4)
        spacerItem2 = QtWidgets.QSpacerItem(96, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.map_in_1 = QtWidgets.QLineEdit(self.rating_5)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.map_in_1.setFont(font)
        self.map_in_1.setStyleSheet("color: rgb(255, 125, 39)")
        self.map_in_1.setObjectName("map_in_1")
        self.horizontalLayout_2.addWidget(self.map_in_1)
        self.label = QtWidgets.QLabel(self.rating_5)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.map_out_1 = QtWidgets.QLineEdit(self.rating_5)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.map_out_1.setFont(font)
        self.map_out_1.setStyleSheet("color: rgb(102, 255, 85);")
        self.map_out_1.setObjectName("map_out_1")
        self.horizontalLayout_2.addWidget(self.map_out_1)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.map_in_2 = QtWidgets.QLineEdit(self.rating_5)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.map_in_2.setFont(font)
        self.map_in_2.setStyleSheet("color: rgb(255, 125, 39)")
        self.map_in_2.setObjectName("map_in_2")
        self.horizontalLayout_5.addWidget(self.map_in_2)
        self.label_2 = QtWidgets.QLabel(self.rating_5)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.map_out_2 = QtWidgets.QLineEdit(self.rating_5)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.map_out_2.setFont(font)
        self.map_out_2.setStyleSheet("color: rgb(102, 255, 85);")
        self.map_out_2.setObjectName("map_out_2")
        self.horizontalLayout_5.addWidget(self.map_out_2)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_5)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem7)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.map_in_3 = QtWidgets.QLineEdit(self.rating_5)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.map_in_3.setFont(font)
        self.map_in_3.setStyleSheet("color: rgb(255, 125, 39)")
        self.map_in_3.setObjectName("map_in_3")
        self.horizontalLayout_7.addWidget(self.map_in_3)
        self.label_3 = QtWidgets.QLabel(self.rating_5)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_7.addWidget(self.label_3)
        self.map_out_3 = QtWidgets.QLineEdit(self.rating_5)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.map_out_3.setFont(font)
        self.map_out_3.setStyleSheet("color: rgb(102, 255, 85);")
        self.map_out_3.setObjectName("map_out_3")
        self.horizontalLayout_7.addWidget(self.map_out_3)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_7)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem8)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem9)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.map_in_4 = QtWidgets.QLineEdit(self.rating_5)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.map_in_4.setFont(font)
        self.map_in_4.setStyleSheet("color: rgb(255, 125, 39)")
        self.map_in_4.setObjectName("map_in_4")
        self.horizontalLayout_9.addWidget(self.map_in_4)
        self.label_4 = QtWidgets.QLabel(self.rating_5)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_9.addWidget(self.label_4)
        self.map_out_4 = QtWidgets.QLineEdit(self.rating_5)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.map_out_4.setFont(font)
        self.map_out_4.setStyleSheet("color: rgb(102, 255, 85);")
        self.map_out_4.setObjectName("map_out_4")
        self.horizontalLayout_9.addWidget(self.map_out_4)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_9)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem10)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem11)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.map_in_5 = QtWidgets.QLineEdit(self.rating_5)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.map_in_5.setFont(font)
        self.map_in_5.setStyleSheet("color: rgb(255, 125, 39)")
        self.map_in_5.setObjectName("map_in_5")
        self.horizontalLayout_11.addWidget(self.map_in_5)
        self.label_5 = QtWidgets.QLabel(self.rating_5)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_11.addWidget(self.label_5)
        self.map_out_5 = QtWidgets.QLineEdit(self.rating_5)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.map_out_5.setFont(font)
        self.map_out_5.setStyleSheet("color: rgb(102, 255, 85);")
        self.map_out_5.setObjectName("map_out_5")
        self.horizontalLayout_11.addWidget(self.map_out_5)
        self.horizontalLayout_10.addLayout(self.horizontalLayout_11)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem12)
        self.verticalLayout_2.addLayout(self.horizontalLayout_10)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem13, 1, 0, 1, 1)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/rating-5.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.rating_5, icon1, "")
        self.rating_3 = QtWidgets.QWidget()
        self.rating_3.setObjectName("rating_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.rating_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        spacerItem14 = QtWidgets.QSpacerItem(96, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_25.addItem(spacerItem14)
        self.my_label_1 = QtWidgets.QLabel(self.rating_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.my_label_1.setFont(font)
        self.my_label_1.setStyleSheet("color: rgb(100, 62, 255);")
        self.my_label_1.setObjectName("my_label_1")
        self.horizontalLayout_25.addWidget(self.my_label_1)
        spacerItem15 = QtWidgets.QSpacerItem(95, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_25.addItem(spacerItem15)
        self.my_label_2 = QtWidgets.QLabel(self.rating_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.my_label_2.setFont(font)
        self.my_label_2.setStyleSheet("color: rgb(100, 62, 255);")
        self.my_label_2.setObjectName("my_label_2")
        self.horizontalLayout_25.addWidget(self.my_label_2)
        spacerItem16 = QtWidgets.QSpacerItem(96, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_25.addItem(spacerItem16)
        self.verticalLayout_4.addLayout(self.horizontalLayout_25)
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_26.addItem(spacerItem17)
        self.horizontalLayout_27 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")
        self.map_in_11 = QtWidgets.QLineEdit(self.rating_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.map_in_11.setFont(font)
        self.map_in_11.setStyleSheet("color: rgb(255, 125, 39)")
        self.map_in_11.setObjectName("map_in_11")
        self.horizontalLayout_27.addWidget(self.map_in_11)
        self.label_19 = QtWidgets.QLabel(self.rating_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_27.addWidget(self.label_19)
        self.map_out_11 = QtWidgets.QLineEdit(self.rating_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.map_out_11.setFont(font)
        self.map_out_11.setStyleSheet("color: rgb(102, 255, 85);")
        self.map_out_11.setObjectName("map_out_11")
        self.horizontalLayout_27.addWidget(self.map_out_11)
        self.horizontalLayout_26.addLayout(self.horizontalLayout_27)
        spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_26.addItem(spacerItem18)
        self.verticalLayout_4.addLayout(self.horizontalLayout_26)
        self.horizontalLayout_28 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_28.setObjectName("horizontalLayout_28")
        spacerItem19 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_28.addItem(spacerItem19)
        self.horizontalLayout_29 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_29.setObjectName("horizontalLayout_29")
        self.map_in_12 = QtWidgets.QLineEdit(self.rating_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.map_in_12.setFont(font)
        self.map_in_12.setStyleSheet("color: rgb(255, 125, 39)")
        self.map_in_12.setObjectName("map_in_12")
        self.horizontalLayout_29.addWidget(self.map_in_12)
        self.label_20 = QtWidgets.QLabel(self.rating_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_29.addWidget(self.label_20)
        self.map_out_12 = QtWidgets.QLineEdit(self.rating_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.map_out_12.setFont(font)
        self.map_out_12.setStyleSheet("color: rgb(102, 255, 85);")
        self.map_out_12.setObjectName("map_out_12")
        self.horizontalLayout_29.addWidget(self.map_out_12)
        self.horizontalLayout_28.addLayout(self.horizontalLayout_29)
        spacerItem20 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_28.addItem(spacerItem20)
        self.verticalLayout_4.addLayout(self.horizontalLayout_28)
        self.horizontalLayout_30 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_30.setObjectName("horizontalLayout_30")
        spacerItem21 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_30.addItem(spacerItem21)
        self.horizontalLayout_31 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_31.setObjectName("horizontalLayout_31")
        self.map_in_13 = QtWidgets.QLineEdit(self.rating_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.map_in_13.setFont(font)
        self.map_in_13.setStyleSheet("color: rgb(255, 125, 39)")
        self.map_in_13.setObjectName("map_in_13")
        self.horizontalLayout_31.addWidget(self.map_in_13)
        self.label_21 = QtWidgets.QLabel(self.rating_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_31.addWidget(self.label_21)
        self.map_out_13 = QtWidgets.QLineEdit(self.rating_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.map_out_13.setFont(font)
        self.map_out_13.setStyleSheet("color: rgb(102, 255, 85);")
        self.map_out_13.setObjectName("map_out_13")
        self.horizontalLayout_31.addWidget(self.map_out_13)
        self.horizontalLayout_30.addLayout(self.horizontalLayout_31)
        spacerItem22 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_30.addItem(spacerItem22)
        self.verticalLayout_4.addLayout(self.horizontalLayout_30)
        self.gridLayout_4.addLayout(self.verticalLayout_4, 0, 0, 1, 1)
        spacerItem23 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem23, 1, 0, 1, 1)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/rating-3.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.rating_3, icon2, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem24 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem24)
        self.map_ok_button = QtWidgets.QPushButton(Setting)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/ok.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.map_ok_button.setIcon(icon3)
        self.map_ok_button.setObjectName("map_ok_button")
        self.horizontalLayout.addWidget(self.map_ok_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Setting)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Setting)

    def retranslateUi(self, Setting):
        _translate = QtCore.QCoreApplication.translate
        Setting.setWindowTitle(_translate("Setting", "Settings"))
        self.my_label_3.setText(_translate("Setting", "Input values"))
        self.my_label_4.setText(_translate("Setting", "Map values"))
        self.label.setText(_translate("Setting", "  :  "))
        self.label_2.setText(_translate("Setting", "  :  "))
        self.label_3.setText(_translate("Setting", "  :  "))
        self.label_4.setText(_translate("Setting", "  :  "))
        self.label_5.setText(_translate("Setting", "  :  "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.rating_5), _translate("Setting", "Five set rating"))
        self.my_label_1.setText(_translate("Setting", "Input values"))
        self.my_label_2.setText(_translate("Setting", "Map values"))
        self.label_19.setText(_translate("Setting", "  :  "))
        self.label_20.setText(_translate("Setting", "  :  "))
        self.label_21.setText(_translate("Setting", "  :  "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.rating_3), _translate("Setting", "Three set rating"))
        self.map_ok_button.setText(_translate("Setting", "Ok"))