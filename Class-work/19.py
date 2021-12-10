def Gcd(num1, num2):
    if num1 > num2:
        x = num2
    else:
        x = num1
    for i in range(1, x+1):
        if((num1 % i == 0) and (num2 % i == 0)):
            gcd = i
    return gcd
a=int(input('Enter number 1:'))
b=int(input('Enter number 2:'))
print("GCD of ",a," and ",b," : ",Gcd(a,b))