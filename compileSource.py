import os
import docker
def writeLogsFile(containerObj): # To write container logs to out.txt, remove should be false if you are using this function
	Out = containerObj.logs(stdout=True,stderr=False).decode('ASCII')
	Error = containerObj.logs(stdout=False,stderr=True).decode('ASCII')
	OutFile = open('tmp/out.txt', 'w', encoding = 'utf-8')
#	OutFile.write(Out+'\n'+Error)
	OutFile.write(containerObj.logs().decode('ASCII'))
	OutFile.close()
def compileSrcCpp(versn, fileString):
	srcPath = os.getcwd() + '/tmp'
	file = open(srcPath + '/in.cpp','w+', encoding = 'utf-8')
	file.write(fileString)
	file.close()
	client = docker.from_env()
	containerObj = client.containers.run(image="ctp1", command=["/bin/bash", "-c", "cd /tmp; g++ -std=c++{} in.cpp 2> out.txt".format(versn)],
	 				volumes={srcPath:{'bind': '/tmp', 'mode':'rw'}}, detach = True, remove=True)
	containerObj.wait() # Wait till the container exits

def compileSrcJava(versn, fileString, fileName):
	if versn == "7" or versn == "8":
		srcPath = os.getcwd() + '/tmp'
		file = open(srcPath + '/' + fileName,'w+', encoding = 'utf-8')
		file.write(fileString)
		file.close()
		client = docker.from_env()
		img = "ctp"
		if versn == "7":
			img = img + "4"
		else:
			img = img + "5"

		containerObj = client.containers.run(image=img, working_dir = '/tmp', command=["javac", "{}".format(fileName)],
	 				volumes={srcPath:{'bind': '/tmp', 'mode':'rw'}}, detach = True)
		containerObj.wait()
		writeLogsFile(containerObj)