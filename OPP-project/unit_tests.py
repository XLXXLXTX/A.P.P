import unittest
from classes.category import Category
from classes.categories import Categories
from classes.products import Products
from classes.product import Product
from classes.amplifier import Amplifier
from classes.receiver import Receiver
from classes.turntable import Turntable
from classes.order import Order
from classes.orders import Orders

class TestOPPProject(unittest.TestCase):

    def test_product(self):
        # Aquí va tu código de prueba para productos
        with self.assertRaises(TypeError):
            product = Product()

    def test_receiver(self):
        name, price, num_channels, color, size = "Test Receiver", 100.0, 200, "red", "Medium"

        receiver = Receiver(name, price, num_channels, color, size)
        
        self.assertEqual(receiver._type, "Receiver")
        self.assertEqual(receiver.name, "Test Receiver")
        self.assertEqual(receiver.price, 100.0)
        self.assertEqual(receiver.num_channels, 200)
        self.assertEqual(receiver.color, "red")
        self.assertEqual(receiver.size, "Medium")

    def test_turntable(self):
        name, price, speed, connection_type, size = "Test Turntable", 100.0, 200, "wired", "Medium"
        
        turntable = Turntable(name, price, speed, connection_type, size)
        
        self.assertEqual(turntable._type, "Turntable")
        self.assertEqual(turntable.name, "Test Turntable")
        self.assertEqual(turntable.price, 100.0)
        self.assertEqual(turntable.speed, 200)
        self.assertEqual(turntable.connection_type, "wired")
        self.assertEqual(turntable.size, "Medium")   


        with self.assertRaises(ValueError):
            turntable_error = Turntable("Test Turntable", 100, 200, "invalid", "large")      

    def test_amplifier(self):
        name, price, num_channels, color, size = "Test Amplifier", 100.0, 200, "red", "Medium"

        receiver = Receiver(name, price, num_channels, color, size)

        self.assertEqual(receiver._type, "Receiver")
        self.assertEqual(receiver.name, "Test Amplifier")
        self.assertEqual(receiver.price, 100.0)
        self.assertEqual(receiver.num_channels, 200)
        self.assertEqual(receiver.color, "red")
        self.assertEqual(receiver.size, "Medium")

    def test_all_products(self):

        products = Products()

        r = Receiver("Test Receiver", 100.0, 200, "red", "Medium")
        t = Turntable("Test Turntable", 100.0, 200, "wired", "Medium")
        a = Amplifier("Test Amplifier", 100.0, 200, "red", "Medium")

        products.add_product(r)
        products.add_product(t)
        products.add_product(a)

        lpAdd = products.load_products()

        self.assertEqual(len(lpAdd), 3)

        products.remove_product(r)
        products.remove_product(t)
        products.remove_product(a)

        lpRem = products.load_products()

        self.assertEqual(len(lpRem), 0)

    def test_category(self):
        category = Category("Test Category")

        self.assertEqual(category.name, "Test Category")

    def test_order(self):
        
        products = [
                Receiver("Test Receiver", 100.0, 200, "red", "Medium"),
                Turntable("Test Turntable", 100.0, 200, "wired", "Medium"),
                Amplifier("Test Amplifier", 100.0, 200, "red", "Medium")
            ]

        quantities = [1, 2, 3]

        order = Order(products, quantities, "Test address")

        self.assertEqual(order.products, products)
        self.assertEqual(order.quantities, quantities)
        self.assertEqual(order.address, "Test address")
        self.assertEqual( len(order.products) + len(order.quantities), len(products) + len(quantities) )

    def test_orders_decoder(self):

        orders = Orders()

        products = [
                Receiver("Test Receiver", 100.0, 200, "red", "Medium"),
                Turntable("Test Turntable", 100.0, 200, "wired", "Medium"),
                Amplifier("Test Amplifier", 100.0, 200, "red", "Medium")
            ]

        quantities = [1, 2, 3]
        address = "Test address"
        order = Order(products, quantities, address)

        orders.add_order(order)

        lo = orders.load_orders()

        self.assertEqual(len(lo), 1)
        
        lo = orders.load_orders()

        self.assertEqual(lo[0].products[0]["name"], products[0].name)
        self.assertEqual(lo[0].products[1]["name"], products[1].name)
        self.assertEqual(lo[0].products[2]["name"], products[2].name)
        self.assertEqual(lo[0].quantities[0], quantities[0])
        self.assertEqual(lo[0].quantities[1], quantities[1])
        self.assertEqual(lo[0].quantities[2], quantities[2])
        self.assertEqual(lo[0].address, address)


if __name__ == '__main__':

    # delete the content of products.txt, orders.txt and categories.txt
    open("./products.txt", "w").close()
    open("./orders.txt", "w").close()
    open("./categories.txt", "w").close()

    # run the tests
    unittest.main()