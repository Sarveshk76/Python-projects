s=int(input("Enter Some Number : "))
m=2*s-2
for i in range(0,s+1):
    for j in range(0,m):
        print(end=" ")
    m=m-1
    for k in range(1,i+1):
        print(i,end=" ")
    print("")