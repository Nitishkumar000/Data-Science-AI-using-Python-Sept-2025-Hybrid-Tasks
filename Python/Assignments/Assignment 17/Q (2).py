class Student:
    def __init__(self, student_id, name, age, percentage):
        self.StudentId = student_id
        self.Name = name
        self.Age = age
        self.Percentage = percentage

    def accept(self):
        self.StudentId = int(input("Enter Student ID: "))
        self.Name = input("Enter Name: ")
        self.Age = int(input("Enter Age: "))
        self.Percentage = float(input("Enter Percentage: "))

    def display(self):
        print("Student ID:", self.StudentId)
        print("Name:", self.Name)
        print("Age:", self.Age)
        print("Percentage:", self.Percentage)

    def calculateRank(self):
        if self.Percentage >= 75:
            return "Distinction"
        elif self.Percentage >= 60:
            return "First Class"
        elif self.Percentage >= 40:
            return "Pass"
        else:
            return "Fail"

    def __str__(self):
        return f"{self.StudentId}, {self.Name}, {self.Age}, {self.Percentage}"

class EnggStudent(Student):

    # i. Parameterized Constructor
    def __init__(self, student_id, name, age, percentage, branch, internal_marks):
        super().__init__(student_id, name, age, percentage)
        self.Branch = branch
        self.InternalMarks = internal_marks

    # iii. Accept method
    def accept(self):
        super().accept()
        self.Branch = input("Enter Branch: ")
        self.InternalMarks = int(input("Enter Internal Marks: "))

    # ii. Display method
    def display(self):
        super().display()
        print("Branch:", self.Branch)
        print("Internal Marks:", self.InternalMarks)
        print("Rank:", self.calculateRank())

    # iv. Override calculateRank method
    def calculateRank(self):
        if self.Percentage >= 75 and self.InternalMarks >= 40:
            return "Distinction"
        elif self.Percentage >= 60 and self.InternalMarks >= 35:
            return "First Class"
        elif self.Percentage >= 40 and self.InternalMarks >= 30:
            return "Pass"
        else:
            return "Fail"

    # v. Override __str__ method
    def __str__(self):
        return (f"StudentId: {self.StudentId}, Name: {self.Name}, Age: {self.Age}, "
                f"Percentage: {self.Percentage}, Branch: {self.Branch}, "
                f"InternalMarks: {self.InternalMarks}, Rank: {self.calculateRank()}")

class EnggStudent(Student):

    # i. Parameterized Constructor
    def __init__(self, student_id, name, age, percentage, branch, internal_marks):
        super().__init__(student_id, name, age, percentage)
        self.Branch = branch
        self.InternalMarks = internal_marks

    # iii. Accept method
    def accept(self):
        super().accept()
        self.Branch = input("Enter Branch: ")
        self.InternalMarks = int(input("Enter Internal Marks: "))

    # ii. Display method
    def display(self):
        super().display()
        print("Branch:", self.Branch)
        print("Internal Marks:", self.InternalMarks)
        print("Rank:", self.calculateRank())

    # iv. Override calculateRank method
    def calculateRank(self):
        if self.Percentage >= 75 and self.InternalMarks >= 40:
            return "Distinction"
        elif self.Percentage >= 60 and self.InternalMarks >= 35:
            return "First Class"
        elif self.Percentage >= 40 and self.InternalMarks >= 30:
            return "Pass"
        else:
            return "Fail"

    # v. Override __str__ method
    def __str__(self):
        return (f"StudentId: {self.StudentId}, Name: {self.Name}, Age: {self.Age}, "
                f"Percentage: {self.Percentage}, Branch: {self.Branch}, "
                f"InternalMarks: {self.InternalMarks}, Rank: {self.calculateRank()}")

e1 = EnggStudent(201, "Amit", 21, 72.5, "Computer", 45)
e1.display()
print(e1)
