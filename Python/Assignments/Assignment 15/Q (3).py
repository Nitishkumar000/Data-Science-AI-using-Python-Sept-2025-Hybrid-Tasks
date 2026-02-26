#Create a class Shirt with members as sid,sname,type(formal etc), price and size(small,large etc) .Add following methods:
#g. Constructor (Support both parameterized and parameterless)
#h. Destructor
#i. ShowBook

class Shirt:
    # Constructor (parameterized + parameterless)
    def __init__(self, sid=None, sname=None, type=None, price=None, size=None):
        self.sid = sid
        self.sname = sname
        self.type = type
        self.price = price
        self.size = size

    # Destructor
    def __del__(self):
        print("Shirt object destroyed")

    # ShowBook method (as per question)
    def ShowBook(self):
        print("Shirt ID:", self.sid)
        print("Shirt Name:", self.sname)
        print("Type:", self.type)
        print("Price:", self.price)
        print("Size:", self.size)
s1 = Shirt(301, "Raymond", "Formal", 1500, "Large")
s1.ShowBook()
s2 = Shirt()
s2.ShowBook()
