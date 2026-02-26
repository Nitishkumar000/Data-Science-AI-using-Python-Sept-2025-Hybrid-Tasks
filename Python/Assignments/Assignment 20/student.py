from sy import SYMarks
from ty import TYMarks

class Student:
    def __init__(self, roll_no, name, sy_marks, ty_marks):
        self.roll_no = roll_no
        self.name = name
        self.sy_marks = sy_marks
        self.ty_marks = ty_marks

    def calculate_result(self):
        total_computer = (
            self.sy_marks.computer +
            self.ty_marks.theory +
            self.ty_marks.practical
        )

        if total_computer >= 70:
            grade = "A"
        elif total_computer >= 60:
            grade = "B"
        elif total_computer >= 50:
            grade = "C"
        elif total_computer >= 40:
            grade = "Pass Class"
        else:
            grade = "Fail"

        print("----- Student Result -----")
        print("Roll No :", self.roll_no)
        print("Name    :", self.name)
        print("Total Computer Marks :", total_computer)
        print("Grade   :", grade)

        