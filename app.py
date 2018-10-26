from PyQt4 import QtGui
import sys
import design
import os
import compileSource
class CTP(QtGui.QMainWindow, design.Ui_MainWindow):
    def __init__(self, parent=None):
        super(CTP, self).__init__(parent)
        self.setupUi(self)
        self.items = {'C++':['std98','std03','std11','std14','std17']} # Mapping for listing versions
        self.openB.clicked.connect(self.browse_folder)  # When the button is pressed
                                                        # Execute browse_folder function
        self.listWidget.itemActivated.connect(self.selectFile) #browse and select file
        self.languageCombo.activated[str].connect(self.onComboActivated)
        self.compileB.clicked.connect(self.compileSrc)  # Todo
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
    	srcPath = self.directory + '/' + listItem.text()
    	srcFile = open(srcPath, 'r', encoding = 'utf-8')
    	self.srcCode = srcFile.read()
    	self.codeTB.insertPlainText(srcCode)
    
    def onComboActivated(self, text):
        self.versionCombo.clear()
        self.versionCombo.addItems(self.items[text])
    
    def compileSrc(self):
        lang = str(self.languageCombo.currentText())
        versn = str(self.versionCombo.currentText())
        if lang == 'C++':
            compileSource.compileSrcCpp(versn, self.codeTB.toPlainText())
            self.logTB.clear()
            srcPath = os.getcwd() + '/tmp'
            file = open(srcPath + '/out.txt','r', encoding = 'utf-8')
            logs = file.read()
            self.logTB.insertPlainText(logs)





def main():
    app = QtGui.QApplication(sys.argv)
    form = CTP()
    form.show()
    # Init code to be added here:
    # Make Images
    app.exec_()


if __name__ == '__main__':
    main()