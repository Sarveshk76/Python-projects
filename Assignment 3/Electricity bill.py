name = input("Enter Consumer Name : ")
units = int(input("Enter Total Units Consumed : "))
if(units<=150):
    pay=units*3
    charge=0
    a=("0-150")
    b=("3.RS")
elif(units<=350):
    pay=(150*3)+(units-100)*3.75
    charge=100
    a = ("151-350")
    b = ("3.75.RS")
elif(units<=450):
    pay=(150*3)+(350-150)*3.75+(units-350)*4
    charge=250
    a = ("351-450")
    b = ("4.RS")
elif(units<=600):
    pay=(150*3)+(350-150)*3.75+(450-350)*4+(units-450)*4.25
    charge=300
    a = ("451-650")
    b = ("4.25.RS")
else:
    pay = (150*3)+(350-150)*3.75+(450-350)*4+(600-450)*4.25+(units-600)*5
    charge=400
    a = ("Above-651")
    b = ("5.RS")

Total=pay+charge
print('ELECTRICITY--BILL'.center(60, '*'))
print("Consumer Name\t\t\t\t:\t\t",name)
print("Range of usage\t\t\t\t:\t\t",a)
print("Per unit charge\t\t\t\t:\t\t",b)
print("Units consumed\t\t\t\t:\t\t",units)
print("Extra Charge\t\t\t\t:\t\t",charge)
print('*'.center(60,'*'))
print("Total Electicity Bill\t\t:\t\t",Total)
print('*'.center(60,'*'))