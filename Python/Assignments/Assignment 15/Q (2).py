#Create a class Product with members as pid,pname,price and quantity .Add following methods:
#d. Constructor (Support both parameterized and parameterless)
#e. Destructor
#f. ShowBook

class Product:
    # Constructor (parameterized + parameterless)
    def __init__(self, pid=None, pname=None, price=None, quantity=None):
        self.pid = pid
        self.pname = pname
        self.price = price
        self.quantity = quantity

    # Destructor
    def __del__(self):
        print("Product object destroyed")

    # ShowBook method (as per question)
    def ShowBook(self):
        print("Product ID:", self.pid)
        print("Product Name:", self.pname)
        print("Price:", self.price)
        print("Quantity:", self.quantity)
p1 = Product(201, "Mouse", 500, 10)
p1.ShowBook()
p2 = Product()
p2.ShowBook()



