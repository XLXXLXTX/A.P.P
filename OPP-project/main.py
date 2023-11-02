
#---------------------------------------------
# Logic functs
#---------------------------------------------

def addCategory():
    print('addCategory ...')

def removeCategory():
    print('removeCategory ...')

def displayCategories():
    print('displayCategories ...')

def addProduct():
    print('addProduct ...')

def removeProduct():
    print('removeProduct ...')

def displayProducts():
    print('displayProducts ...')

def placeOrder():
    print('placeOrder ...')

def displayOrders():
    print('displayOrders ...')

def exit_loop():
    print('exit_loop ...')
    exit(0)

#---------------------------------------------
# Error handler funct
#---------------------------------------------

def error_handler():
    print("This operation does not exist ...")

#---------------------------------------------
# Main funct
#---------------------------------------------

def main():
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
    while True:
        
        print("\n")
        for menu in menuList:
            print(menu)
        
        op = int(input("\nEnter your operation:"))
        func = operations.get(op, error_handler)
        
        func()

#---------------------------------------------
# Check if runnig as a script, not as a module
#---------------------------------------------
if __name__ == '__main__':
    main()
