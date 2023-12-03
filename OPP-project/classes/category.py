# Advanced Python Programming - OPP Project | Author: Javier Pardos | javier.pardos10@e-uvt.ro

"""
Category - describes a single category
"""

from json import JSONEncoder, JSONDecoder, loads

#---------------------------------------------
# DEBUG
#---------------------------------------------
import logging
#---------------------------------------------


class Category:
    """ Definition of the Category class and its attributes/methods """  
    
    def __init__(self, name):
        logging.debug(f'Category.__init__(name : {name}) ...')
        
        self.name = name

    def __eq__(self, other) -> bool:
        
        """ Overloaded in order to verify the membership inside a collection """
        
        if type(other) == type(self):
            return self.name == other.name
        else:
            return False

    def __hash__(self) -> int:
        return hash(self.name)
    
    def get_details(self) -> str:

        """ Returns a string with the details of the category """
        
        logging.debug(f'Category.get_details() ...')
        
        return f"Category: {self.name}"

class CategoryEncoder(JSONEncoder):
    # Transform the Python object into a json representation
    def default(self, o :str) -> str:
        return o.__dict__
    pass

class CategoryDecoder(JSONDecoder):
    # Transform the json representation into a Python object
    def decode(self, o :str) -> str:
        data = loads(o)
        vals = []
        for key in data.keys():
            vals.append(data[key])
        cat = Category(*vals)
        return cat
