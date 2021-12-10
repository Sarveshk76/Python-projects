import re
pattern = r"\b\w\w"
string = "Good Morning Students@gmail.com"
patt1 = r"[\w.-]+@[\w.-]+"
res = re.findall(patt1, string)

