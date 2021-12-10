class polygon:
    def __init__(self):
        print("Polygon class")
    def area(self):
        pass
class rectangle(polygon):
    def __init__(self):
        print("Rectangle class")
    def area(self,l,b):
        print("Area of rectangle: ",l*b)
class traingle:
    def __init__(self):
        print("Triangle class")
    def area(self,b,h):
        area = (1/2) *b*h
        print("Area of Triangle: ",area)
obj = polygon()
obj1 = rectangle()
obj1.area(10,5)
obj2 = traingle()
obj2.area(10,5)

