# Advanced Python Programming - OPP Project | Author: Javier Pardos | javier.pardos10@e-uvt.ro

"""
Order - define an order as a list of products and quantities, and an address
"""

from typing import List

from json import JSONEncoder, JSONDecoder, loads

from classes.product import Product
from classes.products import Products

#---------------------------------------------
# DEBUG
#---------------------------------------------
import logging
#---------------------------------------------

class Order:

    def __init__(self, products: List[Product], quantities: List[int], address: str) -> None:
        logging.debug(f'Orders.__init__() ...')
        
        try:
            if len(products) != len(quantities):
                raise ValueError(f'ERROR: Products and Quantities Lists have different lengths')
        except ValueError as e:
            print(e)
            return

        self.order = []
        self.address = address
        self.products = products
        self.quantities = quantities

        
    def get_details(self) -> str:
        logging.debug(f'Order.get_details() ...')
        
        d = f"\nAddress of the order: {self.address}\n"
        
        # combine both list to create a single string
        for p, q in zip(self.products, self.quantities):
            # when order is decoded, the product p is a dict, not an object
            # so we need to check the type of each product p 
            if isinstance(p, dict):
                # read the dict and create a Product object
                dp = Products.dict_to_product(p)
                d += '\n'
                d += f'\t-{dp.get_details()} x {q}'
            else:
                # product is already a Product object
                # because its in memory
                d += f'\t-{p.get_details()} x {q}'

        return d
    

class OrderEncoder(JSONEncoder):
            
    def default(self, o :str):
        return o.__dict__

class OrderDecoder(JSONDecoder):

    def decode(self, o : str) -> Order:
        data = loads(o)
        vals = []
        for key in data.keys():
            vals.append(data[key])
        order = Order(*vals)
        return order