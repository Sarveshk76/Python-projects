# 11. Write the program to create the random 10 integers. Creates the two list -odd and even.
# Separate the value respectively.
import random
even=[]
odd=[]
for i in range(1,11):
    num = 0
    num = random.randrange(1, 50)
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)
print("Even: ", even)
print("Odd: ", odd)