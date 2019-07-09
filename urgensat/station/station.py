from deamon.tx_deamon import TxDeamon
from deamon.rx_deamon import RxDeamon
import logging,helpers

STANDARD_MESSAGE = "{}> {}"   

class Station:
    def __init__(self,call,deamon_tx,deamon_rx,message_handler,info):
        self.deamon_tx = TxDeamon(deamon_tx["addr"],deamon_tx["port"])
        self.deamon_rx = RxDeamon(deamon_rx["addr"],deamon_rx["port"],message_handler)
        self.call = call
        self.logger = logging.getLogger("station")

    def format_message(self,message):
        return STANDARD_MESSAGE.format(self.call,message)

    def send_message(self,message):
        self.deamon_tx.send_packet(self.format_message(message))
    
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

        return Station(call,deamon_tx,deamon_rx,message_handler,{})