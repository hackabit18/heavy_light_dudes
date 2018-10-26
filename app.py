from PyQt4 import QtGui
import sys
import design
import os
import docker 
import compilers
from buildImage import basicImage

client = docker.from_env()

class CTP(QtGui.QMainWindow, design.Ui_MainWindow):
    def __init__(self, parent=None):
        super(CTP, self).__init__(parent)
        self.setupUi(self)
        self.openB.clicked.connect(self.browse_folder)  # When the button is pressed
                                                            # Execute browse_folder function
        self.listWidget.itemActivated.connect(self.selectFile)
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
    	srcCode = srcFile.read()
    	self.codeTB.insertPlainText(srcCode)


def main():

    basicImage()                      # function to create required images on user's system

    app = QtGui.QApplication(sys.argv)
    form = CTP()
    form.show()

    # Init code to be added here:
    app.exec_()


if __name__ == '__main__':
    main()