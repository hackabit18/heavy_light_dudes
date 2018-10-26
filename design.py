# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(651, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.formLayout = QtGui.QFormLayout(self.centralwidget)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.logTB = QtGui.QPlainTextEdit(self.centralwidget)
        self.logTB.setReadOnly(True)
        self.logTB.setObjectName(_fromUtf8("logTB"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.FieldRole, self.logTB)
        self.languageCombo = QtGui.QComboBox(self.centralwidget)
        self.languageCombo.setObjectName(_fromUtf8("languageCombo"))
        self.languageCombo.addItem(_fromUtf8(""))
        self.languageCombo.addItem(_fromUtf8(""))
        self.formLayout.setWidget(9, QtGui.QFormLayout.FieldRole, self.languageCombo)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(9, QtGui.QFormLayout.LabelRole, self.label_4)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.LabelRole, self.label_3)
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(10, QtGui.QFormLayout.LabelRole, self.label_5)
        self.versionCombo = QtGui.QComboBox(self.centralwidget)
        self.versionCombo.setObjectName(_fromUtf8("versionCombo"))
        self.formLayout.setWidget(10, QtGui.QFormLayout.FieldRole, self.versionCombo)
        self.compileB = QtGui.QPushButton(self.centralwidget)
        self.compileB.setObjectName(_fromUtf8("compileB"))
        self.formLayout.setWidget(16, QtGui.QFormLayout.FieldRole, self.compileB)
        self.statB = QtGui.QPushButton(self.centralwidget)
        self.statB.setObjectName(_fromUtf8("statB"))
        self.formLayout.setWidget(19, QtGui.QFormLayout.FieldRole, self.statB)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setScaledContents(False)
        self.label.setWordWrap(False)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.label)
        self.openB = QtGui.QPushButton(self.centralwidget)
        self.openB.setObjectName(_fromUtf8("openB"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.openB)
        self.listWidget = QtGui.QListWidget(self.centralwidget)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.listWidget)
        self.codeTB = QtGui.QPlainTextEdit(self.centralwidget)
        self.codeTB.setObjectName(_fromUtf8("codeTB"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.codeTB)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 651, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.languageCombo.setItemText(0, _translate("MainWindow", "C/C++", None))
        self.languageCombo.setItemText(1, _translate("MainWindow", "Python", None))
        self.label_4.setText(_translate("MainWindow", "Select Language", None))
        self.label_3.setText(_translate("MainWindow", "Logs", None))
        self.label_5.setText(_translate("MainWindow", "Which Version?", None))
        self.compileB.setText(_translate("MainWindow", "Compiles", None))
        self.statB.setText(_translate("MainWindow", "Static Analysis", None))
        self.label.setText(_translate("MainWindow", "Code", None))
        self.openB.setText(_translate("MainWindow", "Open File", None))

