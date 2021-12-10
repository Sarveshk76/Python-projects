class animal:
    def __init__(self, specie):
        self.specie = specie
    def printf(self):
        print("This is a '",self.specie,"' class")
class dog(animal):
    def __init__(self,specie):
        animal.__init__(self, specie)
    def printf(self):
        print("This is a '",self.specie,"' class")
obj = animal('animal')
obj.printf()
obj1 = dog('dog')
obj1.printf()