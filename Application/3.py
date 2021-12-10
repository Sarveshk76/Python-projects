def perfect(a):
    total = 0
    for i in range(1,a):
        if a%i == 0:
            total = total + i
    if total == a:
        print(total)
def findPerfect(m, n):
    print("The perfect numbers in the range ",m," to ",n," :")
    for i in range (m,n+1):
        x=perfect(i)
        if x==0:
            return [ ]

findPerfect(1,10000)