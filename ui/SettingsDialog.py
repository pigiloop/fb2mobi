# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SettingsDialog.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SettingsDialog(object):
    def setupUi(self, SettingsDialog):
        SettingsDialog.setObjectName("SettingsDialog")
        SettingsDialog.resize(570, 468)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(SettingsDialog)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox = QtWidgets.QGroupBox(SettingsDialog)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 1, 1, 1)
        self.comboProfile = QtWidgets.QComboBox(self.groupBox)
        self.comboProfile.setObjectName("comboProfile")
        self.gridLayout_2.addWidget(self.comboProfile, 1, 0, 1, 1)
        self.comboFormat = QtWidgets.QComboBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboFormat.sizePolicy().hasHeightForWidth())
        self.comboFormat.setSizePolicy(sizePolicy)
        self.comboFormat.setObjectName("comboFormat")
        self.gridLayout_2.addWidget(self.comboFormat, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioHypYes = QtWidgets.QRadioButton(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioHypYes.sizePolicy().hasHeightForWidth())
        self.radioHypYes.setSizePolicy(sizePolicy)
        self.radioHypYes.setObjectName("radioHypYes")
        self.horizontalLayout.addWidget(self.radioHypYes)
        self.radioHypNo = QtWidgets.QRadioButton(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioHypNo.sizePolicy().hasHeightForWidth())
        self.radioHypNo.setSizePolicy(sizePolicy)
        self.radioHypNo.setObjectName("radioHypNo")
        self.horizontalLayout.addWidget(self.radioHypNo)
        self.radioHypProfile = QtWidgets.QRadioButton(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioHypProfile.sizePolicy().hasHeightForWidth())
        self.radioHypProfile.setSizePolicy(sizePolicy)
        self.radioHypProfile.setObjectName("radioHypProfile")
        self.horizontalLayout.addWidget(self.radioHypProfile)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineDestPath = QtWidgets.QLineEdit(self.groupBox)
        self.lineDestPath.setObjectName("lineDestPath")
        self.horizontalLayout_2.addWidget(self.lineDestPath)
        self.btnSelectDestPath = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnSelectDestPath.sizePolicy().hasHeightForWidth())
        self.btnSelectDestPath.setSizePolicy(sizePolicy)
        self.btnSelectDestPath.setObjectName("btnSelectDestPath")
        self.horizontalLayout_2.addWidget(self.btnSelectDestPath)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.checkConvertToSrc = QtWidgets.QCheckBox(self.groupBox)
        self.checkConvertToSrc.setObjectName("checkConvertToSrc")
        self.verticalLayout.addWidget(self.checkConvertToSrc)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(SettingsDialog)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lineKindlePath = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineKindlePath.setObjectName("lineKindlePath")
        self.horizontalLayout_3.addWidget(self.lineKindlePath)
        self.btnSelectKindlePath = QtWidgets.QPushButton(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnSelectKindlePath.sizePolicy().hasHeightForWidth())
        self.btnSelectKindlePath.setSizePolicy(sizePolicy)
        self.btnSelectKindlePath.setObjectName("btnSelectKindlePath")
        self.horizontalLayout_3.addWidget(self.btnSelectKindlePath)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.checkCopyAfterConvert = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkCopyAfterConvert.setObjectName("checkCopyAfterConvert")
        self.verticalLayout_2.addWidget(self.checkCopyAfterConvert)
        self.checkSyncCovers = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkSyncCovers.setObjectName("checkSyncCovers")
        self.verticalLayout_2.addWidget(self.checkSyncCovers)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        spacerItem = QtWidgets.QSpacerItem(20, 22, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.buttonBox = QtWidgets.QDialogButtonBox(SettingsDialog)
        self.buttonBox.setLocale(QtCore.QLocale(QtCore.QLocale.Russian, QtCore.QLocale.Russia))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_3.addWidget(self.buttonBox)

        self.retranslateUi(SettingsDialog)
        self.buttonBox.accepted.connect(SettingsDialog.accept)
        self.buttonBox.rejected.connect(SettingsDialog.reject)
        self.checkConvertToSrc.stateChanged['int'].connect(SettingsDialog.checkConvertToSrcClicked)
        SettingsDialog.accepted.connect(SettingsDialog.closeAccept)
        self.btnSelectDestPath.clicked.connect(SettingsDialog.selectDestPath)
        self.btnSelectKindlePath.clicked.connect(SettingsDialog.selectKindlePath)
        self.checkCopyAfterConvert.stateChanged['int'].connect(SettingsDialog.checkCopyAfterConvertClicked)
        QtCore.QMetaObject.connectSlotsByName(SettingsDialog)

    def retranslateUi(self, SettingsDialog):
        _translate = QtCore.QCoreApplication.translate
        SettingsDialog.setWindowTitle(_translate("SettingsDialog", "Settings"))
        self.groupBox.setTitle(_translate("SettingsDialog", "Converter settings"))
        self.label.setText(_translate("SettingsDialog", "Profile"))
        self.label_2.setText(_translate("SettingsDialog", "Output format"))
        self.groupBox_3.setTitle(_translate("SettingsDialog", "Insert soft hyphens"))
        self.radioHypYes.setText(_translate("SettingsDialog", "Yes"))
        self.radioHypNo.setText(_translate("SettingsDialog", "No"))
        self.radioHypProfile.setText(_translate("SettingsDialog", "Profile default"))
        self.label_3.setText(_translate("SettingsDialog", "Destination folder"))
        self.btnSelectDestPath.setText(_translate("SettingsDialog", "Select"))
        self.checkConvertToSrc.setText(_translate("SettingsDialog", "Save target files in source folder"))
        self.groupBox_2.setTitle(_translate("SettingsDialog", "Kindle"))
        self.label_4.setText(_translate("SettingsDialog", "\"documents\" device folder"))
        self.btnSelectKindlePath.setText(_translate("SettingsDialog", "Select"))
        self.checkCopyAfterConvert.setText(_translate("SettingsDialog", "Copy to device after conversion"))
        self.checkSyncCovers.setText(_translate("SettingsDialog", "Syncronize covers"))

