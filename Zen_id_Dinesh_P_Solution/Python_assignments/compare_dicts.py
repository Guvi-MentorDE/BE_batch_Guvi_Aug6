'''
#Q4) 
dict1 ={"INDIA":"INR","US":"USD"}
dict2 ={"INDIA":"INR","UK":"GBP","JAPAN":"YEN"}


write a logic to compare dict1 and dict2 , create a new dict3 with only commen keys.

RESULT:
dict3={"INDIA":"INR"}
'''

dict1 ={"INDIA":"INR","US":"USD"}
dict2 ={"INDIA":"INR","UK":"GBP","JAPAN":"YEN"}
dict3 ={}
for key in dict1:
    if key in dict2:
        dict3[key]=dict1[key]

print("dict3:",dict3)
