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
        MainWindow.resize(557, 447)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.formLayout = QtGui.QFormLayout(self.centralwidget)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.openB = QtGui.QPushButton(self.centralwidget)
        self.openB.setObjectName(_fromUtf8("openB"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.openB)
        self.srcL = QtGui.QLabel(self.centralwidget)
        self.srcL.setObjectName(_fromUtf8("srcL"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.srcL)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.label_3)
        self.testB = QtGui.QPushButton(self.centralwidget)
        self.testB.setObjectName(_fromUtf8("testB"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.testB)
        self.testL = QtGui.QLabel(self.centralwidget)
        self.testL.setObjectName(_fromUtf8("testL"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.testL)
        self.logTB = QtGui.QPlainTextEdit(self.centralwidget)
        self.logTB.setReadOnly(True)
        self.logTB.setObjectName(_fromUtf8("logTB"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.logTB)
        self.runB = QtGui.QPushButton(self.centralwidget)
        self.runB.setObjectName(_fromUtf8("runB"))
        self.formLayout.setWidget(16, QtGui.QFormLayout.FieldRole, self.runB)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 557, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.openB.setText(_translate("MainWindow", "Browse Project", None))
        self.srcL.setText(_translate("MainWindow", "No Project Selected", None))
        self.label_3.setText(_translate("MainWindow", "Logs", None))
        self.testB.setText(_translate("MainWindow", "Browse Tests", None))
        self.testL.setText(_translate("MainWindow", "No Tests Selected", None))
        self.runB.setText(_translate("MainWindow", "Run Tests", None))

