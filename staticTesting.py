import os
import docker
def staticTestCpp(fileString):
	# srcPath is the path of the source file
	# detach = True is necessary for object returning
	srcPath = os.getcwd() + '/tmp'
	file = open(srcPath + '/in.cpp','w+', encoding = 'utf-8')
	file.write(fileString)
	file.close()
	cli = docker.from_env()
	containerObj = cli.containers.run('ctp3', volumes={srcPath:{'bind':'/src','mode':'rw'}},  detach = True)
	containerObj.wait()
	statOut = str(containerObj.logs(stdout=True,stderr=False)).strip('b\'\\n')
	statError = str(containerObj.logs(stdout=False,stderr=True)).strip('b"\\n\'')
	statOutFile = open('tmp/staticOutput.txt', 'w', encoding = 'utf-8') #StaticTesting Output File
	statOutFile.write(statOut+'\n'+statError)
	statOutFile.close()
