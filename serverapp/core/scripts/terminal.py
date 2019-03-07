import docker
import subprocess
import socket
import random
import os

MINPORT = 30000
MAXPORT = 65000

class SocketIsUsedException(Exception):
    pass

def checkPort(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex(('', port))

    if result == 0:
        raise SocketIsUsedException('socket %s in use' % (port))
    sock.close()
    return True

def getUnusedPort():
    port = False
    while port is False:
        givePort = random.randrange(MINPORT, MAXPORT)
        try:
            port = checkPort(givePort)
        except SocketIsUsedException as sock:
            raise sock
        else:
            return givePort

def copyCodeToServer(usrcontainer, usrcode, codelang):
    if (codelang == 35 ): #python
        lang = '.py'

    usrcontainer.container.exec_run('echo \'' + usrcode + ' \' > usrcompile' + lang )
    print("debug message.")
    

class terminal:

    def __init__(self, ssh, port):
        print("Port is: " + str(port))
        self.port = port
        self.https = False
        self.ssh = ssh
        self.running = False
        self.docker = None
        self.container = None
        self.address = None

    def __enter__(self):
        return self

    def __exit__(self, exec_type, exc_value, traceback):
        self.pid.terminate()

    def makeServer(self):
        try:
            print("Creating server with port: " + str(self.port))
            self.docker = docker.from_env()
            #                                CHANGE THIS TO YOUR DOCKER IMAGE NAME
            #                                                |
            #                                                |
            #                                                v
            imagecmd = '-p ' + str(self.port) + ' bash -x'
            self.container = self.docker.containers.run('fugg:latest',imagecmd,ports={self.port:self.port},detach=True,remove=True,network='test')
            print("THE CONTAINER NAME IS: " + self.container.name)
            self.running = True
            cmd = " docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' " + self.container.name
            self.address = os.popen(cmd).read()
            machete = self.address +':'+ str(self.port)

            print("the docker thing is: " + machete)
            
            return machete.replace('\n','')
        except Exception as e:
            raise e
    
    def terminate(self):
        if self.docker is not None:
            self.running = False
            self.container.kill()
            self.docker = None
