#Create a class Distance with data members as km,m and cm and add following methods :
#a. Constructor
#b. Destructor
#c. Overload +,- operator

class Distance:
    
    # a. Constructor
    def __init__(self, km, m, cm):
        self.km = km
        self.m = m
        self.cm = cm

    # b. Destructor
    def __del__(self):
        print("Distance object destroyed")

    # Normalize distance
    def normalize(self):
        self.m += self.cm // 100
        self.cm = self.cm % 100
        self.km += self.m // 1000
        self.m = self.m % 1000

    # c. Overload + operator
    def __add__(self, other):
        km = self.km + other.km
        m = self.m + other.m
        cm = self.cm + other.cm
        result = Distance(km, m, cm)
        result.normalize()
        return result

    # c. Overload - operator
    def __sub__(self, other):
        total1 = self.km*100000 + self.m*100 + self.cm
        total2 = other.km*100000 + other.m*100 + other.cm
        diff = abs(total1 - total2)

        km = diff // 100000
        diff %= 100000
        m = diff // 100
        cm = diff % 100

        return Distance(km, m, cm)

    def __str__(self):
        return f"{self.km} km {self.m} m {self.cm} cm"
d1 = Distance(2, 500, 80)
d2 = Distance(1, 750, 40)

print("Addition:", d1 + d2)
print("Subtraction:", d1 - d2)
