from deamon.tx_deamon import TxDeamon

STANDARD_MESSAGE = "{}> {}"   

class Station:
    def __init__(self,call,addr,port,info):
        self.call = call
        self.info = info
        self.deamon = TxDeamon(addr,port)

    def format_message(self,message):
        return STANDARD_MESSAGE.format(self.call,message)

    def send_message(self,message):
        self.deamon.send_packet(self.format_message(message))
    
    def build_from_config(station_config):
        call = station_config.raw_config["call"]
        addr = station_config.raw_config["setup"]["deamon_tx"]["addr"]
        port = station_config.raw_config["setup"]["deamon_tx"]["port"]

        return Station(call,addr,port,{})