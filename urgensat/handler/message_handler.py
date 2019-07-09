import logging
from station.packet import Packet

class MessageHandler:
    def __init__(self,io_handler):
        self.logger = logging.getLogger("handler")
        self.io_handler = io_handler
    
    def handle_message(self,packet):
        try:
            category_match = False

            #gestione messaggi di testo
            if packet.category==1:
                print(packet.sender+"> "+packet.message)
                category_match = True
            
            #gestione messaggi per i/o
            
            #gestione messaggi contenenti file

            if not category_match:
                raise Exception('Deamon tx field(s) blank') 
            
        except Exception as e:
            self.logger.exception("Unable to handle packet") 