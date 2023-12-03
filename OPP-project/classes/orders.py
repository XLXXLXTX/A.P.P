# Advanced Python Programming - OPP Project | Author: Javier Pardos | javier.pardos10@e-uvt.ro

"""
Orders  -  models  an  order  to  be  placed  in  the  store.  Basically  a  collection  of  products  and  quantities  also 
with a destination address
"""

from json import JSONDecodeError, loads, dump

from classes.order import Order, OrderEncoder, OrderDecoder

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
        
        od = OrderDecoder()
        
        try: 
            with open("orders.txt") as f:
                for line in f:
                    data = loads(line)

                    decoded_order = od.decode(str(data))

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
        
        # not checking if the order already exists in the list 
        # because orders with the same products and quantities can exist 

        o = { "products": [], "quantities": [], "address": order.address}

        # combine the products and quantities lists into a single dictionary
        for p, q in zip(order.products, order.quantities):
            o["products"].append(p.__dict__) # with __dict__ we get the object's attributes as a dictionary 
            o["quantities"].append(q)

        oe = OrderEncoder()
        order_encoded = oe.encode(o)

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
            
            # after removing the order from the list on memory", we need to update the file
            # so we overwrite the file with the new list of orders
            with open("orders.txt", "w") as f:
                for o in cls.orders:
                    oe = OrderEncoder()
                    order_encoded = oe.encode(o)
                    dump(order_encoded, f)
                    f.write(f'\n')
            
            return True
            
        return False

    @classmethod
    def list_orders(cls):
        logging.debug(f'Orders.list_orders() ...')

        cls.orders = cls.load_orders()

        if len(cls.orders) == 0:
            print(f'\tNo orders to show, Add some orders first!')
            return

        for o in cls.orders:
            print(f'{o.get_details()}')

        print(f'\n')