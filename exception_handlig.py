try:
    a=4/0
    print(a)
    b=[7,1]
    b[3]=9
except ZeroDivisionError:
    print("Enter number other than zero at divisor")
except IndexError:
    print("Our of index error")