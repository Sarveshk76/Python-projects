import os
os.mkdir("D:/Files/Folder")
os.rename("D:/Files/Folder","D:/Files/NewFolder")
relpath = os.path.relpath("file.txt")
print("relpath : ",relpath)
abspath = os.path.abspath("File Handling/1.py")
print("abspath : ",abspath)
os.remove("D:/Files/random.txt")