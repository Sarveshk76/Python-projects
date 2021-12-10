from datetime import date, datetime
class Expiry:
    def __init__(self,manDate,expDate):
        self.manDate = manDate
        self.expDate = expDate
    def checkEpriry(self):
        self.manDate = datetime.strptime(str(self.manDate), "%d %m %Y")
        self.expDate = datetime.strptime(str(self.expDate), "%d %m %Y")
        today = datetime.today()
        res = abs((self.expDate-today).days)
        print("Manufacturing Date: ",self.manDate.date())
        print("Expiry Date: ",self.expDate.date())
        print("Todays Date: ",today.date())
        print(res,"days remaining for the Expiry.")
obj = Expiry("19 05 1998","19 05 2024")
obj.checkEpriry()