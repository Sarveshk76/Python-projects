class Error(Exception):
    pass
class votingAge(Error):
    pass
try:
        age = 21
        print("Age: ",age)
        if age>18:
            print("You are allowed to vote")
        else:
            raise votingAge
except votingAge:
        print("You are not allowed to vote")