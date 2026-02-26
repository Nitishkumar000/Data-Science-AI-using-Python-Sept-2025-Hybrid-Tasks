class Student:
    def __init__(self, student_id, name, age, percentage):
        self.StudentId = student_id
        self.Name = name
        self.Age = age
        self.Percentage = percentage

    def __str__(self):
        return f"{self.StudentId}, {self.Name}, {self.Age}, {self.Percentage}"


class College:
    def __init__(self, no_of_students):
        self.no_of_students = no_of_students
        self.students = []

    def addStudent(self, student):
        if len(self.students) < self.no_of_students:
            self.students.append(student)
            print("Student added")
        else:
            print("Limit reached")

    def getStudent(self, student_id):
        for s in self.students:
            if s.StudentId == student_id:
                return s
        return "Student not found"

    def removeStudent(self, student_id):
        for s in self.students:
            if s.StudentId == student_id:
                self.students.remove(s)
                print("Student removed")
                return
        print("Student not found")

    def __str__(self):
        result = "College Students:\n"
        for s in self.students:
            result += str(s) + "\n"
        return result


s1 = Student(1, "Rahul", 20, 65)
s2 = Student(2, "Anita", 21, 72)

c = College(2)
c.addStudent(s1)
c.addStudent(s2)

print(c)
