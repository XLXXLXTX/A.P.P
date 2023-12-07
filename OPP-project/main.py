# Advanced Python Programming - OPP Project | Author: Javier Pardos | javier.pardos10@e-uvt.ro

from typing import List

# impor from classes folder each file
from classes.category import Category
from classes.categories import Categories

from classes.product import Product
from classes.products import Products
from classes.amplifier import Amplifier
from classes.receiver import Receiver
from classes.turntable import Turntable

from classes.order import Order
from classes.orders import Orders

#---------------------------------------------
# DEBUG
#---------------------------------------------
import logging

#---------------------------------------------
# LOGGING - Setup
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
# MENU UTILS - Logic functs 
#---------------------------------------------

def printNumberedMenu( list :list) -> None:
    logging.debug(f'printNumberedMenu() ...')

    # print all element on a numbered list

    for i, element in enumerate(list):
        print(f'\t{i}) {element.name}')

def setProductForOrder(products :List[Product] ) -> Product:
    while True:
        try:
            prodnum = int( input(f'\n\tType the number of the product to be ordered: ') )
        except ValueError:
            print('\n\t\t***INVALID INPUT: Please enter a valid number.')
            continue
        
        # make sure user selected a product from the list
        if 0 <= prodnum < len(products):
            return products[prodnum]
        elif prodnum == len(products):
            return None
        else:
            print('\n\t\t***INVALID INPUT: Please enter a valid product number.')

def setQuantityForOrder() -> int:
    while True:
        try:
            quan = int(input(f'\n\tType how many of this product you want to order: '))
            
            # make sure quantity is greater than 0
            if quan > 0:
                return quan
            else:
                print(f'\n\t\t***INVALID INPUT: Quantity needs to be greater than 0, try again!')
        except ValueError:
            print('\n\t\t***INVALID INPUT: Please enter a valid number.')

#---------------------------------------------
# CATEGORY - Logic functs 
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

    loadC = Categories.load_categories()

    if len(loadC) == 0:
        print(f'\tAdd some categories to the catalog!')
        return

    printNumberedMenu(Categories.load_categories())
    
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
# PRODUCT - Logic functs 
#---------------------------------------------
def addProduct():
    logging.debug(f'addProduct() ...')

    types_of_products = {1 : Amplifier, 2 : Receiver, 3 : Turntable}
    
    # list the types of products
    for t in types_of_products:
        print(f'\t{t}) {types_of_products[t].__name__}')
    
    p = int(input(f'\n\tType the number of the product to: '))
    
    # check if the product type exists
    if p not in types_of_products:
        print(f'\t\tProduct not found!')
        return

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

    loadP = Products.load_products()

    if len(loadP) == 0:
        print(f'\tAdd some products to the catalog!')
        return

    printNumberedMenu(loadP)

    pronum = int( input(f'\n\tType the number of the product to be removed: ') )
    
    pro = Products.products[int(pronum)]

    if Products.remove_product(pro):
        print(f'\t\tProduct removed successfully!')
    else:
        print(f'\t\tProduct not found!')

def displayProducts():
    logging.debug(f'displayProducts() ...')

    Products.list_products()

#---------------------------------------------
# ORDER - Logic functs 
#---------------------------------------------
def placeOrder():
    logging.debug(f'placeOrder() ...')

    products = Products.load_products()

    # make sure the shop has products to order
    if len(products) == 0: 
        print(f'\tAdd some products to the order catalog!')
        return

    address = input(f'\n\tType your address: ')
    print(f'\n')

    # print all products avaliable in the shop
    for i, pro in enumerate(products):
        print(f'\t{i}) {pro.get_details()}')
    
    # option to exit the loop of adding products
    print(f'\t{len(products)}) --- End Order ---')

    # set up the vars for the order object constructor
    productsorder = []
    quantitiesorder = []

    # loop to add more than one product
    while True:
        product = setProductForOrder(products)
        
        # if user want to exit, product is None
        if product is None:
            break

        quantity = setQuantityForOrder()

        productsorder.append(product)
        quantitiesorder.append(quantity)
        
    # create order with the parameters the user filled in the step by step before
    order = Order(productsorder, quantitiesorder, address)

    # check return code of the process of adding a new order 
    if Orders.add_order(order):
        print(f'\t\tOrder added successfully')
    else:
        print(f'\t\tThere was an error while processing your order! ...')

def displayOrders():
    logging.debug(f'displayOrders() ...')

    Orders.list_orders()

#---------------------------------------------
# EXIT - Logic functs 
#---------------------------------------------

def exit_loop():
    logging.debug(f'exit_loop() ...')
    exit(0)

#---------------------------------------------
# Error handler funct
#---------------------------------------------

def error_handler():
    logging.debug(f'error_handler() ...')
    print("This operation does not exist ...")


# def to create the files if they don't exist, or overwrite them if they do
def createFile(filename :str) -> None:
    logging.debug(f'checkFiles({filename}) ...')

    # open the file in write mode, which will create the file if it doesn't exist
    with open(filename, 'w') as f:
        pass

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

    # define list of filenames to check
    filenames = ['products.txt', 'categories.txt', 'orders.txt']

    # call function to check for specific files that will be used in the program
    for filename in filenames:
        createFile(filename)

    main()
