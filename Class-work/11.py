def avg(num):
    sum = 0
    for i in range(num+1):
        sum = sum + i
    aveg = sum/num
    print(aveg)
x = int(input("Enter the number: "))
print("The average of ",x," natural numebrs: ")
avg(x)