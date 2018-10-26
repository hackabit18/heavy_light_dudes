import os
import docker
def compileSrcCpp(versn, fileString):
	srcPath = os.getcwd() + '/tmp'
	file = open(srcPath + '/in.cpp','w', encoding = 'utf-8')
	print(srcPath)
	file.write(fileString)
	file.close()
	client = docker.from_env()
	containerObj = client.containers.run(image="ctp1", command=["/bin/bash", "-c", "cd /tmp; g++ -std=c++{} in.cpp 2> out.txt".format(versn)], volumes={srcPath:{'bind': '/tmp', 'mode':'rw'}}, detach = True, remove=True)
	srcPath = os.getcwd() + '/tmp/out.txt'
	print(srcPath)
	file1 = open(srcPath ,'r')
	file1.seek(0)	
	logs = file1.read()
	print(logs)
	file1.close()
