file = open("file.txt","w+")
file.write(str('Hello'))
Lines = [" GoodMorning ","Students "]
file.writelines(Lines)
if file:
    print("File successfully written.")
file.close()

file1 = open("file.txt")
read = file1.read(10)
print("Reading the file: ",read)
file1.close()

with open("file.txt",'r') as f:
    line = f.read()
    line1 = line.rstrip()
    print("With keyword: ",line.split())
    print(line1)
    print("Find ""Stud"": ",line.find("Stud"))