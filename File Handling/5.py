file = open("file1.txt",'w')
file.write("Line 1"
           "\nLine 2"
           "\nLine 3"
           "\nLine 4"
           "\nLine 5"
           "\nLine 6"
           "\nLine 7"
           "\nLine 8"
           "\nLine 9"
           "\nLine 10")
file.close()
file1 = open("file1.txt",'r')
n = int(input("Enter the number of first n-lines: "))
for i in range(n):
    print(file1.readline(),end='')
m = int(input("Enter the number of last m-lines: "))
for i in (file1.readlines() [-m:]):
    print(i,end='')
file1.close()