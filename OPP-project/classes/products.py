"""
Products - contains a collections of all the products in the store
"""
from classes.product import Product
from json import JSONEncoder, JSONDecodeError, loads, dump

import json

from classes.amplifier import Amplifier, AmplifierEncoder, AmplifierDecoder
from classes.receiver import Receiver, ReceiverEncoder, ReceiverDecoder
from classes.turntable import Turntable, TurntableEncoder, TurntableDecoder

from typing import Dict, List, Tuple

#---------------------------------------------
# DEBUG
#---------------------------------------------
import logging
#---------------------------------------------

class ProductsEncoder(JSONEncoder):

    def default(self, o :Product):
        return o.__dict__
    
class Products:
    """ Holds a list with all the products in the store """

    products = []
    
    @classmethod
    def _get_product_type(cls, data: str) -> Tuple[str, str]:
        # Buscar la posición de "_type"
        type_index = data.find('"_type":')

        # Verificar si "_type" está presente en la cadena
        if type_index == -1:
            raise ValueError("'_type' not found in the dictionary.")

        # Extraer la parte del string que contiene "_type" y el valor
        type_and_rest = data[type_index:]

        # Split the string into two parts using the commas as separators
        parts = type_and_rest.split(',')

        # Obtain the product type
        product_type = parts[0].split(':')[1].strip(' "')

        # Define dict with the values to create the product (amplifier, receiver, turntable ...)
        product_data = {}

        for part in parts[1:]:
            key, value = part.split(':', 1)  # Limitamos a una sola división para manejar valores con comas
            key = key.strip(' "') # Delete spaces and quotes
            value = value.strip(' "') # Delete spaces and quotes
            value = value.rstrip(' "}') # Delete spaces, quotes and closing curly bracket
            product_data[key] = value #Add key and value to the dict


        product_data = str(product_data).replace("'", '"')

        # Return the product type and the product data
        return product_type, product_data


    @classmethod
    def load_products(cls) -> List[Product]:
        logging.debug(f'Products.load_products() ...')

        """
        Reads the products.txt file and re-compose the Python objects from 
        json representation of products.
        """

        rd = ReceiverDecoder()
        td = TurntableDecoder()
        ad = AmplifierDecoder()

        try:
            with open("products.txt") as f:
                for line in f:
                    data = loads(line)

                    logging.debug(f'Loading product {data}')

                    pt, pd = cls._get_product_type(str(data))

                    logging.debug('Decoding product...')
                    decoded_product = None

                    if pt == 'Receiver':
                        logging.debug(f'   Decoding receiver...: {str(pd)}')
                        decoded_product = rd.decode(str(pd))
                        logging.debug(f'   Decoded product: {decoded_product.get_details()}')

                    elif pt == 'Turntable':
                        logging.debug(f'   Decoding turntable...: {str(pd)}')
                        decoded_product = td.decode(str(pd))
                        logging.debug(f'Decoded product: {decoded_product.get_details()}')

                    elif pt == 'Amplifier':
                        logging.debug(f'   Decoding amplifier...: {str(pd)}')
                        decoded_product = ad.decode(str(pd))
                        logging.debug(f'Decoded product: {decoded_product.get_details()}')

                    else:
                        print(f'ERROR Decoding product: Unknown product type {pt}')
                    
                    logging.debug(f'      Decoded product: {decoded_product.get_details()}')

                    #TODO: not working properly: product is always added, even when the list already contains a product with same details ??? (check it)
                    if decoded_product not in cls.products:
                        cls.products.append(decoded_product)
                        logging.debug(f'Adding product {decoded_product} | 👌 Conteo: {len(cls.products)} ')
                    
        except (JSONDecodeError, FileNotFoundError) as e:
            if isinstance(e, JSONDecodeError):
                print(f'ERROR: {e}')
            elif isinstance(e, FileNotFoundError):
                print(f'ERROR: {e}')
            else:
                print(f'ERROR: {e}')
                
            cls.products = []

        return cls.products
    
    @classmethod
    def add_product(cls, prod :Product) -> bool:
        logging.debug(f'Products.add_product(prod : {prod.get_details}) ...')

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
        re = ReceiverEncoder()
        te = TurntableEncoder()
        ae = AmplifierEncoder()

        #cls.products = cls.load_products()
        
        if prod not in cls.products:

            if not isinstance(prod, Product):
                raise ValueError('Product must be an instance of Product class')
            else:
                ep = None

                if isinstance(prod, Receiver):
                    logging.debug(f'Adding receiver {prod.get_details()}')
                    ep = re.encode(prod)
                elif isinstance(prod, Turntable):
                    logging.debug(f'Adding turntable {prod.get_details()}')
                    ep = te.encode(prod)
                elif isinstance(prod, Amplifier):
                    logging.debug(f'Adding amplifier {prod.get_details()}')
                    ep = ae.encode(prod)
                else:
                    raise ValueError('Product must be an instance of Product class')

                with open("products.txt", 'a') as f:
                    dump(ep, f)
                    f.write("\n")
                
                return True
        
        return False


    @classmethod
    def remove_product(cls, prod :Product) -> bool:
        logging.debug(f'Products.remove_product(prod : {prod.get_details}) ...')

        """
        Removes a product from the products collection. We pass the product
        to be removed as a parameter to the function and then, as a first step
        we remove it from the class variable 'products'. Then, in a second step
        we iterate that collection and we serialize element by element
        """
        pass
    
    @classmethod
    def list_products(cls) -> None:
        logging.debug(f'Products.list_products() ...')
        
        """
        First we read the file products.txt and we deserialize the collection
        of products. Then we iterate the collection and we print each product
        """
        cls.products = cls.load_products()

        for p in cls.products:
            print(f'\t-{p.get_details()}')

        print(f'\n')