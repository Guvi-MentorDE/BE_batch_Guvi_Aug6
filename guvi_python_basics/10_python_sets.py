#A Python set is the collection of the unordered items. 
#Each element in the set must be unique, immutable, and the sets remove the duplicate elements. 
#Sets are mutable which means we can modify it after its creation.

#Unlike other collections in Python, there is no index attached to the elements of the set, 
#i.e., we cannot directly access any element of the set by the index. 
#However, we can print them all together, or we can get the list of elements by looping through the set.

Days = {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}    
print(Days)    
print(type(Days))    
print("looping through the set elements ... ")    
for i in Days:    
    print(i)    


Days = set(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])    
print(Days)    
print(type(Days))    
print("looping through the set elements ... ")    
for i in Days:    
    print(i)    


#Removing items from the set:
#------------------------------

#Python provides the discard() method and remove() method which can be used to remove the items from the set
#discard() function if the item does not exist in the set then the set remain unchanged ; will not capture error
#remove() method will through an error. ; will infom you on error  ; (recommended)

months = set(["January","February", "March", "April", "May", "June"])    
print("\nprinting the original set ... ")    
print(months)    
print("\nRemoving some months from the set...");    
months.discard("January");    
months.discard("May");    
print("\nPrinting the modified set...");    
print(months)    
print("\nlooping through the set elements ... ")    
for i in months:    
    print(i)    


months = set(["January","February", "March", "April", "May", "June"])    
print("\nprinting the original set ... ")    
print(months)    
print("\nRemoving some months from the set...");    
months.remove("January");    
months.remove("May");    
print("\nPrinting the modified set...");    
print(months)    

#Set Operations:
#----------------

#) Union 

Days1 = {"Monday","Tuesday","Wednesday","Thursday", "Sunday"}    
Days2 = {"Friday","Saturday","Sunday"}    
print(Days1|Days2) #printing the union of the sets  


Days1 = {"Monday","Tuesday","Wednesday","Thursday"}    
Days2 = {"Friday","Saturday","Sunday"}    
print(Days1.union(Days2))


#) Intersection

Days1 = {"Monday","Tuesday", "Wednesday", "Thursday"}    
Days2 = {"Monday","Tuesday","Sunday", "Friday"}    
print(Days1&Days2) #prints the intersection of the two sets    

set1 = {"Devansh","John", "David", "Martin"}    
set2 = {"Steve", "Milan", "David", "Martin"}    
print(set1.intersection(set2))

#)intersection_update

a = {"Devansh", "bob", "castle"}    
b = {"castle", "dude", "emyway"}    
c = {"fuson", "gaurav", "castle"}    
    
a.intersection_update(b, c)    
    
print(a)    

#subtraction

Days1 = {"Monday",  "Tuesday", "Wednesday", "Thursday"}    
Days2 = {"Monday", "Tuesday", "Sunday"}    
print(Days1-Days2) 

#op: {'Thursday', 'Wednesday'}

#Symmetric Difference of two sets ; ignores all commen elements 

a = {1,2,3,4,5,6}  
b = {1,2,9,8,10}  
c = a^b  
print(c)  

#op: {3, 4, 5, 6, 8, 9, 10}


reference: 
https://www.javatpoint.com/python-set