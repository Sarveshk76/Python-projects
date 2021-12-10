from datetime import date,datetime
class Person:
  __name = input("Enter your name: ")
  name = __name
  dob = datetime.strptime(input("Your date of birth (dd mm yyyy): "), "%d %m %Y")
  def calculate_age(d):
    today = date.today()
    return today.year - d.year
  age = calculate_age(dob)
  def isVote(age):
    if age > 18:
      print("You are allowed to vote")
    else:
      print("You are not allowed to vote")
obj = Person
print("*"*30)
print("Name: ",obj.name)
print("Age: ",obj.age,"yrs")
obj.isVote(obj.age)
print("*"*30)
print("__repr__: ",obj.name.__repr__())
print("__len__: ",obj.name.__len__())
print("__str__: ",obj.name.__str__())
print("__getitem__: ",obj.name.__getitem__(3))
setattr(obj,obj.name,"Sarvesh")
print("getattr: ",getattr(obj, obj.name))
print("hasattr: ",hasattr(obj, obj.name))
print("Before delattr: ",obj.name)

delattr(obj,"name")
print("After delattr: ",obj.name)