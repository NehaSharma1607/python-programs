# 1)Write a Python class named Student with two attributes student_id, student_name.
# Add a new attribute student_class and display the entire attribute and their values of
# the said class. Now remove the student_name attribute and display the entire
# attribute with values
class Student(object):
    def __init__(self, student_name, student_id, student_class):
        self.name = student_name
        self.id = student_id
        self.cls=student_class
student_one = Student('Rolf Smith', 52, 812)
print("After adding")
print("UId: {1},    Name:{0},      class: {2}"
      .format(student_one.name,student_one.id,student_one.cls))
print("After deleting")
del student_one.name
print("UId: {1},    Class:{0}     "
      .format(student_one.cls,student_one.id))

#2
class py_solution:
  def twoSum(self, nums, target):
       lookup = {}
       for i, num in enumerate(nums):
           if target - num in lookup:
               return (lookup[target - num], i )
           lookup[num] = i
print("index1=%d, index2=%d" % py_solution().twoSum((10,20,10,40,50,60,70),50))
