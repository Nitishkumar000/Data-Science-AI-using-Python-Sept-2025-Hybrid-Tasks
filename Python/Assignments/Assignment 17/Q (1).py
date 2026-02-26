
class Student:
    # i. Parameterized Constructor
    def __init__(self, student_id, name, age, percentage):
        self.StudentId = student_id
        self.Name = name
        self.Age = age
        self.Percentage = percentage

    # iii. Accept method
    def accept(self):
        self.StudentId = int(input("Enter Student ID: "))
        self.Name = input("Enter Name: ")
        self.Age = int(input("Enter Age: "))
        self.Percentage = float(input("Enter Percentage: "))

    # ii. Display method
    def display(self):
        print("Student ID:", self.StudentId)
        print("Name:", self.Name)
        print("Age:", self.Age)
        print("Percentage:", self.Percentage)

    # iv. Calculate Rank method
    def calculateRank(self):
        if self.Percentage >= 75:
            return "Distinction"
        elif self.Percentage >= 60:
            return "First Class"
        elif self.Percentage >= 50:
            return "Second Class"
        elif self.Percentage >= 40:
            return "Pass"
        else:
            return "Fail"

    # v. Override __str__ method
    def __str__(self):
        return (f"StudentId: {self.StudentId}, "
                f"Name: {self.Name}, "
                f"Age: {self.Age}, "
                f"Percentage: {self.Percentage}, "
                f"Rank: {self.calculateRank()}")

s1 = Student(101, "Rahul", 20, 78.5)
s1.display()
print(s1)
