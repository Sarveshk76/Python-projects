file1 = open("file1.py",'w')
file1.write("a = int(input('Enter num1: '))"
"\nb = int(input('Enter num2: '))"
"\n#taking two integers as an input"
"\nadd = a+b"
"\n#Addition operation"
"\n#Printing the output"
"\nprint('Addition: ',add)")
file1.close()
file = open("file1.py",'r')
line = file.readlines()
line1 = []
n=len(line)
for i in range(n):
    if line[i][0]!='#':
        m = line[i]
        line1.append(m)
print('Output with comments removed: ')
print("".join(line1))
file.close()
file2 = open("file2.py",'w')
file2.write("".join(line1))
file2.close()