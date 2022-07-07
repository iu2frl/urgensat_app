from tx_deamon import TxDeamon
from rx_deamon import RxDeamon
from packet import Packet
import logging,helpers 

class Station:
    def __init__(self,call,deamon_tx,deamon_rx,message_handler,info,log_packet):
        self.deamon_tx = TxDeamon(deamon_tx["addr"],deamon_tx["port"],log_packet)
        self.deamon_rx = RxDeamon(deamon_rx["addr"],deamon_rx["port"],message_handler,log_packet)
        self.call = call
        self.logger = logging.getLogger("station")

    def send_message(self,message,dest):
        self.send_packet(message,"plain_text",dest)
    
    def send_packet(self,message,category,dest):
        p = Packet(self.call,dest,message,category)
        self.deamon_tx.send_packet(p)
    
    @staticmethod
    def build_from_config(station_config,message_handler):
        logger = logging.getLogger("station")

        try:
            call = station_config.raw_config["call"]

            if call is None:
                raise Exception('Call field blank')
            
            deamon_tx = {
                "addr": station_config.raw_config["setup"]["deamon_tx"]["addr"],
                "port": station_config.raw_config["setup"]["deamon_tx"]["port"]
            }

            if deamon_tx["addr"] is None or deamon_tx["port"] is None:
                raise Exception('Deamon tx field(s) blank')

            deamon_rx = {
                "addr": station_config.raw_config["setup"]["deamon_rx"]["addr"],
                "port": station_config.raw_config["setup"]["deamon_rx"]["port"]
            }

            if deamon_rx["addr"] is None or deamon_rx["port"] is None:
                raise Exception('Deamon rx field(s) blank')
            
        except Exception as e:
            logger.exception("Error parsing station config")
            helpers.terminate()
        
        try:
            log_packet = station_config.raw_config["log_packet"]
        except:
            log_packet = False

        return Station(call,deamon_tx,deamon_rx,message_handler,{},log_packet)
