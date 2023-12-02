# Advanced Python Programming - OPP Project | Author: Javier Pardos | javier.pardos10@e-uvt.ro

"""
Amplifier  -  inherits  the  Product  class  and  will  contain  info  specific  for  that  kind  of  product  (power, 
number of channels, size)
"""

from json import JSONEncoder, JSONDecoder, loads

from classes.product import Product

#---------------------------------------------
# DEBUG
#---------------------------------------------
import logging
#---------------------------------------------

class Amplifier(Product):
    
    def __init__(self, name: str, price: float, power :int, num_channels :int, size :str):
        logging.debug(f'Amplifier.__init__(name : {name}, price : {price}, power : {power}, num_channels : {num_channels}, size : {size}) ...')
        
        super().__init__(name, price)
        
        self.power = power
        self.num_channels = num_channels
        self.size = size

    def __eq__(self, other) -> bool:
        """ Overloaded in order to verify the membership inside a collection """
        
        logging.debug(f'Amplifier.__eq__(other : {other}) ...')
        
        # first check the type of the object, to ensure both are the same type
        if not isinstance(other, Amplifier):
            return False
        
        return (self.name == other.name and 
                self.price == other.price and
                self.power == other.power and 
                self.num_channels == other.num_channels and
                self.size == other.size)

    def __hash__(self) -> int:
        logging.debug(f'Amplifier.__hash__() ...')

        return hash( (self.name, self.price, self.power, self.num_channels, self.size) )
    
    def get_details(self) -> str:
        logging.debug(f'Amplifier.get_details() ...')

        return f'Amplifier: name: {self.name}, price: {self.price}€, power: {self.power}, num_channels: {self.num_channels}, size: {self.size}'

class AmplifierEncoder(JSONEncoder):
    
    def default(self, o :str) -> str:
        return o.__dict__
    
class AmplifierDecoder(JSONDecoder):

    def decode(self, o :str) -> Amplifier:
        data = loads(o)
        vals = []
        for key in data.keys():
            vals.append(data[key])
        amp = Amplifier(*vals)
        return amp


