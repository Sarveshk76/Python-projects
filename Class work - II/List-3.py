import random
List = []
even = []
odd = []
print("Random List:")
for i in range(10):
     List.append(random.randrange(1,100))
print(List)
for j in List:
    if j%2==0:
        even.append(j)
    else:
        odd.append(j)
print("Even List: ",even)
print("Odd List: ",odd)