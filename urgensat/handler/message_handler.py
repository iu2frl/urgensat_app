import logging

class MessageHandler:
    def __init__(self,io_handler):
        self.logger = logging.getLogger("handler")
        self.io_handler = io_handler
    
    def handle_message(self,raw_text):
        #gestione messaggi per i/o 
        #gestione messaggi di testo
        print("\n"+raw_text)