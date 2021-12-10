import pandas as pd

a = [1, 7, 2]

myvar = pd.Series(a,index=["a","b","c"])

print(myvar)

calories = {"day1": 420, "day2": 380, "day3": 390}

myvar1 = pd.Series(calories, index = ["day1", "day2"])

print(myvar1)

data = {
    "Data":[1,2,3],
    "Number":[12,13,14]
}
myd = pd.DataFrame(data)
print(myd)
print(myd.loc[1])

dt=pd.read_csv('diabetes.csv')
print(dt.info())