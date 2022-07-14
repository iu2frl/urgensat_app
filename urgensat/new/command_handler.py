special_keys = [
    "exit()",
    "macro(",
    "station_info()"
]

import logging
from station_config import StationConfig
from packet import Packet
import sys
import helpers

class CommandHandler:
    def __init__(self,station_config,station):
        self.station = station
        self.station_config = station_config
        self.logger = logging.getLogger("handler")
    
    def parse_command(self,raw_text):
        special_command_found = False

        if raw_text[:5]=="macro":
            try:
                macro_name = raw_text[6:raw_text.index(')')]
            except:
                self.logger.info("Can't identify macro")
                return

            try:
                macros = self.station_config.raw_config["macro"]
                macro_text = macros[macro_name]
                
                if macro_text is None: 
                    raise Exception('Macro text blank')
               
                self.station.send_message(macro_text,"")
                
                print()
                self.logger.info("Sending macro '"+macro_name+"'")
                print()
            except:
                print()
                self.logger.warning("Unable to send '"+macro_name+"' macro", exc_info=True)
                print()
                #print("\n[*]  not found, please check "+self.station.call+".yaml\n")
            
            special_command_found = True
        if raw_text=="exit()":
            helpers.terminate()
        
        if not(special_command_found):
            self.station.send_message(raw_text,"")
