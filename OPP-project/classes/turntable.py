"""
Turntable  -  inherits  the  Product  class  and  contains  specific  info  for  that  kind  of  product  (speed, 
connection type (wired, bluetooth), size)
"""
from classes.product import Product

class Turntable(Product):

    def __init__(self, name :str, price :float, speed :float, connection_type :str, size :str):
        super().__init__(name, price)
        self.speed = speed
        if connection_type in ['wired', 'bluetooth']:
            self.connection_type = connection_type
        else:
            raise ValueError('Connection type must be wired or bluetooth')
        self.size = size

    def get_details(self) -> str:
        return f'Turntable: {self.name}, price: {self.price}€, speed: {self.speed}, connection_type: {self.connection_type}, size: {self.size}'