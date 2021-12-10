num = int(input("Enter Some Number : "))
m=2*num+2
for i in range(1,num+1):
    for k in range(0,m):
        print(end=" ")
    m=m+1
    for j in range(i,num+1):
            print(j,end=' ')
    print()