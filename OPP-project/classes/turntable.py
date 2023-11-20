"""
Turntable  -  inherits  the  Product  class  and  contains  specific  info  for  that  kind  of  product  (speed, 
connection type (wired, bluetooth), size)
"""
from classes.product import Product
from json import JSONEncoder, JSONDecoder, loads, dump

#---------------------------------------------
# DEBUG
#---------------------------------------------
import logging
#---------------------------------------------

class Turntable(Product):

    def __init__(self, name :str, price :float, speed :float, connection_type :str, size :str):
        logging.debug(f'Turntable.__init__(name : {name}, price : {price}, speed : {speed}, connection_type : {connection_type}, size : {size}) ...')
        super().__init__(name, price)
        self.speed = speed
        if connection_type in ['wired', 'bluetooth']:
            self.connection_type = connection_type
        else:
            raise ValueError('Connection type must be wired or bluetooth')
        self.size = size

    def __eq__(self, other) -> bool:
        logging.debug(f'Turntable.__eq__(other : {other}) ...')
        """ Overloaded in order to verify the membership inside a collection """
        
        # First check the type of the object, to ensure both are the same type
        if not isinstance(other, Turntable):
            return False
        
        logging.debug(f'return {self.name == other.name and self.price == other.price and self.speed == other.speed and self.connection_type == other.connection_type and self.size == other.size}')
        
        return (self.name == other.name and
                self.price == other.price and
                self.speed == other.speed and
                self.connection_type == other.connection_type and
                self.size == other.size)

    def __hash__(self):
        return hash( (self.name, self.price, self.speed, self.connection_type, self.size) )
    
    def get_details(self) -> str:
        logging.debug(f'Turntable.get_details() ...')
        return f'Turntable: name: {self.name}, price: {self.price}€, speed: {self.speed}, connection_type: {self.connection_type}, size: {self.size}'
    
class TurntableEncoder(JSONEncoder):
        
    def default(self, o :str):
        return o.__dict__

class TurntableDecoder(JSONDecoder):

    def decode(self, o :str) -> Turntable:
        data = loads(o)
        vals = []
        for key in data.keys():
            vals.append(data[key])
        turn = Turntable(*vals)
        return turn
