a = 8
for i in range(0, 5):
    for j in range(0, a):
        print(end=" ")
    a = a - 2
    for j in range(1, i+1):
        print(j, end=" ")
    print()