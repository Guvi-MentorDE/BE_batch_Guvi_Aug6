
import pandas as pd
technologies   = ({
    'Courses':["DE","DE","Hadoop","DS","Pandas","Hadoop","DE","DS","JAVA"],
    'Fee' :[22000,25000,23000,24000,26000,25000,25000,22000,1500],
    'Duration':['30days','50days','55days','40days','60days','35days','30days','50days','40days'],
    'Discount':[1000,2300,1000,1200,2500,None,1400,1600,0]
          })
df = pd.DataFrame(technologies)
print(df)

df2 =df.groupby(['Courses']).sum()
print(df2)

df3 =df.groupby(['Courses', 'Duration']).sum()
print(df3)

groupedDF = df.groupby('Courses',sort=False).sum()
sortedDF=groupedDF.sort_values('Courses', ascending=False)
print(groupedDF)
print(sortedDF)