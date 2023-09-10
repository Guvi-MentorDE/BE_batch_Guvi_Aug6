import numpy as np
import pandas as pd

labels = ['x', 'y', 'z']

my_list = [10, 20, 30]

arr = np.array([10, 20, 30])

d = {'a':10, 'b':20, 'c':30}


print("creating pandas series")

s1=pd.Series(my_list)
print(s1)

print("creating pandas series with specific index")
s2=pd.Series(my_list, index=labels)
print(s2)

print("accessing the index position")
print(s2[0])

