"""
Receiver  -  inherits  the  Products  class  and  contains  info  specific  for  that  kind  of  product  (number  of 
channels, color, size)
"""
from classes.product import Product
from json import JSONEncoder, JSONDecoder, loads, dump

#---------------------------------------------
# DEBUG
#---------------------------------------------
import logging
#---------------------------------------------

class ReceiverEncoder(JSONEncoder):
        
    def default(self, o :str):
        return o.__dict__

class ReceiverDecoder(JSONDecoder):
    
    def decode(self, o :str):
        data = loads(o)
        vals = []
        for key in data.keys():
            #print(f'Key: {key}')
            vals.append(data[key])
        rec = Receiver(*vals)
        return rec

class Receiver(Product):
    
    def __init__(self, name: str, price: float, num_channels :int, color :str, size :str):
        logging.debug(f'Receiver.__init__(name : {name}, price : {price}, num_channels : {num_channels}, color : {color}, size : {size}) ...')
        super().__init__(name, price)
        self.num_channels = num_channels
        self.color = color
        self.size = size
    
    def __eq__(self, other) -> bool:
        """ Overloaded in order to verify the membership inside a collection """
        if type(other) == type(self):
            return self.name == other.name and self.price == other.price\
                   and self.num_channels == other.num_channels and self.color == other.color\
                   and self.size == other.size
        else:
            return False

    def __hash__(self):
        return hash(self.name, self.price, self.num_channels, self.color, self.size)

    def get_details(self) -> str:
        logging.debug(f'Receiver.get_details() ...')
        return f'Receiver: name: {self.name}, price: {self.price}€, num_channels: {self.num_channels}, color: {self.color}, size: {self.size}'