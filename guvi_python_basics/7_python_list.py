#List:
#=====
#--hold's ordered collection of item
#--mix of data structures within a list 
#--list within a list can be done : nested list
#--mutable : changable , updatable 

#accesing of list elements is same as array 
#list=[int,int,int,string,float]

list1=[2,4,6,8]

list2=[1,3,5,7,9]

list3=['python','java','c','sql']

listx=[0,'abc',2,2.5,3,5,6]

#accessing a list=> list1[2]

#accessing a list from reverse => list1[-1] 
#(reverse access of list starts from -1 , -2 , -3 untill -(lenth)) 
len(mylist)

#insert/update in list:
 
#beginning, end, middle , insert into another list 
mylist=[9,8,7,6,4,5]
[9,8,7,6,4,5]
0  1 2 3 4 5 
len(mylist)

print(mylist)
mylist[0]=10000
print(mylist)

#list.insert(index,value)
mylist.insert(0,11)#--> all elements will move one step right   
print(mylist)


mylist.insert(7,'i am index 7') 

mylist.append(50)  #--> adds element to end of the list. 
print(mylist)

mylist.extend(list1) #--> all elements from list1 will be appended to mylist
print(mylist)

#delete a element from list 
mylist.pop(0)
print(mylist)


max(mylist)

min(mylist)

len(mylist)

#asc
mylist=[9,8,7,6,4,5]
mylist.sort()

#dec
mylist.sort(reverse=True)

#reverse
mylist.reverse()

#traversing through list element:
#-------------------------------
for i in list1:
    print(i)

for i in range(len(list1)):
    list1[i] = list1[i] + 1
    print(list1)

emptylist = []
for i in emptylist:
    print("empty list")

#convert string to list:
#-----------------------
a='spam'
b=list(a)
print(b)


#split: (convert string to list)
#-----
a='spam-spam-spam'
b=a.split('-')
print(b)
#>>> print(b)
['spam', 'spam', 'spam']

#join: (convert list to string)
#------
b1="hello all"
delimiter=" "
result=delimiter.join(b1)
print(result)


 


