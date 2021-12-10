class Error(Exception):
    pass
class foundDigit(Error):
    pass
class noDigit(Error):
    pass
try:
        a = "123".isdigit()

        if a==True:
            print("for a")
            raise foundDigit
        else:
            print("for a")
            raise noDigit
except foundDigit:
        print("Integer found")
except noDigit:
        print("Non-Integer found")