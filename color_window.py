# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'color_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ColorPicker(object):
    def setupUi(self, ColorPicker):
        ColorPicker.setObjectName("ColorPicker")
        ColorPicker.resize(299, 334)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ColorPicker.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(ColorPicker)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(ColorPicker)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.color1_button = QtWidgets.QPushButton(self.groupBox)
        self.color1_button.setText("")
        self.color1_button.setObjectName("color1_button")
        self.horizontalLayout.addWidget(self.color1_button)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_9.addWidget(self.label_9)
        self.color2_button = QtWidgets.QPushButton(self.groupBox)
        self.color2_button.setText("")
        self.color2_button.setObjectName("color2_button")
        self.horizontalLayout_9.addWidget(self.color2_button)
        self.gridLayout_2.addLayout(self.horizontalLayout_9, 1, 0, 1, 1)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_10.addWidget(self.label_10)
        self.color3_button = QtWidgets.QPushButton(self.groupBox)
        self.color3_button.setText("")
        self.color3_button.setObjectName("color3_button")
        self.horizontalLayout_10.addWidget(self.color3_button)
        self.gridLayout_2.addLayout(self.horizontalLayout_10, 2, 0, 1, 1)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_11.addWidget(self.label_11)
        self.color4_button = QtWidgets.QPushButton(self.groupBox)
        self.color4_button.setText("")
        self.color4_button.setObjectName("color4_button")
        self.horizontalLayout_11.addWidget(self.color4_button)
        self.gridLayout_2.addLayout(self.horizontalLayout_11, 3, 0, 1, 1)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_12.addWidget(self.label_12)
        self.color5_button = QtWidgets.QPushButton(self.groupBox)
        self.color5_button.setText("")
        self.color5_button.setObjectName("color5_button")
        self.horizontalLayout_12.addWidget(self.color5_button)
        self.gridLayout_2.addLayout(self.horizontalLayout_12, 4, 0, 1, 1)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_13 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_13.addWidget(self.label_13)
        self.color6_button = QtWidgets.QPushButton(self.groupBox)
        self.color6_button.setText("")
        self.color6_button.setObjectName("color6_button")
        self.horizontalLayout_13.addWidget(self.color6_button)
        self.gridLayout_2.addLayout(self.horizontalLayout_13, 5, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem)
        self.close_color_picker = QtWidgets.QPushButton(ColorPicker)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/ok.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.close_color_picker.setIcon(icon1)
        self.close_color_picker.setObjectName("close_color_picker")
        self.horizontalLayout_14.addWidget(self.close_color_picker)
        self.verticalLayout.addLayout(self.horizontalLayout_14)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(ColorPicker)
        QtCore.QMetaObject.connectSlotsByName(ColorPicker)

    def retranslateUi(self, ColorPicker):
        _translate = QtCore.QCoreApplication.translate
        ColorPicker.setWindowTitle(_translate("ColorPicker", "Form"))
        self.groupBox.setTitle(_translate("ColorPicker", "Pick you colors"))
        self.label.setText(_translate("ColorPicker", "Color 1"))
        self.label_9.setText(_translate("ColorPicker", "Color 2"))
        self.label_10.setText(_translate("ColorPicker", "Color 3"))
        self.label_11.setText(_translate("ColorPicker", "Color 4"))
        self.label_12.setText(_translate("ColorPicker", "Color 5"))
        self.label_13.setText(_translate("ColorPicker", "Color 6"))
        self.close_color_picker.setText(_translate("ColorPicker", "Ok"))
