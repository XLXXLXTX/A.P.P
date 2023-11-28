from classes.product import Product
from classes.products import Products
from json import JSONEncoder, JSONDecoder, loads, dump

from typing import List

#---------------------------------------------
# DEBUG
#---------------------------------------------
import logging
#---------------------------------------------

class Order:

    # DONE: needs to be implemented
    # Define an order as a list of products and quantities, and an address
    # to pass this object to the add_order() method in the Orders class
    # in order to add it to the list of orders
    # Maybe ????

    def __init__(self, products: List[Product], quantities: List[int], address: str) -> None:
        logging.debug(f'Orders.__init__() ...')
        ##print(f'__init__\n')
        ##print(f'address -> {len(address)} : {address} \n products -> {len(products)} : {products} \n quantities -> {len(quantities)} : {quantities}')
        
        if len(products) != len(quantities):
            raise ValueError(f'ERROR: Products and Quantities Lists have different lengths')
        else:
            self.order = []
            self.address = address
            self.products = products
            self.quantities = quantities
    
        """    
        def add_product(self, product: List[Product], quantitie: int) -> None:
        for i in range(quantitie):
            self.order.append(product)
        data = {"address": self.address, "product": product, "quantitie": quantitie}
        """
        
    def get_details(self) -> str:
        logging.debug(f'Order.get_details() ...')
        
        d = f"Address of the order: {self.address}\n"
        
        # Combine both list to create a single string
        for p, q in zip(self.products, self.quantities):
            # when order is decoded, the product is a dict, not an object
            # so we need to check the type of p
            if isinstance(p, dict):
                # TODO: da un error:
                #    raise ValueError("'_type' not found in the dictionary.")
                #    ValueError: '_type' not found in the dictionary.
                dp = Products.dict_to_product(p)
                d += '\n'
                d += f'\t-{dp.get_details()} x {q}'
            else:
                d += f'\t-{p.get_details()} x {q}'

        return d
    

class OrderEncoder(JSONEncoder):
            
    def default(self, o :str):
        return o.__dict__

class OrderDecoder(JSONDecoder):

    def decode(self, o : str) -> Order:
        ##print(f'OrderDecoder.decode()...')
        data = loads(o)
        vals = []
        for key in data.keys():
            vals.append(data[key])
        
        ##print(f'[vals] --> {vals}')
                
        order = Order(*vals)
        return order