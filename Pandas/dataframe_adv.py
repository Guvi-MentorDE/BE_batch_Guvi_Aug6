import pandas as pd
import numpy as np
# Create first Dataframe using dictionary   
info1 = pd.DataFrame({"x":[25,15,12,19],"y":[47, 24, 17, 29]})     
# Create second Dataframe using dictionary   
Info2 = pd.DataFrame({"x":[25, 15, 12],"y":[47, 24, 17],"z":[38, 12, 45]})   
# append info2 at end in info1   
final_df=info1.append(Info2, ignore_index = True) 

print(final_df)



info = pd.DataFrame([[2, 3]] * 4, columns=['P', 'Q'])  
info.apply(np.sqrt)  
print(info)

t1=info.apply(np.sum, axis=0)  
print(t1)

t2=info.apply(np.sum, axis=1)  
print(t2)