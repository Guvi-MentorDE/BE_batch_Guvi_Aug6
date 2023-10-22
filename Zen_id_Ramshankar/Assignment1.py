# Find the occurences of elements in list
lst_cnt=0
list1=["dog","horse","hen","dog"]
list2=[]
for cnt,i in enumerate(list1):
    for j in range(cnt,len(list1)):
        if i==list1[j]:
            lst_cnt=lst_cnt+1
    if i not in list2:
        print(i,":",lst_cnt)
    list2.append(i)
    lst_cnt=0

# Anagram
str1="save"
str2="vase"
str1_set=set(str1)
str2_set=set(str2)
if str1_set==str2_set:
    print("The 2 strings are anagrams")
else:
    print("The 2 strings are NOT anagrams")

# Palidrome:
# Approach 1:
lst=["malayalam","middle"]
for i in lst:
    i_reverse=i[::-1]
    if i==i_reverse:
        print(i," is a palindrome")
    else:
        print(i," is NOT a palindrome")

# Approach 2:
lst=["malayalam","middle"]
for i in lst:
    i_reverse=list(i).reverse()
    if list(i)==i_reverse:
        print(i," is a palindrome")
    else:
        print(i," is NOT a palindrome")