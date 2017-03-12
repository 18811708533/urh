# -*- coding: utf-8 -*-

#
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DialogOptions(object):
    def setupUi(self, DialogOptions):
        DialogOptions.setObjectName("DialogOptions")
        DialogOptions.resize(953, 653)
        self.horizontalLayout = QtWidgets.QHBoxLayout(DialogOptions)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(DialogOptions)
        self.tabWidget.setObjectName("tabWidget")
        self.tabInterpretation = QtWidgets.QWidget()
        self.tabInterpretation.setObjectName("tabInterpretation")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tabInterpretation)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.tabInterpretation)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.spinBoxSymbolTreshold = QtWidgets.QSpinBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBoxSymbolTreshold.sizePolicy().hasHeightForWidth())
        self.spinBoxSymbolTreshold.setSizePolicy(sizePolicy)
        self.spinBoxSymbolTreshold.setMaximum(50)
        self.spinBoxSymbolTreshold.setObjectName("spinBoxSymbolTreshold")
        self.gridLayout.addWidget(self.spinBoxSymbolTreshold, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.lSymbolLength = QtWidgets.QLabel(self.groupBox)
        self.lSymbolLength.setObjectName("lSymbolLength")
        self.gridLayout.addWidget(self.lSymbolLength, 2, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 2, 1, 1)
        self.chkBoxEnableSymbols = QtWidgets.QCheckBox(self.groupBox)
        self.chkBoxEnableSymbols.setObjectName("chkBoxEnableSymbols")
        self.gridLayout.addWidget(self.chkBoxEnableSymbols, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.lExplanation = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lExplanation.setFont(font)
        self.lExplanation.setWordWrap(True)
        self.lExplanation.setObjectName("lExplanation")
        self.verticalLayout.addWidget(self.lExplanation)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.tabWidget.addTab(self.tabInterpretation, "")
        self.tabGeneration = QtWidgets.QWidget()
        self.tabGeneration.setObjectName("tabGeneration")
        self.layoutWidget = QtWidgets.QWidget(self.tabGeneration)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 20, 299, 53))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.checkBoxDefaultFuzzingPause = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBoxDefaultFuzzingPause.setObjectName("checkBoxDefaultFuzzingPause")
        self.gridLayout_4.addWidget(self.checkBoxDefaultFuzzingPause, 0, 0, 1, 2)
        self.doubleSpinBoxFuzzingPause = KillerDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBoxFuzzingPause.setDecimals(3)
        self.doubleSpinBoxFuzzingPause.setMaximum(999999999.0)
        self.doubleSpinBoxFuzzingPause.setObjectName("doubleSpinBoxFuzzingPause")
        self.gridLayout_4.addWidget(self.doubleSpinBoxFuzzingPause, 1, 0, 1, 1)
        self.labelFuzzingSamples = QtWidgets.QLabel(self.layoutWidget)
        self.labelFuzzingSamples.setObjectName("labelFuzzingSamples")
        self.gridLayout_4.addWidget(self.labelFuzzingSamples, 1, 1, 1, 1)
        self.tabWidget.addTab(self.tabGeneration, "")
        self.tabView = QtWidgets.QWidget()
        self.tabView.setObjectName("tabView")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tabView)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_7 = QtWidgets.QLabel(self.tabView)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_2.addWidget(self.label_7)
        self.comboBoxDefaultView = QtWidgets.QComboBox(self.tabView)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxDefaultView.sizePolicy().hasHeightForWidth())
        self.comboBoxDefaultView.setSizePolicy(sizePolicy)
        self.comboBoxDefaultView.setObjectName("comboBoxDefaultView")
        self.comboBoxDefaultView.addItem("")
        self.comboBoxDefaultView.addItem("")
        self.comboBoxDefaultView.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBoxDefaultView)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.checkBoxShowConfirmCloseDialog = QtWidgets.QCheckBox(self.tabView)
        self.checkBoxShowConfirmCloseDialog.setObjectName("checkBoxShowConfirmCloseDialog")
        self.verticalLayout_4.addWidget(self.checkBoxShowConfirmCloseDialog)
        self.checkBoxHoldShiftToDrag = QtWidgets.QCheckBox(self.tabView)
        self.checkBoxHoldShiftToDrag.setObjectName("checkBoxHoldShiftToDrag")
        self.verticalLayout_4.addWidget(self.checkBoxHoldShiftToDrag)
        self.checkBoxPauseTime = QtWidgets.QCheckBox(self.tabView)
        self.checkBoxPauseTime.setObjectName("checkBoxPauseTime")
        self.verticalLayout_4.addWidget(self.checkBoxPauseTime)
        self.checkBoxAlignLabels = QtWidgets.QCheckBox(self.tabView)
        self.checkBoxAlignLabels.setObjectName("checkBoxAlignLabels")
        self.verticalLayout_4.addWidget(self.checkBoxAlignLabels)
        self.checkBoxFallBackTheme = QtWidgets.QCheckBox(self.tabView)
        self.checkBoxFallBackTheme.setObjectName("checkBoxFallBackTheme")
        self.verticalLayout_4.addWidget(self.checkBoxFallBackTheme)
        spacerItem2 = QtWidgets.QSpacerItem(20, 383, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem2)
        self.tabWidget.addTab(self.tabView, "")
        self.tabFieldtypes = QtWidgets.QWidget()
        self.tabFieldtypes.setObjectName("tabFieldtypes")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tabFieldtypes)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.tblLabeltypes = QtWidgets.QTableView(self.tabFieldtypes)
        self.tblLabeltypes.setAlternatingRowColors(True)
        self.tblLabeltypes.setObjectName("tblLabeltypes")
        self.horizontalLayout_3.addWidget(self.tblLabeltypes)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.btnAddLabelType = QtWidgets.QToolButton(self.tabFieldtypes)
        icon = QtGui.QIcon.fromTheme("list-add")
        self.btnAddLabelType.setIcon(icon)
        self.btnAddLabelType.setObjectName("btnAddLabelType")
        self.verticalLayout_3.addWidget(self.btnAddLabelType)
        self.btnRemoveLabeltype = QtWidgets.QToolButton(self.tabFieldtypes)
        icon = QtGui.QIcon.fromTheme("list-remove")
        self.btnRemoveLabeltype.setIcon(icon)
        self.btnRemoveLabeltype.setObjectName("btnRemoveLabeltype")
        self.verticalLayout_3.addWidget(self.btnRemoveLabeltype)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem3)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        spacerItem4 = QtWidgets.QSpacerItem(20, 203, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem4)
        self.tabWidget.addTab(self.tabFieldtypes, "")
        self.tab_plugins = QtWidgets.QWidget()
        self.tab_plugins.setObjectName("tab_plugins")
        self.tabWidget.addTab(self.tab_plugins, "")
        self.tabDevices = QtWidgets.QWidget()
        self.tabDevices.setObjectName("tabDevices")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tabDevices)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.listWidgetDevices = QtWidgets.QListWidget(self.tabDevices)
        self.listWidgetDevices.setObjectName("listWidgetDevices")
        self.gridLayout_3.addWidget(self.listWidgetDevices, 0, 0, 3, 2)
        self.chkBoxDeviceEnabled = QtWidgets.QCheckBox(self.tabDevices)
        self.chkBoxDeviceEnabled.setObjectName("chkBoxDeviceEnabled")
        self.gridLayout_3.addWidget(self.chkBoxDeviceEnabled, 0, 2, 1, 1)
        self.rbNativeBackend = QtWidgets.QRadioButton(self.tabDevices)
        self.rbNativeBackend.setObjectName("rbNativeBackend")
        self.gridLayout_3.addWidget(self.rbNativeBackend, 1, 2, 1, 1)
        self.rbGnuradioBackend = QtWidgets.QRadioButton(self.tabDevices)
        self.rbGnuradioBackend.setObjectName("rbGnuradioBackend")
        self.gridLayout_3.addWidget(self.rbGnuradioBackend, 2, 2, 1, 1)
        self.lSupport = QtWidgets.QLabel(self.tabDevices)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lSupport.sizePolicy().hasHeightForWidth())
        self.lSupport.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lSupport.setFont(font)
        self.lSupport.setStyleSheet("color: green")
        self.lSupport.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lSupport.setObjectName("lSupport")
        self.gridLayout_3.addWidget(self.lSupport, 3, 0, 1, 2)
        self.line = QtWidgets.QFrame(self.tabDevices)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_3.addWidget(self.line, 5, 0, 1, 3)
        self.label_8 = QtWidgets.QLabel(self.tabDevices)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 7, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.tabDevices)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_3.addWidget(self.line_2, 9, 0, 1, 3)
        self.groupBox_3 = QtWidgets.QGroupBox(self.tabDevices)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_11 = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 0, 0, 1, 2)
        self.lineEditPython2Interpreter = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEditPython2Interpreter.setObjectName("lineEditPython2Interpreter")
        self.gridLayout_2.addWidget(self.lineEditPython2Interpreter, 1, 1, 1, 1)
        self.lGnuradioInstalled = QtWidgets.QLabel(self.groupBox_3)
        self.lGnuradioInstalled.setStyleSheet("")
        self.lGnuradioInstalled.setObjectName("lGnuradioInstalled")
        self.gridLayout_2.addWidget(self.lGnuradioInstalled, 3, 0, 1, 2)
        self.lineEditGnuradioDirectory = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEditGnuradioDirectory.setEnabled(True)
        self.lineEditGnuradioDirectory.setObjectName("lineEditGnuradioDirectory")
        self.gridLayout_2.addWidget(self.lineEditGnuradioDirectory, 2, 1, 1, 1)
        self.radioButtonPython2Interpreter = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButtonPython2Interpreter.setObjectName("radioButtonPython2Interpreter")
        self.gridLayout_2.addWidget(self.radioButtonPython2Interpreter, 1, 0, 1, 1)
        self.radioButtonGnuradioDirectory = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButtonGnuradioDirectory.setObjectName("radioButtonGnuradioDirectory")
        self.gridLayout_2.addWidget(self.radioButtonGnuradioDirectory, 2, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_3, 10, 0, 1, 2)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem5, 11, 1, 1, 1)
        self.labelWindowsError = QtWidgets.QLabel(self.tabDevices)
        self.labelWindowsError.setWordWrap(True)
        self.labelWindowsError.setObjectName("labelWindowsError")
        self.gridLayout_3.addWidget(self.labelWindowsError, 4, 0, 1, 2)
        self.label_5 = QtWidgets.QLabel(self.tabDevices)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 8, 0, 1, 1)
        self.doubleSpinBoxRAMThreshold = QtWidgets.QDoubleSpinBox(self.tabDevices)
        self.doubleSpinBoxRAMThreshold.setMinimum(1.0)
        self.doubleSpinBoxRAMThreshold.setMaximum(100.0)
        self.doubleSpinBoxRAMThreshold.setObjectName("doubleSpinBoxRAMThreshold")
        self.gridLayout_3.addWidget(self.doubleSpinBoxRAMThreshold, 8, 1, 1, 2)
        self.spinBoxNumSendingRepeats = QtWidgets.QSpinBox(self.tabDevices)
        self.spinBoxNumSendingRepeats.setProperty("showGroupSeparator", False)
        self.spinBoxNumSendingRepeats.setMaximum(999999999)
        self.spinBoxNumSendingRepeats.setDisplayIntegerBase(10)
        self.spinBoxNumSendingRepeats.setObjectName("spinBoxNumSendingRepeats")
        self.gridLayout_3.addWidget(self.spinBoxNumSendingRepeats, 7, 1, 1, 2)
        self.tabWidget.addTab(self.tabDevices, "")
        self.horizontalLayout.addWidget(self.tabWidget)

        self.retranslateUi(DialogOptions)
        self.tabWidget.setCurrentIndex(5)
        QtCore.QMetaObject.connectSlotsByName(DialogOptions)

    def retranslateUi(self, DialogOptions):
        _translate = QtCore.QCoreApplication.translate
        DialogOptions.setWindowTitle(_translate("DialogOptions", "Options"))
        self.groupBox.setTitle(_translate("DialogOptions", "Symbols"))
        self.label.setText(_translate("DialogOptions", "Some protocols use different information lengths. This can be part of the protocol logic (e.g. to indicate a SOF). You can set a tolerance window for the selected bit length, outside the window a new symbol will be created."))
        self.label_2.setText(_translate("DialogOptions", "Tolerance window:"))
        self.spinBoxSymbolTreshold.setSuffix(_translate("DialogOptions", "%"))
        self.label_3.setText(_translate("DialogOptions", "of selected bit length"))
        self.label_4.setText(_translate("DialogOptions", "Relative symbol length:"))
        self.lSymbolLength.setText(_translate("DialogOptions", "0%"))
        self.label_6.setText(_translate("DialogOptions", "of selected bit length"))
        self.chkBoxEnableSymbols.setText(_translate("DialogOptions", "Enable symbols"))
        self.lExplanation.setText(_translate("DialogOptions", "No Symbols will be created"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabInterpretation), _translate("DialogOptions", "Interpretation"))
        self.checkBoxDefaultFuzzingPause.setToolTip(_translate("DialogOptions", "<html><head/><body><p>If you disable the default pause, the pause of the fuzzed message will be used.</p></body></html>"))
        self.checkBoxDefaultFuzzingPause.setText(_translate("DialogOptions", "Use a default pause for fuzzed messages"))
        self.labelFuzzingSamples.setText(_translate("DialogOptions", "Samples"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabGeneration), _translate("DialogOptions", "Generation"))
        self.label_7.setText(_translate("DialogOptions", "Default View:"))
        self.comboBoxDefaultView.setItemText(0, _translate("DialogOptions", "Bit"))
        self.comboBoxDefaultView.setItemText(1, _translate("DialogOptions", "Hex"))
        self.comboBoxDefaultView.setItemText(2, _translate("DialogOptions", "ASCII"))
        self.checkBoxShowConfirmCloseDialog.setText(_translate("DialogOptions", "Show \"confirm close\" dialog"))
        self.checkBoxHoldShiftToDrag.setText(_translate("DialogOptions", "Hold shift to drag"))
        self.checkBoxPauseTime.setText(_translate("DialogOptions", "Show pauses as time"))
        self.checkBoxAlignLabels.setText(_translate("DialogOptions", "Align on labels"))
        self.checkBoxFallBackTheme.setToolTip(_translate("DialogOptions", "Tick this option if you experience problems with you current Qt theme like no colors in table headers."))
        self.checkBoxFallBackTheme.setText(_translate("DialogOptions", "Use fallback application theme [RESTART REQUIRED]"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabView), _translate("DialogOptions", "View"))
        self.btnAddLabelType.setText(_translate("DialogOptions", "..."))
        self.btnRemoveLabeltype.setText(_translate("DialogOptions", "..."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabFieldtypes), _translate("DialogOptions", "Fieldtypes"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_plugins), _translate("DialogOptions", "Plugins"))
        self.chkBoxDeviceEnabled.setText(_translate("DialogOptions", "Enabled"))
        self.rbNativeBackend.setText(_translate("DialogOptions", "Native backend (recommended)"))
        self.rbGnuradioBackend.setText(_translate("DialogOptions", "Gnuradio backend"))
        self.lSupport.setText(_translate("DialogOptions", "device supports sending and receiving"))
        self.label_8.setText(_translate("DialogOptions", "Default sending repititions:"))
        self.groupBox_3.setTitle(_translate("DialogOptions", "Gnuradio options"))
        self.label_11.setText(_translate("DialogOptions", "Needed for Gnuradio backend only"))
        self.lineEditPython2Interpreter.setToolTip(_translate("DialogOptions", "<html><head/><body><p>Use this option if you installed Gnuradio with your package manager e.g. on Linux and Mac OS X.</p></body></html>"))
        self.lineEditPython2Interpreter.setPlaceholderText(_translate("DialogOptions", "/usr/bin/python2"))
        self.lGnuradioInstalled.setText(_translate("DialogOptions", "Gnuradio installation found"))
        self.lineEditGnuradioDirectory.setToolTip(_translate("DialogOptions", "<html><head/><body><p>If you installed Gnuradio with a bundled python interpreter, you need to enter the site-packages path of the installation here. The path should be something like <span style=\" font-style:italic;\">C:\\Program Files\\GNURadio-3.7</span>.</p></body></html>"))
        self.lineEditGnuradioDirectory.setPlaceholderText(_translate("DialogOptions", "C:\\...\\Gnuradio"))
        self.radioButtonPython2Interpreter.setToolTip(_translate("DialogOptions", "<html><head/><body><p>Use this option if you installed Gnuradio with your package manager e.g. on Linux and Mac OS X.</p></body></html>"))
        self.radioButtonPython2Interpreter.setText(_translate("DialogOptions", "Python2 interpreter"))
        self.radioButtonGnuradioDirectory.setToolTip(_translate("DialogOptions", "<html><head/><body><p>If you installed Gnuradio with a bundled python interpreter, you need to enter the site-packages path of the installation here. The path should be something like <span style=\" font-style:italic;\">C:\\Program Files\\GNURadio-3.7</span>.</p></body></html>"))
        self.radioButtonGnuradioDirectory.setText(_translate("DialogOptions", "Gnuradio Directory"))
        self.labelWindowsError.setText(_translate("DialogOptions", "<html><head/><body><p><span style=\" color:#ff0000;\">Detected a 32 bit installation of python 3.</span> Install <span style=\" font-weight:600;\">64 bit version</span> to use native backends.</p></body></html>"))
        self.label_5.setText(_translate("DialogOptions", "Use this percentage of available RAM for buffer allocation:"))
        self.doubleSpinBoxRAMThreshold.setSuffix(_translate("DialogOptions", "%"))
        self.spinBoxNumSendingRepeats.setSpecialValueText(_translate("DialogOptions", "Infinite"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabDevices), _translate("DialogOptions", "Device"))

from urh.ui.KillerDoubleSpinBox import KillerDoubleSpinBox
