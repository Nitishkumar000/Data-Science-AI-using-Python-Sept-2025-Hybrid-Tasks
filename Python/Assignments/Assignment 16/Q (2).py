#Create a class Product with members as pid,pname,price and quantity .Add following methods:
#e. Constructor (Support both parameterized and parameterless)
#f. Destructor
#g. ShowBook
#h. Add static member discount.
#i. Provide methods for applying discount on price of product.

class Product:
    # Static variable
    discount = 10   # discount in percentage

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

    # Method to apply discount
    def apply_discount(self):
        if self.price is not None:
            discount_amount = (self.price * Product.discount) / 100
            self.price -= discount_amount
p1 = Product(201, "Keyboard", 1000, 2)
p1.ShowBook()

p1.apply_discount()
print("After Discount:")
p1.ShowBook()
