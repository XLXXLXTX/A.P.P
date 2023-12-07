# Advanced Python Programming - OPP Project | Author: Javier Pardos | javier.pardos10@e-uvt.ro

"""
Receiver  -  inherits  the  Products  class  and  contains  info  specific  for  that  kind  of  product  (number  of 
channels, color, size)
"""

from typing import Dict, Any
from json import JSONEncoder, JSONDecoder, loads

from classes.product import Product

#---------------------------------------------
# DEBUG
#---------------------------------------------
import logging
#---------------------------------------------

class Receiver(Product):
    
    def __init__(self, name: str, price: float, num_channels :int, color :str, size :str):
        logging.debug(f'Receiver.__init__(name : {name}, price : {price}, num_channels : {num_channels}, color : {color}, size : {size}) ...')
        
        super().__init__(name, price)
        
        self.num_channels = num_channels
        self.color = color
        self.size = size
    
    def __eq__(self, other) -> bool:
        """ Overloaded in order to verify the membership inside a collection """
        
        logging.debug(f'Receiver.__eq__(other : {other}) ...')

        # first check the type of the object, to ensure both are the same type
        if not isinstance(other, Receiver):
            return False

        return (self.name == other.name and
                self.price == other.price and
                self.num_channels == other.num_channels and
                self.color == other.color and
                self.size == other.size)

    def __hash__(self) -> int:
        """ Overloaded in order to verify the membership inside a collection"""
        
        logging.debug(f'Receiver.__hash__() ...')

        return hash( (self.name, self.price, self.num_channels, self.color, self.size) )

    def get_details(self) -> str:
        logging.debug(f'Receiver.get_details() ...')
        return f'Receiver: name: {self.name}, price: {self.price}€, num_channels: {self.num_channels}, color: {self.color}, size: {self.size}'

class ReceiverEncoder(JSONEncoder):
        
    def default(self, o :str) -> Dict[str, Any]:
        return o.__dict__

class ReceiverDecoder(JSONDecoder):
    
    def decode(self, o :str) -> Receiver:
        data = loads(o)
        vals = []
        for key in data.keys():
            vals.append(data[key])
        rec = Receiver(*vals)
        return rec
