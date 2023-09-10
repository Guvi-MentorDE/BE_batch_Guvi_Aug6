import pandas as pd  
data = pd.DataFrame({'Players':['sachin', 'Dhoni', 'Rohit', 'Kholi'], 'Matches':[200, 180, 140, 166]} )  
stats = pd.DataFrame({'Players':['sachin', 'Kholi'], 'runs':[22000, 20000]})  
print("different ways to join")
df_join=data.join(stats.set_index(["Players"]),on=["Players"],how="outer",lsuffix="_left", rsuffix="_right",sort=True) 
df_join=data.join(stats,lsuffix="_left", rsuffix="_right",sort=True)   
  
print(df_join)
df_join.loc[0]


print("different types of jons available in pandas:")

#pandas join using columns name

df_join2=data.set_index('Players').join(stats.set_index('Players') , how='inner')  
print(df_join2)


df_join3=data.join(stats.set_index('Players'), on='Players') 
#print(df_join3) 

#df joins:
df2=data.join(stats, lsuffix="_left", rsuffix="_right") #select a.* , b.* from a join b ;
print(df2)

df3=data.join(stats, lsuffix="_left", rsuffix="_right", how='inner')
print(df3)

df4=data.join(stats, lsuffix="_left", rsuffix="_right", how='right')
print(df4)

df5=data.join(stats, lsuffix="_left", rsuffix="_right", how='left')
print(df5)

df6=data.join(stats, lsuffix="_left", rsuffix="_right", how='outer')
print(df6)