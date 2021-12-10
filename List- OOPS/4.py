class store:
    n = 0
    prCode=0
    prName=0
    prPrice=0
    id = 0
    qua = 0
    amt = 0
    def __init__(self):
        self.prCode = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.prName = ['Tshirt-1', 'Shirt-1', 'Shorts-1', 'Jeans-1', 'Tshirt-2', 'Shirt-2', 'Shorts-2', '  Hat  ',
                       ' Shoes', 'Watch']
        self.prPrice = [250, 450, 350, 700, 350, 550, 400, 200, 900, 999]
    def prOrder(self):
        self.n = int(input("Enter no. of items to buy: "))
        self.id = []
        self.qua = []
        self.amt = []
        for i in range (0,self.n):
            self.id.append(input("Enter product id: "))
            self.qua.append(input("Enter product quantity: "))

    def prDisplay(self):
        print("Product id\t\tProduct Name\t\tPrice")
        for i in range(len(self.prCode)):
            print("\t", self.prCode[i], "\t\t\t", self.prName[i], "\t\t\t", self.prPrice[i])

    def prBill(self):
        print('  ORDER-BILL  '.center(60, '-'))
        print("Product id\t\tProduct Name\t\tQua.\t\tAmount")
        for i in range (0,self.n):
            self.amt.append(int(self.prPrice[int(self.id[i])-1]) * int(self.qua[i]))
            print("\t",self.id[i],"\t\t\t",self.prName[int(self.id[i])-1],"\t\t\t",self.qua[i],"\t\t\t",self.amt[i])
        print(60*"-")
        print("\t\t\t\t\t\t\t\t Total amount : ",sum(self.amt))
        print(60 * "-")
obj = store()
obj.prDisplay()
obj.prOrder()
obj.prBill()