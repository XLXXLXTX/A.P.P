"""
Product - base class for all the products we’ll have
"""

from abc import ABC, abstractmethod
from json import JSONEncoder, JSONDecoder, dump, loads


# As Product its the base class from which all the other products will inherit, we make it abstract
class Product(ABC):

    # Define constructor with the base info common to all the prodcts
    def __init__(self, name :str, price :float):
        self.name = name
        self.price = price

    # Define an abstract method to be implemented by the child classes
    # to get the info from the object
    @abstractmethod
    def get_details(self) -> str:
        pass