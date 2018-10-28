from PyQt4 import QtGui
import sys
import design
import os
import time
import compileSource
from buildImage import basicImage
class CTP(QtGui.QMainWindow, design.Ui_MainWindow):
    def __init__(self, parent=None):
        super(CTP, self).__init__(parent)
        self.setupUi(self)
        self.items = {'C++':['98','03','11','14','17'], 'Python':['Python-2', 'Python-3'], 'Java':['7', '8', '9']} # Mapping for listing versions
        self.openB.clicked.connect(self.selectFolder)  # When the button is pressed
                                                        # Execute browse_folder function
        self.testB.clicked.connect(self.selectTests)
        self.runB.clicked.connect(self.runTests)  # Run tests

    def browse_folder(self):
        directory = str(QtGui.QFileDialog.getExistingDirectory(self, "Select Directory"))
        return directory
        # execute getExistingDirectory dialog and set the directory variable to be equal
        # to the user selected directory
    def selectFolder(self):
        self.srcL.clear()
        srcPath = '"' + self.browse_folder() + '/"*'
        self.srcL.setText(srcPath)
        destDir = '"'+os.getcwd() + '/dfile/node/'+'"'
        os.system('mkdir -p ' + destDir)
        commd = 'cp -rf '+ srcPath + ' ' + destDir
        print("Copying Project")
        os.system(commd)

    def selectTests(self):
        self.testL.clear()
        srcPath = '"' + self.browse_folder() + '/"'
        self.testL.setText(srcPath)
        destDir = '"'+os.getcwd() + '/dfile/'+'"'
        os.system('mkdir -p ' + destDir)
        commd = 'cp -rf '+ srcPath + ' ' + destDir
        print("Copying tests")
        os.system(commd)

    def runTests(self):
    	### to Do
        print('Running Tests')
        basicImage()                      # function to create required images on user's system
        logs = compileSource.compileSrc()
        self.logTB.clear()
        File = open('tmp/out.txt', 'r', encoding = 'utf-8')
        self.logTB.insertPlainText(str(File.read()))
        File.close()

def main():


    app = QtGui.QApplication(sys.argv)
    form = CTP()
    form.show()
    # Init code to be added here:
    # Make Images
    app.exec_()


if __name__ == '__main__':
    main()