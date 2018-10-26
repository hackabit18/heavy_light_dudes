import os
def compileSrcCpp(versn, fileString):
	srcPath = os.getcwd() + '/tmp'
	file = open(srcPath + '/in.cpp','w', encoding = 'utf-8')
	file.write(fileString)
	file.close()
	containerObj = client.containers.run(image="ctp1", 
	            command=["/bin/bash", "-c", "cd /tmp; g++ -std={} in.cpp 2> out.txt".format(versn)], 
	            volumes={srcPath:{'bind': '/tmp', 'mode':'rw'}}, detach=True, remove=True)