class Error(Exception):
    pass
class valueLarge(Error):
    pass
class valueSmall(Error):
    pass
num = 10
while True:
    try:
        guess = int(input("Guess the number: "))
        if guess<num:
            raise valueSmall
        elif guess==num:
            print("You guessed it right")
            break
        else:
            raise valueLarge
    except valueSmall:
        print("Number is greater than you guessed")
    except valueLarge:
        print("Number is less than you guessed")

