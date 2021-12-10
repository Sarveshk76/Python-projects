class Student:
    V=0
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display(self):
        print(self.name,self.marks)
    def __add__(self,S):
        obj=Student(S.name,[])
        for i in range(len(self.marks)):
            obj.marks.append(self.marks[i]+S.marks[i])
        return obj
    def __sub__(self,S):
        obj=Student(S.name,[])
        for i in range(len(self.marks)):
            obj.marks.append(self.marks[i]-S.marks[i])
        return obj
    def __mul__(self, S):
        obj=Student(S.name,[])
        for i in range(len(self.marks)):
            obj.marks.append((self.marks[i]) * (S.marks[i]))
        return obj
    def __truediv__(self, S):
        obj = Student(S.name, [])
        for i in range(len(self.marks)):
            obj.marks.append(self.marks[i] / S.marks[i])
        return obj
    def Address(local,perm):
       dict = {'Local address':local,'Permenant address':perm}
       print(dict)
S1=Student("Student ",[50,31,42])
S2=Student("Student ",[45,46,47])
S1.display()
S2.display()
print("Addition: ")
S3=(Student("", []))
S3=S1+S2
str(S3.display())
print("Substraction: ")
S4=(Student("", []))
S4=S1-S2
str(S4.display())
print("Multiplication: ")
S5=(Student("", []))
S5=S1*S2
str(S5.display())
print("Division: ")
S6=(Student("", []))
S6=S1/S2
str(S6.display())
print("Address : ")
S7 = Student.Address("Pune","Nashik")
print("Class name: ",S1.__class__.__name__)
print("Module name: ",S1.__module__)