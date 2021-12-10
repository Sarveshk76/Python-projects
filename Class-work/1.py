amt = int(input("Enter the amount: "))
interest = int(input("Enter the Annual interest: "))
time = int(input("Enter the number of months: "))
res = 0
for i in range (1) :
   res = amt + amt*interest/100*time/12
   print("The value of investment after ",(time/12)," year :",res)