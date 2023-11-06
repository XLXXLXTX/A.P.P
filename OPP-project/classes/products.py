"""
Products - contains a collections of all the products in the store
"""
from classes.product import Product
from json import JSONEncoder, JSONDecodeError, loads, dump

import json

from classes.amplifier import Amplifier, AmplifierEncoder, AmplifierDecoder
from classes.receiver import Receiver, ReceiverEncoder, ReceiverDecoder
from classes.turntable import Turntable, TurntableEncoder, TurntableDecoder

from typing import List

class ProductsEncoder(JSONEncoder):

    def default(self, o :Product):
        return o.__dict__
    

class Products:
    """ Holds a list with all the products in the store """

    products = []

    @classmethod
    def load_products(cls) -> List[Product]:
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
                    data = json.loads(line)

                    print(f'Loading product {data}')

                    # not working:
                    """                    
                    if not isinstance(data, dict):
                        print(f'Error: {data} is not a dictionary')
                        continue
                    else:
                        print(f'Type: {data["_type"]}')
                        
                    """

                    # Buscar la posición de "_type"
                    type_index = data.find('"_type":')

                    # Extraer la parte del string que contiene "_type" y el valor
                    type_and_rest = data[type_index:]

                    # Dividir la cadena en dos partes utilizando las comas como separadores
                    parts = type_and_rest.split(',')

                    # Obtener el valor de "_type"
                    product_type = parts[0].split(':')[1].strip(' "')

                    product_data = {}
                    for part in parts[1:]:
                        key, value = part.split(':')
                        key = key.strip(' "')
                        value = value.strip(' "')
                        product_data[key] = value


                    #print(f'Product type: {product_type}')
                    #print(f'Product data: {product_data}')
                    
                    # -----------------
                    # TODO: NOT WORKING 

                    print('Decoding product...')

                    decoded_product = rd.decode(str(product_data))
                    print(f'Decoded product: {decoded_product.get_details()}')
                    
                    if decoded_product not in cls.products:
                        print(f'Adding product {decoded_product}')
                        cls.products.append(decoded_product)
        
                    #if not isinstance(data, dict):
                    #    print(f'Error: {data} is not a dictionary')
                    
                    # TODO: NOT WORKING
                    # -----------------
                    
        except (JSONDecodeError, FileNotFoundError) as e:
            cls.products = []

        return cls.products
    
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
        re = ReceiverEncoder()
        te = TurntableEncoder()
        ae = AmplifierEncoder()

        #cls.load_products()
        

        if prod not in cls.products:

            if not isinstance(prod, Product):
                raise ValueError('Product must be an instance of Product class')
            else:
                ep = None

                if isinstance(prod, Receiver):
                    print(f'Adding receiver {prod.get_details()}')
                    ep = re.encode(prod)
                elif isinstance(prod, Turntable):
                    print(f'Adding turntable {prod.get_details()}')
                    ep = te.encode(prod)
                elif isinstance(prod, Amplifier):
                    print(f'Adding amplifier {prod.get_details()}')
                    ep = ae.encode(prod)
                else:
                    raise ValueError('Product must be an instance of Product class')

                with open("products.txt", 'a') as f:
                    dump(ep, f)
                    f.write("\n")


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
        cls.load_products()

        print(f'Products: {cls.products}')
        for p in cls.products:
            print(f'--->{p.get_details()}')

        pass