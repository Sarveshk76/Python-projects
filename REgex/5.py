import re
string = "This is a string"
pat1 = r"\w+"
pat2  =r"\w{1}"
res = re.findall(pat1,string)
res1 = re.findall(pat2,string)
print("Words: ",res)
print("Characters: ",res1)