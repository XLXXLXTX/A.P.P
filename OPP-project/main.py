# impor from classes folder each file
from classes.category import Category
from classes.categories import Categories
#from classes.products import Products
from classes.product import Product
from classes.amplifier import Amplifier
#from classes.orders import Orders
from classes.receiver import Receiver
from classes.turntable import Turntable

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
    
    catnum = input(f'\n\tType the number of the category to be removed: ')
    cat = Categories.categories[int(catnum)]

    if Categories.remove_category(cat):
        print(f'\t\tCategory removed successfully!')
    else:
        print(f'\t\tCategory not found!')


def displayCategories():
    logging.debug(f'displayCategories() ...')

    Categories.list_categories()

def addProduct():
    logging.debug(f'addProduct() ...')

def removeProduct():
    logging.debug(f'removeProduct() ...')

def displayProducts():
    logging.debug(f'displayProducts() ...')

def placeOrder():
    logging.debug(f'placeOrder() ...')

def displayOrders():
    logging.debug(f'displayOrders() ...')

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
        
        op = int(input("\nEnter your operation:"))
        func = operations.get(op, error_handler)
        

        func()

        print(f'\n{"*" * 50}\n')
        #Clear de console
        

#---------------------------------------------
# Check if runnig as a script, not as a module
#---------------------------------------------
if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        test_main()
    else:
        setupLogging(logging.INFO)
        main()
