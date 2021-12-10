class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    print(name, age)
class Child(Person):
  def __init__(self):
    super().__init__(self)
p1 = Person("John", 36)
p2 = Child()
