import pandas as pd  
import numpy as np  
a = pd.Series(['Java', 'C', 'C++', np.nan])  
b=a.map({'Java': 'Core'})  

print(b)



s = pd.Series(["a", "b", "c"],name="vals")
print(s)   
f=s.to_frame()
print(f)