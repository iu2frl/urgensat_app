special_keys = [
    "exit()",
    "macro(",
    "station_info()"
]

import logging
from station.station_config import StationConfig
import sys
import helpers

class CommandHandler:
    def __init__(self,log_file,station_config,station):
        logging.basicConfig(filename=log_file, filemode='w')
        self.station = station
        self.station_config = station_config
    
    def parse_command(self,raw_text):
        special_command_found = False

        if raw_text[:5]=="macro":
            macro_name = raw_text[6:raw_text.index(')')]

            try:
                macros = self.station_config.raw_config["macro"]
                macro_text = macros[macro_name]
                self.station.send_message(macro_text)
                print("\n[*] sended macro "+macro_name+"\n")
            except:
                print("\n[*] macro not founded, please check "+self.station.call+".yaml\n")
            
            special_command_found = True
        if raw_text=="exit()":
            helpers.terminate(self.station)
        
        if not(special_command_found):
            self.station.send_message(raw_text)