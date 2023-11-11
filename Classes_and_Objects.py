# objects are things that store data and actions

class Student:
    def __init__(self, new_name, new_grades):
        self.name = new_name
        self.grades = new_grades

    def average(self):
        return sum(self.grades) / len(self.grades)


student_one = Student('rolf smith', [70, 88, 90, 99])
print(student_one.name)
print(student_one.__class__)
print(student_one.average())
print(Student.average(student_one))


################################################################3


class Movie:
    def __init__(self,name,year):
        self.name=name
        self.year=year

matrix=Movie("the matrix",1994)


print(matrix.name)
print(matrix.__class__)

