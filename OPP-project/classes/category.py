"""
Category - describes a single category
"""

from json import JSONEncoder, JSONDecoder, JSONDecodeError, loads, dump
#from .category import Category

#---------------------------------------------
# DEBUG
#---------------------------------------------
import logging
#---------------------------------------------

class CategoryEncoder(JSONEncoder):
    # Transform the Python object into a json representation
    def default(self, o :str) -> str:
        return o.__dict__
    pass

class CategoryDecoder(JSONDecoder):
    # Transform the json representation into a Python object
    def decode(self, o :str):
        data = loads(o)
        vals = []
        for key in data.keys():
            vals.append(data[key])
        cat = Category(*vals)
        return cat

class Category:
    """ Definition of the Category class and its attributes/methods """  
    
    def __init__(self, name) -> object:
        logging.debug(f'Category.__init__(name : {name}) ...')
        self.name = name

    def __eq__(self, other) -> bool:
        """ Overloaded in order to verify the membership inside a collection """
        if type(other) == type(self):
            return self.name == other.name
        else:
            return False

    def __hash__(self):
        return hash(self.name)
    
    def get_details(self) -> str:
        logging.debug(f'Category.get_details() ...')
        
        """ Returns a string with the details of the category """
        return f"Category: {self.name}"

