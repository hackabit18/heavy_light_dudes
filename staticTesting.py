import os
import docker
def writeStaticFile(containerObj):
	statOut = containerObj.logs(stdout=True,stderr=False).decode('ASCII')
	statError = str(containerObj.logs(stdout=False,stderr=True)).decode('ASCII')
	statOutFile = open('tmp/staticOutput.txt', 'w', encoding = 'utf-8') #StaticTesting Output File
	statOutFile.write(statOut+'\n'+statError)
	statOutFile.close()
def staticTestPy(fileString):
	srcPath = os.getcwd() + '/tmp'
	file = open(srcPath + '/in.py','w+', encoding = 'utf-8')
	file.write(fileString)
	file.close()
	cli = docker.from_env()
	containerObj = cli.containers.run(image = 'ctp2', command=["/bin/bash","-c", "cd /src; pylint in.py > staticOutput.txt"],
				 volumes={srcPath:{'bind':'/src','mode':'rw'}},  detach = True)
	containerObj.wait()
def staticTestCpp(fileString):
	# srcPath is the path of the source file
	# detach = True is necessary for object returning
	srcPath = os.getcwd() + '/tmp'
	file = open(srcPath + '/in.cpp','w+', encoding = 'utf-8')
	file.write(fileString)
	file.close()
	cli = docker.from_env()
	containerObj = cli.containers.run(image = 'ctp3', volumes={srcPath:{'bind':'/src','mode':'rw'}},  detach = True)
	containerObj.wait()
	writeStaticFile(containerObj)
	