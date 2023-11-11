"""
Product - base class for all the products we’ll have
"""

from abc import ABC, abstractmethod
from json import JSONEncoder, JSONDecoder, dump, loads

#---------------------------------------------
# DEBUG
#---------------------------------------------
import logging
#---------------------------------------------

# As Product its the base class from which all the other products will inherit, we make it abstract
class Product(ABC):

    # Define constructor with the base info common to all the prodcts
    def __init__(self, name :str, price :float):
        logging.debug(f'Product.__init__(name : {name}, price : {price}) ...')
        self._type = type(self).__name__ # Obtain name of the class, for child purpose
        self.name = name
        self.price = price

    def __eq__(self, other) -> bool:
        """ Overloaded in order to verify the membership inside a collection """
        if type(other) == type(self):
            return self.name == other.name and self.price == other.price
        else:
            return False

    def __hash__(self):
        return hash(self._type, self.name, self.price)
    
    # Define an abstract method to be implemented by the child classes
    # to get the info from the object
    @abstractmethod
    def get_details(self) -> str:
        logging.debug(f'Product.get_details() ...')
        pass