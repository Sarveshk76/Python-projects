import re
string = "Write a program that has a class store which keeps a record of code and price of each product. Display a menu of all products to the user and prompt him to enter the quantity of each item required. 12 08 2021 Generate a bill and display the total amount. XYZ@python.com"
pat1 =  r"\d{2} \d{2} \d{4}"
pat2 =  r"^Write.*com$"
pat3 = r"[\w.-]+@[\w.-]+"
res1 = re.findall(pat1,string)
res2 = re.search(pat2,string)
res3 = re.findall(pat3,string)
print(string)
print("res1 =",res1)
if res2:
    print("Res2 = Matched")
else:
    print("Res 2 = Not matched")
print("res3 =",res3)
pat4 = r"\bW\w+"
res4 = re.search(pat4,string)
print("Res4 =",str(res4))