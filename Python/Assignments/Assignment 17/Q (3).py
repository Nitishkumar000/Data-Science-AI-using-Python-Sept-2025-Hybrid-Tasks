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
        print("Student ID :", self.StudentId)
        print("Name       :", self.Name)
        print("Age        :", self.Age)
        print("Percentage :", self.Percentage)

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

class MedicalStudent(Student):

    # i. Parameterized Constructor
    def __init__(self, student_id, name, age, percentage, specialization, internship_marks):
        super().__init__(student_id, name, age, percentage)
        self.Specialization = specialization
        self.MarksOfInternship = internship_marks

    # iii. Accept method
    def accept(self):
        super().accept()
        self.Specialization = input("Enter Specialization: ")
        self.MarksOfInternship = int(input("Enter Internship Marks: "))

    # ii. Display method
    def display(self):
        super().display()
        print("Specialization      :", self.Specialization)
        print("Internship Marks    :", self.MarksOfInternship)
        print("Rank                :", self.calculateRank())

    # iv. Override calculateRank method
    def calculateRank(self):
        if self.Percentage >= 70 and self.MarksOfInternship >= 60:
            return "Excellent"
        elif self.Percentage >= 60 and self.MarksOfInternship >= 50:
            return "Very Good"
        elif self.Percentage >= 50 and self.MarksOfInternship >= 40:
            return "Good"
        else:
            return "Fail"

    # v. Override __str__ method
    def __str__(self):
        return (f"StudentId: {self.StudentId}, Name: {self.Name}, Age: {self.Age}, "
                f"Percentage: {self.Percentage}, Specialization: {self.Specialization}, "
                f"InternshipMarks: {self.MarksOfInternship}, Rank: {self.calculateRank()}")

m = MedicalStudent(301, "Sneha", 23, 72.5, "Cardiology", 65)
m.display()
print(m)
