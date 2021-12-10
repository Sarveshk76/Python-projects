def division(a,b):
    return a/b
try:
    a,b = 19,0
    print("a: ",a," b: ",b)
    division(a,b)
except ZeroDivisionError as z:
    print(z)
    print("Denominator should be non-zero")
else:
    print("Denominator is non-zero")
finally:
    print("Division:",division(19,0))