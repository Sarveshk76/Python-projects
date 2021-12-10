class payBill:
    def __init__(self,name,amt):
        self.name = name
        self.amt = amt
class payMethod(payBill):

    def __init__(self,name,amt):
        payBill.__init__(self,name, amt)
    def display(self):
        print("Name: ",self.name)
        print("Bill amount: ",self.amt)
        self.n = int(input("Choice of payment by  1.cheque or 2.cash?(choose 1 or 2):  "))
    def chosenMethod(self):
        if self.n == 1:
            print("Payment method chosen as Cheque.")
        elif self.n == 2:
            print("Payment method chosen as Cash.")
        else:
            print("Please enter either 1 or 2.",self.n)
obj = payMethod("Sarvesh","1000 Rs")
obj.display()
obj.chosenMethod()
