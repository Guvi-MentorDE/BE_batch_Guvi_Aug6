#                         ASSIGNMENT 1


#        Question 1: How to find if there is multiple occurance of same value in list/string/tuple?
#        Given list is, l1=["eat","sleep","repeat","eat"]

#        Solution:

#        A. To find the multiple occurance of values in a list.

#        Method 1: Using 'for loop'

l2=["eat","sleep","repeat","eat","repeat","sleep","eat","repeat","eat"]
l1=["eat","sleep","repeat","eat","repeat","sleep","eat","repeat","eat"]
len_l1 = len(l1)

duplicate_idx = [0]
n=0
for i in range(len_l1-1):    # in range len_li-1 because there's no need to check for last element
    duplicate_idx[0]=i
    for j in range(i+1,len_l1,1):
        if l1[i]==l1[j]:
            duplicate_idx.append(j)
            l1[j]=n
            n=n+1
            #print(l1)
    if len(duplicate_idx)>1:
        print(f"Element '{l1[i]}' is present in the given list at indices {duplicate_idx}")
        duplicate_idx = [0]


#       Method 2: Using 'while loop'
# 
l1=["eat","sleep","repeat","eat","repeat","sleep","eat","repeat","eat"]
l2=["eat","sleep","repeat","eat","repeat","sleep","eat","repeat","eat"]

len_l1 = len(l1)

duplicate_idx = [0]
itr1 = 0
itr2=0
n=0

while itr1<len_l1-1:
    itr2 = itr1 + 1
    duplicate_idx[0] = itr1
    
    while itr2<len_l1:
        if l1[itr1] == l1[itr2]:
            duplicate_idx.append(itr2)
            l1[itr2] = n
            n = n + 1                  
        
        itr2 = itr2 + 1
    
    
    
    if len(duplicate_idx)>1:
        print(f"Element '{l1[itr1]}' is present in the given list at indices {duplicate_idx}")
        duplicate_idx = [0]  
        
    itr1 = itr1 + 1     


#        Method 3: Using 'enumerate in for loop'

l2=["eat","sleep","repeat","eat","repeat","sleep","eat","repeat","eat"]
l1=["eat","sleep","repeat","eat","repeat","sleep","eat","repeat","eat"]

duplicate_idx = [0]
n=0

for i, vali in enumerate(l1[:-1]):    
    duplicate_idx[0]=i
    for j, valj in enumerate(l1[i+1:], start = i+1):
        if vali==valj:
            duplicate_idx.append(j)
            l1[j]=n
            n=n+1
            #print(l1)
    if len(duplicate_idx)>1:
        print(f"Element '{l1[i]}' is present in the given list at indices {duplicate_idx}")
        duplicate_idx = [0]


#        B. To find the multiple occurance of values in a string.
#        Method 1: Using 'for loop'

str1 = input("Enter a string :")
str2 = str1
for i in range(len(str1)-2):
    duplicate_idx[0] = i
    for j in range(i+1,len(str1),1):
         if str1[i] == str2[j]:
            duplicate_idx.append(j)
            str2 = str2[:j] + '*' + str2[j+1:]
            
    if len(duplicate_idx)>1:
        print(f"Element '{str1[i]}' is present in the given string at indices {duplicate_idx}")
        duplicate_idx = [0]


#        Method 2: Using 'while loop'

str1 = input("Enter a string :")
str2 = str1

duplicate_idx = [0]
itr1 = 0
itr2=0
n=0

while itr1<len(str1)-1:
    itr2 = itr1 + 1
    duplicate_idx[0] = itr1
    
    while itr2<len(str1):
        if str1[itr1] == str2[itr2]:
            duplicate_idx.append(itr2)
            str2 = str2[:itr2] + '*' + str2[itr2+1:]
        
        itr2 = itr2 + 1
    
    
    
    if len(duplicate_idx)>1:
        print(f"Element '{str1[itr1]}' is present in the given string at indices {duplicate_idx}")
        duplicate_idx = [0]  
        
    itr1 = itr1 + 1


#        Method 3: Using 'enumerate in for loop'

str1 = input("Enter a string :")
str2 = str1
for i, vali in enumerate(str1[:-1]):
    duplicate_idx[0] = i
    for j, valj in enumerate(str2[i+1:], start = i+1):
         if vali == valj:
            duplicate_idx.append(j)
            str2 = str2[:j] + '*' + str2[j+1:]
            
    if len(duplicate_idx)>1:
        print(f"Element '{str1[i]}' is present in the given string at indices {duplicate_idx}")
        duplicate_idx = [0]


#        C. To find the multiple occurance of values in a tuple.
#        Method 1: Using 'for loop'
#        input should be space separated eg: e a t s l e e p r e p e a t 

t1 = tuple(input().split())
t2 = t1
duplicate_idx = [0]
tr = ('*',)
for i in range(len(t1)):
    duplicate_idx[0] = i
    for j in range(i+1,len(t1),1):
        if t1[i]==t2[j]:
            duplicate_idx.append(j)
            t_2 = t2[:j] + tr + t2[j+1:]
            t2 = t_2
            
    if len(duplicate_idx)>1:
        print(f"Element '{t1[i]}' is present in the given tuple at indices {duplicate_idx}")
        duplicate_idx = [0]


#        Method 2: Using 'while loop'
#        input should be space separated eg: e a t s l e e p r e p e a t 

t1 = tuple(input().split())
t2 = t1

duplicate_idx = [0]
tr = ('*',)

itr1 = 0
itr2=0

while itr1<len(t1)-1:
    itr2 = itr1 + 1
    duplicate_idx[0] = itr1
    
    while itr2<len(t1):
        if t1[itr1] == t2[itr2]:
            duplicate_idx.append(itr2)
            t_2 = t2[:itr2] + tr + t2[itr2+1:]
            t2 = t_2
        
        itr2 = itr2 + 1
          
    if len(duplicate_idx)>1:
        print(f"Element '{t1[itr1]}' is present in the given tuple at indices {duplicate_idx}")
        duplicate_idx = [0]
        
    itr1 = itr1 + 1


#        Method 3: Using 'enumerate in for loop'
#        input should be space separated eg: e a t s l e e p r e p e a t 

t1 = tuple(input().split())
t2 = t1
duplicate_idx = [0]
tr = ('*',)
for i, vali in enumerate(t1[:-1]):
    duplicate_idx[0] = i
    for j, valj in enumerate(t2[i+1:], start = i+1):
        if vali==valj:
            duplicate_idx.append(j)
            t_2 = t2[:j] + tr + t2[j+1:]
            t2 = t_2
            
    if len(duplicate_idx)>1:
        print(f"Element '{t1[i]}' is present in the given tuple at indices {duplicate_idx}")
        duplicate_idx = [0]



#           Question 2: Find if below two strings are anagrams or not?

#           str1 = "save"

#           str2 = "vase"

#           Solution:


str1 = input("Enter first string: ")
str2 = input("Enter Second string: ")
n=0
for i in str1:
    for j in str2:
        if i==j:
            n+=1
if n==len(str1):
    print(f"Strings '{str1}' and '{str2}' are anagrams of eachother")
else:
    print(f"Strings '{str1}' and '{str2}' are not anagrams of eachother")


#           Question 3: Find if any string is palindrome or not ?

#           Solution: 

str1 = input("Enter your string : ")

str2 = str1[::-1]
if str1==str2:
    print(f"Entered string '{str1}' is a palindrome")
else:
    print(f"Entered string '{str1}' is not a palindrome")