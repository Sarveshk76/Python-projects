import random
class Error(Exception):
    pass
class smallNumber(Error):
    pass
try:
    num = random.uniform(0,1)
    if num < 0.1:
        print(num)
        raise smallNumber
    else:
        print(num)
except smallNumber:
    print("Number is less than 0.1")