import socket
from threading import Thread

class RxDeamon(Thread):
    def __init__(self,addr,port):
        Thread.__init__(self)
        self.addr = addr
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
        self.sock.bind((self.addr, self.port))
        self.sock.settimeout(0.5)
        
        self.kill = False

    def run(self):
        while not self.kill:
            try:
                data, addr = self.sock.recvfrom(1024)
                print("\n"+data.decode('ascii'))
            except socket.timeout:
                pass
            
               
    def stop(self):
        self.kill = True