from datetime import date

class Date:
    def __init__(self, d1):
        self.d1 = d1

    def __lt__(self, other):
        return self.d1 < other.d1

    def __gt__(self, other):
        return self.d1 > other.d1

    def __eq__(self, other):
        return self.d1 == other.d1

    def __le__(self, other):
        return self.d1 <= other.d1

    def __ge__(self, other):
        return self.d1 >= other.d1

    def __cmp__(self, other):
        return self.d1 == other.d1

x = date(2020, 5, 17)
y = date(2021, 8, 12)
Date(x)
Date(y)
print('x: ',x)
print('y: ',y)
print("x>y: ",x>y)
print("x<y ",x<y)
print("x>=y: ",x>=y)
print("x<=y: ",x<=y)
print("x==y: ",x==y)