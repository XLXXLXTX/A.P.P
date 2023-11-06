"""
Category - describes a single category
"""

from json import JSONEncoder, JSONDecodeError, loads, dump

class CategoryEncoder(JSONEncoder):
    # TODO
    pass

class CategoryDecoder(JSONEncoder):
    # TODO
    pass

class Category:
    """ Definition of the Category class and its attributes/methods """  
    
    def __init__(self, name) -> object:
        self.name = name

    def __eq__(self, other) -> bool:
        """ Overloaded in order to verify the membership inside a collection """
        if type(other) == type(self):
            return self.name == other.name
        else:
            return False

    def __hash__(self):
        return hash(self.name)

