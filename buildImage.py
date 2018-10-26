import compilers
import docker

def basicImage():

    client = docker.from_env()
    for id in range(1, len(compilers.compilers)+1):
        
        tagName = "ctp" + str(id)
        print(tagName)
        dockerFileText = compilers.compilers[str(id)]
        dockerFile = open('dfile/Dockerfile', 'w', encoding = 'utf-8')     # Getting the content of Required Dockerfile
        dockerFile.write(dockerFileText)
        dockerFile.close()
        client.images.build(path="dfile", tag = tagName)
        