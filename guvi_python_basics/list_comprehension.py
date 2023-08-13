#regular python looping logic 

#list1 = ["java", "python", "sql", "c"]
#list2 = []

#for x in list1:
  #if "a" in x:
    #list2.append(x)

#print(list2)

#list comprehension

list1 = ["java", "python", "sql", "c"]

list2 = [x for x in list1 if "p" in x ]

list3 = [x for x in list1 if x in list1]

print(list2)