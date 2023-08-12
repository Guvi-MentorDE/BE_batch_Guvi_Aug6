# array is very similar to LIST.
# python does not natively support array.
# we can directly 
# []  => array/list
#list2=[1,3,5,7,9] 

#list3=['python','java','c','sql']
#import pandas

import array as arr
import numpy as np 

arr1 = arr.array('i',[1,2,3,4,5,6])


print(arr1)

print(type(arr1))

arr1.insert(6,7)

print(arr1)

arr1.insert(2,9)

print(arr1)


#traversing an array 

def traverseArray(array):
    for i in array:
        print(i)

traverseArray(arr1)



toArray=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(toArray)
