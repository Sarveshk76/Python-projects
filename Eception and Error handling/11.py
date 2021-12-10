Input = float(input("Enter temp. in Celsius: "))
try:
    f=(Input * 1.8) + 32
    assert f>32,"Its cold"
except AssertionError as temp:
    print(temp)
    print("Temp. is less than Normal")
else:
    print("In Celsius: ",Input," In Fahrenheit: ",f)