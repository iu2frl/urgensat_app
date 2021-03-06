import socket,logging,sys
import helpers
from packet import Packet

class TxDeamon:
    def __init__(self, addr, port, log_packet):
        #da eliminare finito di integrare il socket tcp
        self.addr = addr
        self.port = port

        self.packet_logger = logging.getLogger("packet")
        self.log_packet = log_packet

        self.logger = logging.getLogger("deamon")

        try:
            #self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect((addr,port))
        except Exception as e:
            self.logger.exception("Unable to create tx deamon")
            helpers.terminate()

    def send_packet(self,packet):
        
        if self.log_packet:
            self.packet_logger.debug(" TX - "+str(packet.__dict__))
        
        try:
            #self.sock.sendto(Packet.encode(packet), (self.addr, self.port))
            self.sock.sendall(Packet.encode(packet))
        except Exception as e:
            self.logger.exception("Error during packet transmission")
            
