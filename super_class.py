class Person:
  def __init__(self, fname, lname):
    self.fname = fname
    self.lname = lname
  def printname(self):
    print(self.fname, self.lname)
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)

obj = Person("First name, ", " Last name")
obj.printname()
obj1 = Student("Sarvesh, "," Kulkarni")
obj1.printname()

a = 1
def add_func():
global a
a = a+1
print(“Inside the function”,a)
add_func()
print(“In main after a change in the value of the variable”, a)