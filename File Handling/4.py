import os
file = open(input("Enter the file name to write: "),"w")
file.write("GoodmornigStudents")
file.close()
file = open(input("Enter the file name to read: "),"r")
text = file.read()
print(len(text))
file.close()