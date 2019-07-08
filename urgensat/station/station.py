from deamon.tx_deamon import TxDeamon
from deamon.rx_deamon import RxDeamon

STANDARD_MESSAGE = "{}> {}"   

class Station:
    def __init__(self,call,deamon_tx,deamon_rx,info):
        self.deamon_tx = TxDeamon(deamon_tx["addr"],deamon_tx["port"])
        self.deamon_rx = RxDeamon(deamon_rx["addr"],deamon_rx["port"])
        self.call = call

    def format_message(self,message):
        return STANDARD_MESSAGE.format(self.call,message)

    def send_message(self,message):
        self.deamon_tx.send_packet(self.format_message(message))
    
    def build_from_config(station_config):
        call = station_config.raw_config["call"]
        
        deamon_tx = {
            "addr": station_config.raw_config["setup"]["deamon_tx"]["addr"],
            "port": station_config.raw_config["setup"]["deamon_tx"]["port"]
        }

        deamon_rx = {
            "addr": station_config.raw_config["setup"]["deamon_rx"]["addr"],
            "port": station_config.raw_config["setup"]["deamon_rx"]["port"]
        }
        
        return Station(call,deamon_tx,deamon_rx,{})