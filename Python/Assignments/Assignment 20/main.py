from sy import SYMarks
from ty import TYMarks
from student import Student

sy = SYMarks(25, 60, 55)
ty = TYMarks(20, 30)

student = Student(101, "Rahul Patil", sy, ty)
student.calculate_result()
