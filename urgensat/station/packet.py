category_enum = {
    "plain_text": 1,
    "i/o": 2,
    "file": 3
}

import logging,umsgpack,json

class Packet:
    def __init__(self,sender=None,dest=None,message=None,category=None):
        
        self.sender = sender

        if dest=="":
            self.dest = "*"
        else:
            self.dest = dest
        
        try:
            if isinstance(category, int):
                self.category = category
            else:  
                self.category = category_enum[category]
            
            self.message = message 
        except Exception as e:
            logger = logging.getLogger("station")
            logger.exception("Unable to create packet object")

    def encode(packet):
        logger = logging.getLogger("station")
    
        try:
            encoded_packet = umsgpack.packb(json.dumps(packet.__dict__))
        except Exception as e:
            logger.exception("Unable to encode packet")
        
        return encoded_packet
    
    def decode(packet):
        logger = logging.getLogger("station")
        
        try:
            packet_dict = json.loads(umsgpack.unpackb(packet))
            decoded_packet = Packet(packet_dict["sender"],packet_dict["dest"],packet_dict["message"],packet_dict["category"])
        except Exception as e:
            logger.exception("Unable to decode packet")
        
        return decoded_packet