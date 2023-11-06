"""
Products - contains a collections of all the products in the store
"""
from classes.product import Product, DecoderProduct
from json import JSONDecoder, JSONEncoder, JSONDecodeError, loads, dump


from typing import List

class Products:
    """ Holds a list with all the products in the store """

    products = []

    @classmethod
    def load_products(cls) -> List[Product]:
        """
        Reads the products.txt file and re-compose the Python objects from 
        json representation of products.
        """
        return []
    
    @classmethod
    def add_product(cls, prod :Product) -> None:
        """
            Adds a product to the products collection. We pass the product.
            We need to check if the product is an instance of the Product class.
            In afirmative case we add it to the collection, otherwise we raise an
            exception.
            After we add the product to the collection we need to serialize the
            collection to the products.txt file. 
            We achieve this by iterating and encoding each product in the list 
            we received.

        """
        pass

    @classmethod
    def remove_product(cls, prod :Product) -> None:
        """
        Removes a product from the products collection. We pass the product
        to be removed as a parameter to the function and then, as a first step
        we remove it from the class variable 'products'. Then, in a second step
        we iterate that collection and we serialize element by element
        """
        pass
    
    @classmethod
    def list_products(cls) -> None:
        """
        First we read the file products.txt and we deserialize the collection
        of products. Then we iterate the collection and we print each product
        """
        pass