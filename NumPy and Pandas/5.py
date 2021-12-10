import pandas as pd
import numpy as np
data = np.array(['a','b','c','d'])
s = pd.Series(data)
print(s)
print("Data at 1th position: ",s[1])


data1 = {'a' : 0, 'b' : 1, 'c' : 2}
s1 = pd.Series(data1)
print(s1)
print("Data at 1th position: ",s1[1])

data = {
    "Roll No.":[1,2,3,4,5],
    "Names":['Rohan','Rahul','Suraj','Ashok','Nitin'],
    "Div":['A','B','A','B','A'],
    "Class":['FY','SY','TY','FY','SY']
}
df = pd.DataFrame(data)
print(df)
col = df.loc["Roll No.":"Div"]
print(col)
df1 = df.assign(City=['Nashik','Pune','Mumbai','Nashik','Pune'])
print("After adding column: ")
print(df1)
del df1['Class']
print('After deleting column: ')
print(df1)
print("After adding row: ")
row = df1.append({
    "Roll No.":6,
    "Names":'Sarvesh',
    "Div":'B',
    "City":'Nagpur'
},ignore_index=True)
print(row)
row1 = row[row.Div != 'B']
print("After deleting row: ")
print(row1)