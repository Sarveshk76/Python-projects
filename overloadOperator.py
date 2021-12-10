class divideByZero(Exception):
    pass
class Fraction:
    def __init__(self,num):
        self.num = num
    def __itruediv__(self, other):
        self.num /= other.num
        return self
num1 = int(input("Enter Nummerator:"))
num2 = int(input("Enter Denominator:"))
try:
    f1 = Fraction(num1)
    f2 = Fraction(num2)
    f1 /= f2
    if f2==0:
        raise divideByZero
except :
    print("Divided by zero")
else:
    print(f1.num)