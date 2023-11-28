"""
Orders  -  models  an  order  to  be  placed  in  the  store.  Basically  a  collection  of  products  and  quantities  also 
with a destination address
"""

from classes.order import Order, OrderEncoder, OrderDecoder
from json import JSONEncoder, JSONDecodeError, loads, dump

from typing import List

#---------------------------------------------
# DEBUG
#---------------------------------------------
import logging
#---------------------------------------------

class Orders(object):

    orders = []

    @classmethod
    def load_orders(cls):
        logging.debug(f'Orders.load_orders() ...')
        
        # clear list, to avoid duplicate orders (file and memory)
        cls.orders = []
        
        # DONE: needs to be implemented
        od = OrderDecoder()
        
        try: 
            with open("orders.txt") as f:
                for line in f:
                    data = loads(line)

                    ##print(f'Loading order: {data}')

                    decoded_order = od.decode(str(data))

                    ##print(f'Decoded order: {decoded_order.get_details()}')

                    cls.orders.append(decoded_order)
                    logging.debug(f'Adding order {decoded_order} | 👌 Conteo: {len(cls.orders)} ')

        except (JSONDecodeError, FileNotFoundError) as e:
            if isinstance(e, JSONDecodeError):
                print(f'ERROR: {e}')
            elif isinstance(e, FileNotFoundError):
                print(f'ERROR: {e}')
            else:
                print(f'ERROR: {e}')
                
            cls.orders = []
        
        return cls.orders


    @classmethod
    def add_order(cls, order : Order) -> bool:
        logging.debug(f'Orders.add_order() ...')
        
        # Not checking if the order already exists in the list 
        # because orders with the same products and quantities can exist 

        o = { "products": [], "quantities": [], "address": order.address}

        #print(f'o: {o}')
        #print(f'o["products"]: {o["products"]}')
        #print(f'o["quantities"]: {o["quantities"]}')
        #print(f'o["address"]: {o["address"]}')

        # Combine the products and quantities lists into a single dictionary
        for p, q in zip(order.products, order.quantities):
            o["products"].append(p.__dict__) #With __dict__ we get the object's attributes as a dictionary 
            o["quantities"].append(q)

        oe = OrderEncoder()
        order_encoded = oe.encode(o)

        #cls.orders.append(o)
        #logging.debug(f'Adding order {o}')
        with open("orders.txt", "a") as f:
            dump(order_encoded, f)
            f.write(f'\n')

        return True

    @classmethod
    def remove_order(cls, ordernum: int):
        logging.debug(f'Orders.remove_order() ...')

        if ordernum in range(len(cls.orders)):
            logging.debug(f'Removing order {cls.orders[ordernum]}')
            cls.orders.pop(ordernum)
            return True

        return False

    @classmethod
    def list_orders(cls):
        logging.debug(f'Orders.list_orders() ...')

        # DONE: needs to be implemented
        cls.orders = cls.load_orders()

        for o in cls.orders:
            print(f'{o.get_details()}')

        print(f'\n')