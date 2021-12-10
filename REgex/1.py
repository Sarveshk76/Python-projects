from datetime import date
import re
adate = "Todays date : 20 08 2021"
today = str(date.today())
pattern = r"\d{2} \d{2} \d{4}"
pattern2 = r"\d{4}-\d{2}-\d{2}"
res = re.findall(pattern,adate)
res1 = re.findall(pattern2,today)
print("Random date: ",res)
print("Date using datetime module: ",res1)