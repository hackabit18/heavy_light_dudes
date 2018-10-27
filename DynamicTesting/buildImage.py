import compilers
import docker

def basicImage():

    client = docker.from_env()
    for key in compilers.compilers:
        
        print(key)
        tagName = key
        dockerFileText = compilers.compilers[key]
        dockerFile = open('dfile/Dockerfile', 'w', encoding = 'utf-8')     # Getting the content of Required Dockerfile
        dockerFile.write(dockerFileText)
        dockerFile.close()
        client.images.build(path="dfile", tag = tagName)
