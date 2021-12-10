class abc:
    x=10
    __doc__ = "This is a __doc__"
    def _private(self):
        print("This is a private class")
        _x=5
obj = abc

print("Private method = ",)
print("__bases__ =",obj.__bases__)
print("__module__ =",obj.__module__)
print("__name__ =",obj.__name__)
print("dict = ",obj.__dict__)
print("class.__doc__ = ",obj.__doc__)
print("Before = ",obj.x)
setattr(obj,'x',50)
print("setattr = ",obj.x)
getattr(obj,'x')
print("hasattr = ",hasattr(obj,'x'))
print("getattr = ",obj.x)
delattr(obj,'x')
print(obj.x)
#write a program that uses class student which store name and marks of a student(store in list)
#also use all types of methods

#Calculate the area of triangle using class