import re
string = "Write a program that has a class store which keeps a record of code and price of each product. Display a menu of all products to the user and prompt him to enter the quantity of each item required. 12 08 2021 Generate a bill and display the total amount. XYZ@python.com"
pat =  r"\d{2} \d{2} \d{4}"
pat1 = r"\d{4}"
res = re.search(pat,string)
res1 = re.search(pat1,string)
print("Date: ",res.group())
print("Year: ",res1.group())