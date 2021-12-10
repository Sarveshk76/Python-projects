num = input("Enter a string: ")
try:
    assert num.isdigit()
except AssertionError:
    print("Non-integer value")
else:
    print("num is a Integer")