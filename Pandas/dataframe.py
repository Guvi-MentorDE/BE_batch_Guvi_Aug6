import pandas as pd
import numpy as np


print("create an empty dataframe")
df = pd.DataFrame()
print(df)

print("#1 example")
lst = ['Java', 'python', 'scala', 'bash', 'sql']
df = pd.Series(lst)
print(df)

print("#2 example")
data = {'Players':['sachin', 'Dhoni', 'Rohit', 'Kholi'], 'Matches':[200, 180, 140, 166]}
df = pd.DataFrame(data)
print(df)
df.head(n=2) #select * from limit 2;
df.tail(n=2) #select * from order by desc limit 2

print("#4 matrix")

rows = ['X','Y','Z']
cols = ['A', 'B', 'C', 'D', 'E']
data = np.round(np.random.randn(3,5),2)
df1=pd.DataFrame(data, rows, cols)
print(df1)

print(df1['A'])

print(df1['A']['X'])

print("#5 creating and removing cols")

df1['A + B'] = df1['A'] + df1['B']
print(df1)


print("#6 drop the newly added columns")

df2 = df1.drop('A + B', axis = 1)
print(df2)

#df.drop('A + B', axis=1, inplace=True) alternative way

print("#6 dropping rows")

df3 =df1.drop('Y')
print(df3)


print("#7 determine no of rows and columns in a dataframe")
print(df1.shape)

print("#8 select operation")

print(df.loc['Dhoni'])


print("different types of select operations:")

