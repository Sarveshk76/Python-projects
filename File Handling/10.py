file = open("lower.txt",'r')
a=file.read()
print("Original String: ",a)
file.close()
file1 = open("upper.txt",'w')
file1.write(a.upper())
file1.close()
with open("upper.txt") as file2:
    data = file2.read()
    print("Converted to uppercase: ",data)
    reverse = data[::-1]
    print("Reversed string: ",reverse)