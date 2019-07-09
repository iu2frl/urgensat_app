import socket,logging,sys
import helpers

class TxDeamon:
    def __init__(self, addr, port):
        self.addr = addr
        self.port = port

        self.logger = logging.getLogger("deamon")

        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        except Exception as e:
            self.logger.exception("Unable to create tx deamon")
            helpers.terminate()

    def send_packet(self,message):
        try:
            self.sock.sendto(bytes(message, "utf-8"), (self.addr, self.port))
        except Exception as e:
            self.logger.exception("Bad tx socket configuration")
            helpers.terminate()
            