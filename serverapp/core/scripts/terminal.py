import subprocess
import socket
import random

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

class terminal:

    def __init__(self, ssh, port):
        print("Port is: " + str(port))
        self.port = port
        self.https = False
        self.ssh = ssh
        self.running = False
        self.pid = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.pid.terminate()

    def makeServer(self):
        try:
            print("Creating server with port: " + str(self.port))
            self.pid = subprocess.Popen(['node', 'wetty/index.js', '--sshhost', '--sshuser', str(self.ssh), '-p', str(self.port)])
            self.running = True
            return self.port
        except Exception as e:
            raise e
    
    def terminate(self):
        if self.pid is not None:
            self.running = False
            self.pid.kill()
            self.pid = None
