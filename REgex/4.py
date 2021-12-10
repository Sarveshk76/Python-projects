import re
string = input("Enter Mobile No.: ")
pat = r"^[7-9]\d{9}"
res = re.findall(pat, string)
if res:
    print("Number validated.")
else:
    print("Invalid number")