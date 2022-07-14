import logging
from packet import Packet

class MessageHandler:
    def __init__(self,io_handler):
        self.logger = logging.getLogger("handler")
        self.io_handler = io_handler
    
    def handle_message(self,packet):
        try:
            category_match = False
            
            if packet.category==0:
                category_match = True
            #gestione messaggi di testo
            if packet.category==1:
                print(packet.sender+"> "+packet.message)
                category_match = True
            #gestione messaggi per i/o
            if packet.category==2:
                category_match = True
            #gestione messaggi contenenti file
            if packet.category==3:
                category_match = True

            if not category_match:
                raise Exception('Deamon tx field(s) blank') 
            
        except Exception as e:
            self.logger.exception("Unable to handle packet") 
