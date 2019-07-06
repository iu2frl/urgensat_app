import socket
import threading

class RxDeamon(threading.Thread):
    def __init__(addr,port):
        self.addr = addr
        self.port = port
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
        sock.bind((self.addr, self.port))
    
    def run(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
        
        while True:
            data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
            print(str(data))