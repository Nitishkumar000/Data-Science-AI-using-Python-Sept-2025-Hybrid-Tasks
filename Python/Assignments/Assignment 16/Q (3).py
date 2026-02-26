#3. Create a class Shirt with members as sid,sname,type(formal etc), price and size(small,large etc) .Add following methods:
#j. Constructor (Support both parameterized and parameterless)
#k. Destructor
#l. ShowBook
#m. For each size of shirt price should change by 10%.
#(eg. If 1000 is price then small price = 1000, medium = 1100,large=1200 and xlarge=1300) Use static concept.

class Shirt:
    # Static dictionary 
    size_increment = {
        "small": 0,
        "medium": 10,
        "large": 20,
        "xlarge": 30
    }

    # Constructor 
    def __init__(self, sid=None, sname=None, type=None, price=None, size="small"):
        self.sid = sid
        self.sname = sname
        self.type = type
        self.base_price = price   
        self.size = size
        self.price = price

        if price is not None:
            self.apply_size_price()

    # Destructor
    def __del__(self):
        print("Shirt object destroyed")

    # Static method 
    @staticmethod
    def calculate_price(price, size):
        increment = Shirt.size_increment.get(size.lower(), 0)
        return price + (price * increment / 100)

    # Method to apply size-based price
    def apply_size_price(self):
        self.price = Shirt.calculate_price(self.base_price, self.size)

    # ShowBook method 
    def ShowBook(self):
        print("Shirt ID:", self.sid)
        print("Shirt Name:", self.sname)
        print("Type:", self.type)
        print("Size:", self.size)
        print("Price:", self.price)
s1 = Shirt(301, "Raymond", "Formal", 1000, "small")
s2 = Shirt(302, "Peter England", "Casual", 1000, "medium")
s3 = Shirt(303, "Allen Solly", "Formal", 1000, "large")
s4 = Shirt(304, "Van Heusen", "Formal", 1000, "xlarge")

s1.ShowBook()
s2.ShowBook()
s3.ShowBook()
s4.ShowBook()
