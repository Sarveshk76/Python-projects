def division(a,b):
    return a/b
try:
    division(19,5)
except ZeroDivisionError:
    print("Denominator should be non-zero")
else:
    print("Denominator is non-zero")
finally:
    print("Division:",division(19,5))