# Advanced Python Programming - OPP Project | Author: Javier Pardos | javier.pardos10@e-uvt.ro

"""
Products - contains a collections of all the products in the store
"""

from typing import List, Tuple

from json import JSONDecodeError, loads, dump
import json

from classes.product import Product
from classes.amplifier import Amplifier, AmplifierEncoder, AmplifierDecoder
from classes.receiver import Receiver, ReceiverEncoder, ReceiverDecoder
from classes.turntable import Turntable, TurntableEncoder, TurntableDecoder

#---------------------------------------------
# DEBUG
#---------------------------------------------
import logging
#---------------------------------------------

class Products:
    """ Holds a list with all the products in the store """

    products = []
    
    @classmethod
    def _get_product_type(cls, data: str) -> Tuple[str, str]:

        """
        Auxiliary function to get the product type from a given dictionary
        """

        logging.debug(f'Products._get_product_type() ...')

        # parse the string into a dictionary
        try:
            data_dict = json.loads(data)
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON data.")

        # get the product type
        product_type = data_dict.get('_type')
        if product_type is None:
            raise ValueError("'_type' not found in the dictionary.")

        # remove the product type from the dictionary
        del data_dict['_type']

        # convert the dictionary back into a string
        product_data = json.dumps(data_dict)

        # return the product type and the product data
        return product_type, product_data
    
    @classmethod
    def dict_to_product(cls, data: dict) -> Product:

        """
        Auxiliary function to convert a dictionary into a product object
        """
                
        logging.debug(f'Products.dict_to_product() ...')

        rd = ReceiverDecoder()
        td = TurntableDecoder()
        ad = AmplifierDecoder()

        # pass the product in str but with '' to make sure its formatted correctly
        # as its a "json" str
        pt, pd = cls._get_product_type(str(data).replace("'", '"'))

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

        return decoded_product
    
    @classmethod
    def load_products(cls) -> List[Product]:
        logging.debug(f'Products.load_products() ...')

        """
        Reads the products.txt file and re-compose the Python objects from 
        json representation of products.
        """

        # clear list, to avoid duplicate products (file and memory)
        cls.products = []

        rd = ReceiverDecoder()
        td = TurntableDecoder()
        ad = AmplifierDecoder()

        try:
            with open("products.txt") as f:
                for line in f:
                    data = loads(line)

                    logging.debug(f'Loading product {data}')

                    pt, pd = cls._get_product_type(str(data))

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

                    #TODO: not working properly: product is always added, even when 
                    # the list already contains a product with same details 
                    # so that's why the trick of cls.products = []
                    if decoded_product not in cls.products:
                        cls.products.append(decoded_product)
                        logging.debug(f'Adding product {decoded_product} | 👌 Count: {len(cls.products)} ')
                    
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

        cls.products = cls.load_products()

        # TODO: No compara bien xd 
        ##for p in cls.products:
        ##    print(f'*Comparando {p.get_details()}\n\t con\n\t {prod.get_details()}: {p == prod}')

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
        
        else:
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
    
        if prod in cls.products:
            cls.products.remove(prod)
            logging.debug(f'Product {prod.get_details()} removed successfully!')

            re = ReceiverEncoder()
            te = TurntableEncoder()
            ae = AmplifierEncoder()
            encoded_product = None

            with open("products.txt", 'w') as f:
                for p in cls.products:

                    if isinstance(p, Amplifier):
                        encoded_product = ae.encode(p)
                    elif isinstance(p, Receiver):
                        encoded_product = re.encode(p)
                    elif isinstance(p, Turntable):
                        encoded_product = te.encode(p)
                    
                    dump(encoded_product, f)
                    f.write("\n")

            return True

        return False
    
    @classmethod
    def list_products(cls) -> None:
        logging.debug(f'Products.list_products() ...')
        
        """
        First we read the file products.txt and we deserialize the collection
        of products. Then we iterate the collection and we print each product
        """
        cls.products = cls.load_products()

        if len(cls.products) == 0:
            print(f'\tNo products to show, Add some products first!')
            return

        for p in cls.products:
            print(f'\t-{p.get_details()}')

        print(f'\n')