import socket

class TxDeamon:
    def __init__(self, addr, port):
        self.addr = addr
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    def send_packet(self,message):
        self.sock.sendto(bytes(message, "utf-8"), (self.addr, self.port))