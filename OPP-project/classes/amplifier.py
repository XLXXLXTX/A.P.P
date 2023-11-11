"""
Amplifier  -  inherits  the  Product  class  and  will  contain  info  specific  for  that  kind  of  product  (power, 
number of channels, size)
"""

from json import JSONEncoder, JSONDecoder, loads, dump
from classes.product import Product

#---------------------------------------------
# DEBUG
#---------------------------------------------
import logging
#---------------------------------------------

class AmplifierEncoder(JSONEncoder):
    
    def default(self, o :str):
        return o.__dict__
    
class AmplifierDecoder(JSONDecoder):

    def decode(self, o :str) -> object:
        data = loads(o)
        vals = []
        for key in data.keys():
            vals.append(data[key])
        amp = Amplifier(*vals)
        return amp



class Amplifier(Product):
    
    def __init__(self, name: str, price: float, power :int, num_channels :int, size :str):
        logging.debug(f'Amplifier.__init__(name : {name}, price : {price}, power : {power}, num_channels : {num_channels}, size : {size}) ...')
        super().__init__(name, price)
        self.power = power
        self.num_channels = num_channels
        self.size = size

    def __eq__(self, other) -> bool:
        """ Overloaded in order to verify the membership inside a collection """
        if type(other) == type(self):
            return self.name == other.name and self.price == other.price\
                   and self.power == other.power and self.num_channels == other.num_channels\
                   and self.size == other.size
        else:
            return False

    def __hash__(self):
        return hash(self.name, self.price, self.power, self.num_channels, self.size)
    
    def get_details(self) -> str:
        logging.debug(f'Amplifier.get_details() ...')
        return f'Amplifier: name: {self.name}, price: {self.price}€, power: {self.power}, num_channels: {self.num_channels}, size: {self.size}'