"""
Receiver  -  inherits  the  Products  class  and  contains  info  specific  for  that  kind  of  product  (number  of 
channels, color, size)
"""
from classes.product import Product

class Receiver(Product):
    
    def __init__(self, name: str, price: float, num_channels :int, color :str, size :str):
        super.__init__(name, price)
        self.num_channels = num_channels
        self.color = color
        self.size = size
    
    def get_details(self) -> str:
        return f'Receiver: {self.name}, price: {self.price}€, num_channels: {self.num_channels}, color: {self.color}, size: {self.size}'