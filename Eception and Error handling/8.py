import re
class authorError(Exception):
    pass
class priceError(Exception):
    pass
try:
    def library(name,price):
        print("Book Details".center(20,"-"))
        Author = bool(re.fullmatch('[A-Za-z]{2,15}( [A-Za-z]{2,15})?',name))
        Price = bool(re.fullmatch("(\d{1,2})(?:[,]\d{3})|(\d{3})", price))
        #print(Author)
        #print(Price)
        if Author==False:
            raise authorError
        elif Price==False:
            raise priceError
        else:
            print("Author: ",name)
            print("Price: ",price," ₹")

    library("Sarvesh Kulkarni","198")
    library("Sarvesh Kulkarni","1,198")
    #library("Sarvesh Kulkarni","11,98")
    library("$arvesh Kulkarni", "1,198")
except authorError:
    print("Invalid auther name format")
except priceError:
    print("Invalid price format")
