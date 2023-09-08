import pandas as pd
import numpy as np
technologies = {
    'Courses':["Spark","PySpark","Hadoop","Python","pandas",np.nan],
    'Fee' :[20000,25000,26000,23093,24000,np.nan],
    'Duration':['30day','40days','35days','45days',np.nan,np.nan],
    'Discount':[1000,np.nan,1200,2500,pd.NaT,np.nan],
    '':[np.nan,np.nan,np.nan,np.nan,np.nan,np.nan]
              }
index_labels=['r1','r2','r3','r4','r5','']
df = pd.DataFrame(technologies,index=index_labels)
print(df)

# Drop rows that has all Nan Values
df=df.dropna(how='all')
print(df)

# Drop columns that has all Nan Values
df=df.dropna(how='all',axis=1)
print(df)

# Default drop rows that contains nan values
df2=df.dropna()
print(df2)

# Drop all columns with NaN values
df2=df.dropna(axis=1)
print(df2)

# Drop rows that has NaN values on selected columns
df2=df.dropna(subset=['Courses','Duration'])
print(df2)
# With threshold, 
# Keep only the rows with at least 2 non-NA values.
df2=df.dropna(thresh=3,axis=1)
print(df2)