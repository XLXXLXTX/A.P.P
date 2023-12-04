from classes.amplifier import Amplifier
from classes.receiver import Receiver
from classes.turntable import Turntable
from classes.product import Product

from classes.products import Products

from classes.category import Category
from classes.categories import Categories

from classes.order import Order
from classes.orders import Orders

from typing import List

__colors = ['red', 'blue', 'green', 'yellow', 'black']
__size = ['small', 'medium', 'large', 'extra large', 'extra extra large']
__connection_type = ['wired', 'bluetooth', 'wired', 'bluetooth', 'asdasd']
__categories = ['Amplifiers', 'Receivers', 'Turntables']


def test_product() -> None:
    print('\ntest_product() ...')

    try:
        p = Product('Producto prueba', 100)
        print(p.get_details())
    except Exception as e:
        print(f'ERROR: {e}')

def test_receiver() -> List[Receiver]:
    print('\ntest_receiver() ...')

    receivers = []

    for i in range(5):
        receivers.append(Receiver(f'Receiver {i}', 100 + i * 100, i*2, __colors[i], __size[i]))
    
    for r in receivers:
        print(r.get_details())

    return receivers        

def test_turntable() -> List[Turntable]:
    print('\ntest_turntable() ...')

    turntables = []

    for i in range(5):
        try:
            turntables.append(Turntable(f'Turntable {i}', 100 + i * 100, 2 * i, __connection_type[i], __size[i]))
        except Exception as e:
            print(f'ERROR: {e}\n')
    
    for t in turntables:
        print(t.get_details())

    return turntables

def test_amplifier() -> List[Amplifier]:
    print('\ntest_amplifier() ...')

    amplifiers = []
    for i in range(5):
        amplifiers.append(Amplifier(f'Amplifier {i}', 100 + i * 100, 2 * i, i*2, __size[i]))

    for a in amplifiers:
        print(a.get_details())
        
    return amplifiers

def test_all_products(receivers: List[Receiver], turntables: List[Turntable], amplifiers: List[Amplifier]) -> None:
    print('\ntest_all_products() ...')

    # append all list in one list:
    all_products = receivers + turntables + amplifiers

    # check if all_products is a list of Product objects and prints the details:
    for i in all_products:
        if isinstance(i, Product):
            print(f'Product --> {i.get_details()}')

def test_encoder(lista :List[Product]) -> None:
    print('\ntest_encoder() ...')

    for p in lista:
        Products.add_product(p)
    
    Products.list_products()

# --------------------------------------------
# Methods to test Category/Categories classes:
# --------------------------------------------

def test_category() -> List[Category]:
    print('\ntest_category() ...')

    print(f'\n')
    
    categories = []

    for i in range(__categories.__len__()):
        categories.append(Category(__categories[i]))
    
    for c in categories:
        print(c.get_details())

    return categories

def test_category_encoder(lista: List[Category]) -> None:
    print('\ntest_category_encoder() ...')

    for c in lista:
       Categories.add_category(c)
    
    Categories.list_categories()

def test_eq_amplifier() -> None:
    amplifier1 = Amplifier("Amplificador1", 100.0, 50, 2, "Medium")
    amplifier2 = Amplifier("Amplificador1", 100.0, 50, 2, "Medium")
    l = [amplifier2]

    for i in l:
        print(f'Amplifier1: {amplifier1} == i: {i} --> {amplifier1 == i}')

    if amplifier1 in l:
        print(f'Amplifier1: {amplifier1} in l: {l}')

# --------------------------------------------
# Methods to test Order/Orders classes:
# --------------------------------------------
def test_order() -> None:
    print('\ntest_order() ...')
    
    a = Amplifier("Amplificador1", 100.0, 50, 2, "Medium")
    r = Receiver("Receiver1", 100.0, 50, "Red", "Medium")
    t = Turntable("Turntable1", 100.0, 50, "wired", "Medium")

    products = [a]#, r, t]
    quantities = [1]#, 2, 3]

    order_obj = Order(products, quantities, 'Calle Falsa 123')
    #print(f'{order_obj.get_details()}\n')
    
    Orders.add_order(order_obj)

    p2 = [a, r, t]
    q2 = [1, 2, 3]

    order_obj2 = Order(p2, q2, 'Freddys fazzbear pizza XD')
    #print(f'{order_obj2.get_details()}\n')

    Orders.add_order(order_obj2)

    #order_simple = Order([a], [10], 'Calle Falsa 456')
    
    #Orders.add_order(order_simple)

    Orders.list_orders()

def test_orders_decoder() -> None:
    print('\ntest_orders_decoder() ...')

    Orders.list_orders()

# --------------------------------------------


def test_main() -> None:
    print('\ntest_main() ...')

    
    # test product implementation:
    test_product()

    # test receiver implementation:
    r = test_receiver()

    # test turntable implementation:
    t = test_turntable()

    # test amplifier implementation:
    a = test_amplifier()

    # test all products:
    test_all_products(r, t, a)
    
    # test Encoder implementation:
    lista = r + t + a
    test_encoder(lista)

    # test Encoder/Decoder Category/Categories implementation:
    c = test_category()
    test_category_encoder(c)

    # test Order/Orders implementation:
    test_order()

    # test Orders Decoder implementation (reading from file):
    test_orders_decoder() 
    
    #TODO: still not working in products.py properly
    # test __eq__ implementation: 
    #test_eq_amplifier()
