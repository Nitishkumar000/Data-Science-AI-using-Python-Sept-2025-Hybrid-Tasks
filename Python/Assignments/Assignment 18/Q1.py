#1. Create a class Complex Number with data members as real and imag and add following methods :
#a. Constructor
#b. Destructor
#c. Overload +,- operator

class ComplexNumber:
    
    # a. Constructor
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    # b. Destructor
    def __del__(self):
        print("ComplexNumber object destroyed")

    # c. Overload + operator
    def __add__(self, other):
        real = self.real + other.real
        imag = self.imag + other.imag
        return ComplexNumber(real, imag)

    # c. Overload - operator
    def __sub__(self, other):
        real = self.real - other.real
        imag = self.imag - other.imag
        return ComplexNumber(real, imag)

    def __str__(self):
        return f"{self.real} + {self.imag}i"
c1 = ComplexNumber(3, 4)
c2 = ComplexNumber(1, 2)

print("Addition:", c1 + c2)
print("Subtraction:", c1 - c2)