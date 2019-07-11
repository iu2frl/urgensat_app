import socket,sys
from threading import Thread
from handler.message_handler import MessageHandler
from station.packet import Packet
import logging
import helpers

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
            self.sock.settimeout(0.5)
        except Exception as e:
            self.logger.exception("Unable to create the rx server")
            helpers.terminate()
        
        self.kill = False

    def run(self):
        while not self.kill:
            try:
                connection, client_address = sock.accept()
                #data, addr = self.sock.recvfrom(1024)
                data = self.connection.recv(1024)
                packet = Packet.decode(data)
                
                if self.log_packet:
                    self.packet_logger.debug(" RX - "+str(packet.__dict__))
                
                self.message_handler.handle_message(packet)
            except socket.timeout:
                pass
            except Exception as e:
                self.logger.exception("Error during packet reception")
            

    def stop(self):
        self.logger.info("Stopping rx server")
        self.kill = True