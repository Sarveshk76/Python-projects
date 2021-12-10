import pandas as pd
print('Printing first 5 and last 5 rows: ')
df = pd.read_csv('Automobile_data.csv')
print(df)

new_df = df.dropna(inplace = True)
print('After deleting empty rows: ')
print(df)

df.fillna(130, inplace = True)
print('After replacing empty cells: ')
print(df)

x = df["price"].mean()
df["price"].fillna(x, inplace = True)
print('Replacing using mean, mode or median: ')
print(df)

print(df.corr())
