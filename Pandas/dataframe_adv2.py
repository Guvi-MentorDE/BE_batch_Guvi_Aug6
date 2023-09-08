import pandas as pd

#Pandas DataFrame.count()
#The Pandas count() is defined as a method that is used to count the number of non-NA cells for each column or row. 
data = {'Players':['sachin', 'Dhoni', 'Rohit', 'Kholi'], 'Matches':[200, 180, 140, 166]}
df = pd.DataFrame(data)
print(df)
c=df.count(axis='columns')
print(c)
r=df.count(axis='rows')
x=df.count() 
print(x)

#Pandas DataFrame.describe()
#The describe() method is used for calculating some statistical data like percentile, mean and std of the numerical values of the Series or DataFrame

import pandas as pd  
import numpy as np  
a1 = pd.Series([1, 2, 3])  
result=a1.describe()
print(result)

#Pandas DataFrame.drop_duplicates()
import pandas as pd  
data = {'Players':['sachin', 'Dhoni', 'Rohit', 'Kholi'], 'Matches':[200, 180, 140, 166]} 
info = pd.DataFrame(data)  
print(info) 

#Pandas DataFrame.append()

info1 = pd.DataFrame({"x":[25,15,12,19], "y":[47, 24, 17, 29]})     
info2 = pd.DataFrame({"x":[25, 15, 12],"y":[47, 24, 17],"z":[38, 12, 45]})    
res=info1.append(info2, ignore_index = True)    

df=info2.dropna(how='all')
print(df)