n = int(input("Enter the start number: "))
m = int(input("Enter the end number: "))
count = 0
for i in range(n,m):
    if i > 1:
        for j in range(2,i):
            if(i % j == 0):
                break
        else:
            print(i)
            count = count + 1