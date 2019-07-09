import socket,sys
from threading import Thread
from handler.message_handler import MessageHandler
import logging

class RxDeamon(Thread):
    def __init__(self,addr,port,message_handler):
        Thread.__init__(self)
        self.addr = addr
        self.port = port
        self.logger = logging.getLogger("deamon")
        
        self.message_handler = message_handler
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
            self.sock.bind((self.addr, self.port))
            self.sock.settimeout(0.5)
        except Exception as e:
            self.logger.exception("Unable to create the rx server")
            sys.exit()
        
        self.kill = False

    def run(self):
        while not self.kill:
            try:
                data, addr = self.sock.recvfrom(1024)
                self.message_handler.handle_message(data.decode('ascii'))
            except socket.timeout:
                pass
            except Exception as e:
                self.logger.exception("Bad rx socket configuration")
                sys.exit()
            

    def stop(self):
        self.logger.info("Stopping rx server")
        self.kill = True