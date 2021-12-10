sum=0
n = int(input('Enter a value of Nth Natural Number: '))
if n==0 or n==1:
    print("Please enter a valid number.")
else:
    for i in range(1,n+1,):
        sum=i+sum
    print("The sum of ",n," natural number is ",sum)