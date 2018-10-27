import os
import docker
import time
def writeLogsFile(containerObj):
	OutFile = open('tmp/out.txt', 'w', encoding = 'utf-8')
	OutFile.write(containerObj.logs().decode('utf-8'))
	OutFile.close()
#	OutFile.write(Out+'\n'+Error)
def compileSrc():
	client = docker.from_env()
	containerObj = client.containers.run(image = "test", remove = False, detach = True)
	time.sleep(1)
	containerObj.stop()
	writeLogsFile(containerObj)

