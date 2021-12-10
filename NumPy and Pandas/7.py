import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('data.csv')
print(df)
df['Date'] = pd.to_datetime(df['Date'])
print('Convert wrong date into correct form: ')
print(df.to_string())

print('Removing duplicate row: ')
print(df.duplicated())

print('Representing pulse and Max pulse variable relation ')
print(df.corr())
boxplot = df.corr().plot(column=['Pulse','Maxpulse','Calories'])
plt.show()