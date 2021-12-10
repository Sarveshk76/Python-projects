class Employee:
    def __init__(self, name, des, sal):
        self.name = name
        self.des = des
        self.sal = sal
    def Display(self):
        print("Employee name: ",self.name)
        print("Employee designation: ",self.des)
        print("Employee salary: ",self.sal)
obj = Employee("Sarvesh","Jr programmer",20000)
obj.Display()