import pandas as pd  
data = pd.DataFrame({'Players':['sachin', 'Dhoni', 'Rohit', 'Kholi'], 'Matches':[200, 180, 140, 166]} )  
stats = pd.DataFrame({'Players':['sachin', 'Kholi'], 'runs':[22000, 20000]})  
print("different ways to join")
#df_join=data.join(stats.set_index(["Players"]),on=["Players"],how="outer",lsuffix="_left", rsuffix="_right",sort=True) 
#df_join=data.join(stats,lsuffix="_left", rsuffix="_right",sort=True)   
  
print(df_join)
df_join.loc[0]

df_join2=data.set_index('Players').join(stats.set_index('Players'))  
#print(df_join2)

df_join3=data.join(stats.set_index('Players'), on='Players') 
#print(df_join3) 
