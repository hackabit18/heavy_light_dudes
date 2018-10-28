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
        MainWindow.resize(755, 549)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.openB = QtGui.QPushButton(self.centralwidget)
        self.openB.setObjectName(_fromUtf8("openB"))
        self.gridLayout.addWidget(self.openB, 0, 0, 1, 1)
        self.srcL = QtGui.QLabel(self.centralwidget)
        self.srcL.setObjectName(_fromUtf8("srcL"))
        self.gridLayout.addWidget(self.srcL, 0, 1, 1, 1)
        self.testB = QtGui.QPushButton(self.centralwidget)
        self.testB.setObjectName(_fromUtf8("testB"))
        self.gridLayout.addWidget(self.testB, 1, 0, 1, 1)
        self.testL = QtGui.QLabel(self.centralwidget)
        self.testL.setObjectName(_fromUtf8("testL"))
        self.gridLayout.addWidget(self.testL, 1, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.logTB = QtGui.QPlainTextEdit(self.centralwidget)
        self.logTB.setReadOnly(True)
        self.logTB.setObjectName(_fromUtf8("logTB"))
        self.gridLayout.addWidget(self.logTB, 2, 1, 1, 1)
        self.runB = QtGui.QPushButton(self.centralwidget)
        self.runB.setObjectName(_fromUtf8("runB"))
        self.gridLayout.addWidget(self.runB, 3, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 755, 23))
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
        self.testB.setText(_translate("MainWindow", "Browse Tests", None))
        self.testL.setText(_translate("MainWindow", "No Tests Selected", None))
        self.label_3.setText(_translate("MainWindow", "Logs", None))
        self.runB.setText(_translate("MainWindow", "Run Tests", None))

