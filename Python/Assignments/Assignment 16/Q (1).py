#1. Create a class Book with members as bid,bname,price and author.Add following methods:
#a. Constructor (Support both parameterized and parameterless)
#b. Destructor
#c. ShowBook
#d. Add static variable count and also maintain count of objects created.
class Book:
    # Static variable
    count = 0

    # Constructor 
    def __init__(self, bid=None, bname=None, price=None, author=None):
        self.bid = bid
        self.bname = bname
        self.price = price
        self.author = author
        Book.count += 1   

    # Destructor
    def __del__(self):
        print("Book object destroyed")

    # ShowBook method
    def ShowBook(self):
        print("Book ID:", self.bid)
        print("Book Name:", self.bname)
        print("Price:", self.price)
        print("Author:", self.author)

    # Static method 
    @staticmethod
    def show_count():
        print("Total Book objects created:", Book.count)
b1 = Book(101, "Python", 500, "Guido")
b2 = Book(102, "Java", 450, "James")

b1.ShowBook()
Book.show_count()
