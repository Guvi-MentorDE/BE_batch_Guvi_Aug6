'''
#Q3)  
reverse a string without using any inbuilt functions 
hind: looping. 
'''


mystring = "elephant"
reversed = ""
for i in mystring:
    reversed = i + reversed
print(reversed)