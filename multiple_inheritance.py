class animal:
    def __init__(self, specie):
        self.specie = specie
    def printf1(self):
        print("This is a '",self.specie,"' class")
class dog(animal):
    def __init__(self,specie):
        super().__init__(specie)
    def printf2(self):
        print("This is a '",self.specie,"' class")
class cat(animal):
    def __init__(self,specie):
        super().__init__(specie)
    def printf3(self):
        print("This is a '",self.specie,"' class")

obj = animal('animal')
obj.printf1()
obj1 = dog('dog')
obj1.printf2()
obj2 = cat('cat')
obj2.printf3()