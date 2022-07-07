import socket,sys
from threading import Thread
from handler.message_handler import MessageHandler
from station.packet import Packet
import logging
import helpers
import select

class RxDeamon(Thread):
    def __init__(self,addr,port,message_handler,log_packet):
        Thread.__init__(self)
        self.addr = addr
        self.port = port
        self.logger = logging.getLogger("deamon")

        self.packet_logger = logging.getLogger("packet")
        self.log_packet = log_packet
        
        self.message_handler = message_handler
        try:
            #self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.bind((self.addr, self.port))
            self.sock.listen(1)
        except Exception:
            self.logger.exception("Unable to create the rx server")
            helpers.terminate()
        
        self.kill = False

    def run(self):
        try:
            connection, client_address = self.sock.accept()
            connection.settimeout(0.1)
            
            while not self.kill:
                data = b""
                end_of_packet_received = False
                
                while not(end_of_packet_received):
                    try:
                        data = data + connection.recv(1024)
                    except socket.timeout:
                        if self.kill:
                            break
                        pass
                    
                    if "}" in data.decode():
                        end_of_packet_received = True
                
                if data!=b"" and not(self.kill):
                    packet = Packet.decode(data)
                    self.message_handler.handle_message(packet)
                
                if self.log_packet:
                    self.packet_logger.debug(" RX - "+str(packet.__dict__))
                
                
        except Exception:
            self.logger.exception("Error during packet reception")

        self.sock.close()   

    def stop(self):
        self.logger.info("Stopping rx server")
        self.kill = True
        