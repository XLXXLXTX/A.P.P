"""
Amplifier  -  inherits  the  Product  class  and  will  contain  info  specific  for  that  kind  of  product  (power, 
number of channels, size)
"""

from classes.product import Product

class Amplifier(Product):
    
    def __init__(self, name: str, price: float, power :int, num_channels :int, size :str):
        super().__init__(name, price)
        self.power = power
        self.num_channels = num_channels
        self.size = size
    
    def get_details(self) -> str:
        return f'Amplifier: {self.name}, price: {self.price}€, power: {self.power}, num_channels: {self.num_channels}, size: {self.size}'