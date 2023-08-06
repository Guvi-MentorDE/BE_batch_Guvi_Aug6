#Python Dictionary is used to store the data in a key-value pair format.
#mutable 
#Value can be any type such as list, tuple, integer, etc.
#[] {},       ()

#mutable     immutable 



Dict = {}     
print("Empty Dictionary: ")     
print(Dict)  

Dict = {"key1": "value2", "key2": "value2"}      
print(type(Dict))  

Dict2 = {"India": 1, "America": 2, "UK": 3, "Japan":3 }   

Dict2 = {1:"India", 2:"America" }   

#Dict_student1 ={roll_no:2 ,match:100, science:80 , lang:90}
#Dict_student2 ={roll_no:2, match:90, science:80 , lang:90}


Dict2 = {"India": "INR", "America": "USD", "UK":"GBP", "Japan":"Yen"}      
print(Dict2)  

print(Dict2["America"])

print(Dict2.get('Japan'))


#Add/Update dictionary
print('-----------Add/Update dictionary-----------')
my_dict = {'course':'python','fee':100,'duration':'60 days'}


#my_dict = {'course':'python','fee':100,'duration':'60 days','tutor':'guvi'}

my_dict['tutor']='guvi'
print(my_dict)

my_dict.update({'name':'DSA'}) #if key no there - > append to dict at end ; if key is there update the value alone 
print(my_dict)

my_dict['duration']='45 days'
print(my_dict)

#length
print(len(my_dict))


#delete 
print(my_dict.pop('duration'))


#iterate:

my_dict={"Course":"python","Fee":4000,"Duration":"60 days"}
for x in my_dict:
    print(x)

#iterate key and value:
my_dict ={"Course":"python","Fee":4000,"Duration":"60 days"}
for key, value in my_dict.items():
    print(key, value)
    

#misc:
dict = {7: "Ayan", 5: "Bunny", 8: "Ram", 1: "Bheem"}  
sorted(dict)  

dict = {1: "Microsoft", 2: "Google", 3: "Facebook", 4: "Amazon", 5: "Flipkart"}  
# clear() method  
dict.clear()  
print(dict) 


dict = {1: "Microsoft", 2: "Google", 3: "Facebook", 4: "Amazon", 5: "Flipkart"}  
# keys() method  
print(dict.keys())  

#convert dict to tuples

dict = {1: "Microsoft", 2: "Google", 3: "Facebook", 4: "Amazon", 5: "Flipkart"}  
# items() method  
print(dict.items())  