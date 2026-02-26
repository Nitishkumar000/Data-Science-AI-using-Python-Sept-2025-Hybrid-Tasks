#Create a class Book with members as bid,bname,price and author.Add following methods:
#a. Constructor (Support both parameterized and parameterless)
#b. Destructor
#c. ShowBook
class Book:
   
    def __init__(self, bid=None, bname=None, price=None, author=None):
        self.bid = bid
        self.bname = bname
        self.price = price
        self.author = author

    # Destructor
    def __del__(self):
        print("Book object destroyed")

    # ShowBook method
    def ShowBook(self):
        print("Book ID:", self.bid)
        print("Book Name:", self.bname)
        print("Price:", self.price)
        print("Author:", self.author)

# Example usage:
book1 = Book(1, "Python Programming", 29.99, "John Doe")
book1.ShowBook()
book2 = Book()
book2.ShowBook()
