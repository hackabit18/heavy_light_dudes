from PyQt4 import QtGui
import sys
import design
import os
from buildImage import basicImage
import compileSource
import staticTesting
import time

class CTP(QtGui.QMainWindow, design.Ui_MainWindow):
    def __init__(self, parent=None):
        super(CTP, self).__init__(parent)
        self.setupUi(self)
        self.items = {'C++':['98','03','11','14','17'], 'Python':['Python-2', 'Python-3'], 'Java':['7', '8', '9']} # Mapping for listing versions
        self.openB.clicked.connect(self.browse_folder)  # When the button is pressed
                                                        # Execute browse_folder function
        self.listWidget.itemActivated.connect(self.selectFile) #browse and select file
        self.languageCombo.activated[str].connect(self.onComboActivated)
        self.compileB.clicked.connect(self.compileSrc)  # Compile Button
        self.statB.clicked.connect(self.staticAnalyse)  # Static Button

    def browse_folder(self):
        self.listWidget.clear() # In case there are any existing elements in the list
        self.directory = QtGui.QFileDialog.getExistingDirectory(self,"Pick a folder")
        # execute getExistingDirectory dialog and set the directory variable to be equal
        # to the user selected directory

        if self.directory: # if user didn't pick a directory don't continue
            for file_name in os.listdir(self.directory): # for all files, if any, in the directory
                self.listWidget.addItem(file_name)  # add file to the listWidget
    
    def selectFile(self, listItem):
        self.codeTB.clear()
        self.fileName = listItem.text()
        srcPath = self.directory + '/' + self.fileName
        srcFile = open(srcPath, 'r', encoding = 'utf-8')
        srcCode = srcFile.read()
        srcFile.close()
        self.codeTB.insertPlainText(srcCode)
    
    def onComboActivated(self, text):
        self.versionCombo.clear()
        self.versionCombo.addItems(self.items[text])
    
    def compileSrc(self):
        lang = str(self.languageCombo.currentText())
        versn = str(self.versionCombo.currentText())
        if lang == 'C++':
            compileSource.compileSrcCpp(versn, self.codeTB.toPlainText())
        elif lang == 'Python':
            pass
        elif lang == 'Java':
        	compileSource.compileSrcJava(versn, self.codeTB.toPlainText(), self.fileName)

        srcPath = os.getcwd() + '/tmp/out.txt'            
        file = open(srcPath ,'r', encoding = 'utf-8')
        logs = file.read()
        file.close()
        self.logTB.clear()
        if logs == "" :
            self.logTB.insertPlainText("Compiled Successfully")
        else:
            self.logTB.insertPlainText(logs)


    def staticAnalyse(self):
        lang = str(self.languageCombo.currentText())
        if lang == 'C++' :
            staticTesting.staticTestCpp(self.codeTB.toPlainText())        
        if lang == 'Python':
            staticTesting.staticTestPy(self.codeTB.toPlainText())
        srcPath = os.getcwd() + '/tmp/staticOutput.txt'
        file = open(srcPath, 'r', encoding = 'utf-8')
        logs = file.read()
        file.close()
        self.logTB.clear()
        self.logTB.insertPlainText(logs)







def main():

    basicImage()                      # function to create required images on user's system

    app = QtGui.QApplication(sys.argv)
    form = CTP()
    form.show()

    # Init code to be added here:
    # Make Images
    app.exec_()


if __name__ == '__main__':
    main()