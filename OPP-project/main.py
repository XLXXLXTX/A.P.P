# impor from classes folder each file
from classes.category import Category
from classes.categories import Categories
from classes.products import Products
#from classes.product import Product
from classes.amplifier import Amplifier
from classes.receiver import Receiver
from classes.turntable import Turntable
from classes.order import Order
from classes.orders import Orders

#---------------------------------------------
# DEBUG
#---------------------------------------------
# import sys to use sys.argv 
import sys
from test import test_main

import logging
#---------------------------------------------

def setupLogging(level: int = logging.INFO) -> None:
    # By default level is set to INFO, if no argument is passed to the function
    
    # Log level: ----------------------------------------------------
    fmt = '[%(levelname)s : %(asctime)s - %(message)s]'
    # Adjust log level, format msg and date format
    logging.basicConfig(level=level, format=fmt, datefmt='%d-%m-%Y %H:%M:%S')
    # Log level: ----------------------------------------------------

    logging.debug(f'setupLogging() ...')

#---------------------------------------------
# Logic functs
#---------------------------------------------

def addCategory():
    logging.debug(f'addCategory() ...')

    name = input(f'\tType the name of the new category: ')
    cat = Category(name)
    if Categories.add_category(cat):
        print(f'\t\tCategory added successfully!')
    else:
        print(f'\t\tCategory already exists!')

def removeCategory():
    logging.debug(f'removeCategory() ...')

    c = Categories.load_categories()
    i = 0
    print(f'\n')
    for cat in c:
        print(f'\t{i}) {cat.name}')
        i += 1
    
    catnum = int( input(f'\n\tType the number of the category to be removed: ') )
    cat = Categories.categories[catnum]

    if Categories.remove_category(cat):
        print(f'\t\tCategory removed successfully!')
    else:
        print(f'\t\tCategory not found!')


def displayCategories():
    logging.debug(f'displayCategories() ...')

    Categories.list_categories()

#---------------------------------------------

def addProduct():
    logging.debug(f'addProduct() ...')

    types_of_products = {1 : Amplifier, 2 : Receiver, 3 : Turntable}
    
    for t in types_of_products:
        print(f'\t{t}) {types_of_products[t].__name__}')
    
    p = int(input(f'\n\tType the number of the product to: '))
    
    if p not in types_of_products:
        print(f'\t\tProduct not found!')
        return
    else:
        
        #Ask for details of the product
        info = {"name" : "", "price" : 0}
        product = None

        # Ask for comon info of the product
        info["name"] = input(f'\t\tType the name of the new {types_of_products[p].__name__}: ')
        info["price"] = float(input(f'\t\tType the price of the new {types_of_products[p].__name__}: '))

        # Ask for specific info of the product
        if types_of_products[p].__name__ == Amplifier.__name__:

            info["power"] = int(input(f'\t\tType the power of the new {types_of_products[p].__name__}: '))
            info["num_channels"] = int(input(f'\t\tType the number of channels of the new {types_of_products[p].__name__}: '))
            info["size"] = input(f'\t\tType the size of the new {types_of_products[p].__name__}: ')

        elif types_of_products[p].__name__ == Receiver.__name__:

            info["num_channels"] = int(input(f'\t\tType the number of channels of the new {types_of_products[p].__name__}: '))
            info["color"] = input(f'\t\tType the color of the new {types_of_products[p].__name__}: ')
            info["size"] = input(f'\t\tType the size of the new {types_of_products[p].__name__}: ')

        elif types_of_products[p].__name__ == Turntable.__name__:

            info["speed"] = float(input(f'\t\tType the speed of the new {types_of_products[p].__name__}: '))
            info["connection_type"] = input(f'\t\tType the connection type (wired or bluetooth) of the new {types_of_products[p].__name__}: ')
            info["size"] = input(f'\t\tType the size of the new {types_of_products[p].__name__}: ')

        #Create the product
        product = types_of_products[p](**info)

        # Add the product to the list of products
        if Products.add_product(product):
            print(f'\n\t\tProduct added successfully!')
        else:
            print(f'\n\t\tProduct already exists!')
        
        #TODO: not working properly: add_product() returns always True ??? (check it)

def removeProduct():
    logging.debug(f'removeProduct() ...')

    p = Products.load_products()
    i = 0
    print(f'\n')
    for pro in p:
        print(f'\t{i}) {pro.get_details()}')
        i += 1
    
    pronum = input(f'\n\tType the number of the product to be removed: ')
    pro = Products.products[int(pronum)]

    if Products.remove_product(pro):
        print(f'\t\tProduct removed successfully!')
    else:
        print(f'\t\tProduct not found!')


def displayProducts():
    logging.debug(f'displayProducts() ...')

    Products.list_products()


#---------------------------------------------

def placeOrder():
    logging.debug(f'placeOrder() ...')

    p = Products.load_products()
    
    if len(p) == 0: 
        print(f'\tAdd some products to the order catalog!')
        return

    # set the number for the option to exit the menu for adding products to the order
    exitnum = len(p)
    
    # set up the vars for the order object constructor
    productsorder = []
    quantitiesorder = []
    address = ""
    
    # fill the address
    address = input(f'\n\tType your address: ')

    print(f'\n')

    # print all products avaliable in the shop
    for i, pro in enumerate(p):
        print(f'\t{i}) {pro.get_details()}')

    print(f'\t{exitnum}) --- End Order ---')

    # loop to add more than one product
    while True:

        # error handlelinng for product selection
        try:
            prodnum = int(input(f'\n\tType the number of the product to be ordered: '))
        except ValueError:
            print('\n\t\t***INVALID INPUT: Please enter a valid number.')
            continue
        
        # if user want to exit 
        if prodnum == exitnum:
            # exit while loop
            break
        # make sure user selected a product 
        elif 0 <= prodnum < len(p):
            
            # set up a var outside de loop to retrieve user choice
            quan = 0
            
            # loop to select quantities for this product
            while True:
                try:
                    quan = int(input(f'\n\tType how many of this product you want to order: '))
                    
                    if quan > 0:
                        break
                    else:
                        print(f'\n\t\t***INVALID INPUT: Quantity needs to be greater than 0, try again!')
                except ValueError:
                    print('\n\t\t***INVALID INPUT: Please enter a valid number.')

            # append products and quantities to list
            productsorder.append(p[prodnum])
            quantitiesorder.append(quan)
        
        else:
            print('\n\t\t***INVALID INPUT: Please enter a valid product number.')

    # create order with the parameters the user filled in the step by step before
    o = Order(productsorder, quantitiesorder, address)

    # check return code of the process of adding a new order 
    if Orders.add_order(o):
        print(f'\t\tOrder added successfully')
    else:
        print(f'\t\tThere was an error while processing your order! ...')

def displayOrders():
    logging.debug(f'displayOrders() ...')

    Orders.list_orders()
    
def exit_loop():
    logging.debug(f'exit_loop() ...')
    exit(0)

#---------------------------------------------
# Error handler funct
#---------------------------------------------

def error_handler():
    logging.debug(f'error_handler() ...')
    print("This operation does not exist ...")

#---------------------------------------------
# Main funct
#---------------------------------------------

def main():
    logging.debug(f'main() ...')

    menuList = [
        '1. Add a category',
        '2. Remove a category',
        '3. Display all the categories',
        '4. Add a product',
        '5. Remove a product',
        '6. Display all the products',
        '7. Place a new order',
        '8. Display all orders',
        '9. Exit'
    ]

    operations = { 1 : addCategory, 2 : removeCategory, 
                   3 : displayCategories, 4 : addProduct,
                   5 : removeProduct, 6 : displayProducts,
                   7 : placeOrder, 8 : displayOrders, 9 : exit_loop}
    
    #Header 
    print(f'\n{"*" * 50}\n')
    
    while True:
        

        for menu in menuList:
            print(menu)
        
        print(f'\n{"*" * 50}\n')
        
        op = int( input("\nEnter your operation:") )
        func = operations.get(op, error_handler)
        

        func()

        print(f'\n{"*" * 50}\n')
        #Clear de console
        

#---------------------------------------------
# Check if runnig as a script, not as a module
#---------------------------------------------
if __name__ == '__main__':
    setupLogging(logging.INFO)
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        test_main()
    else:
        main()
