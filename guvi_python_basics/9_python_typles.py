#python typles
#A Python Tuple is a group of items that are separated by comma

#list vs tuple 
#1. []                       ()
#2. mutable                 immutable 
#ex. mylist[0]=10000        tuple1[0]=10000

#-------------------------------------------------------
#3. collection of           collection of same or different data type  
#    same or diff
#    data type 


empty_tuple = ()    
print("Empty tuple: ", empty_tuple)    


int_tuple = (4, 6, 8, 10, 12, 14)    
print("Tuple with integers: ", int_tuple) 

mixed_tuple = (4, "Python", 9.3)  
print("Tuple with different data types: ", mixed_tuple)    

nested_tuple = ("Python", (5, 3, 5, 6))    
print("A nested tuple: ", nested_tuple) 

#index 

tuple1 = ("Python", "Tuple", "Ordered", "Immutable", "Collection", "Objects")  
print(tuple1[1])


#slicing
print(tuple1[1:])



#misc

tuple1 = tuple1 * 3
print("repeating a tuple:",tuple1)  

T1 = (0, 1, 5, 6, 7, 2, 2, 4, 2, 3, 2, 3, 1, 3, 2 )  
res = T1.count(2)  

res=T1.index(5)

