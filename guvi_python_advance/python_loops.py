
#There are two types of loop
#1.For loop   
#2.While loop 
1,2,3,..........10
# starting index , last index >> len(list)
# one index by another incremnetally 

#template
for [ELEMENT] in [ITERATIVE-LIST]:
	[statement to execute]
else:
	[statement to execute when loop is over]
	[else statement is completely optional]


[0,1,2,3,4,5,6,7,8,9,10]

s="Hello"
for i in s:
    print(i) 

for x in range(5):     
    print(x)

list=[20,30,10,40]
for x in list:
    print(x)
else:
    print("Task finished")
    
#for i in range 0 to 4
for i in range(0, len(list)+1):    #list =  start at index 0 , end at index 5
	print (list[i])
 
for i in range(7):   
	print (list[i])
 

list=[10,20,30,40,50,60,70]
for x in list:
    print(x)
    if x == 40:
        break
 
 
# list=[10,20,200,30,40,300,60]
# for x in list:
#     if x > 100:
#         continue
#     print(x)


#Nested for loop
list1=[10,20]
list2=[5,10,20]
for x in list1:
    for y in list2:
        print(x,y)



superlist = [[1, 3, 6], [8, 2,], [0, 4, 7, 10], [1, 5, 2], [6]]

for i in superlist:
	for j in i:
		print ("sub list within superlist : ", j)

for i in superlist:
    print("printing list from sperlist:",i)

#while loop template
while [condition] :
	[statement to execute]
else:
	[statement to execute if condition is false]
	[else statement is completely optional]

#while True:
#	print ("I am printing because the condition is True")
    
list=[0,1,2,3,4,5,5,6]
print('---while loop---')
iter = 7  #starting
while iter <= 7: #ending at 6  1,2,3,4,5 , 6 break the loop 
  print(iter) 
  iter = iter + 2        #iterate mnaully 
  #iter +=1 
  
print('---while loop example 2---')
i = 1
while i < 3:
  print(i)
  i += 1
else:
  print("i is no longer less than 3")