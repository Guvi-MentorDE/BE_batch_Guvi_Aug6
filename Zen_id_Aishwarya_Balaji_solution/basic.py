'''1) How to find if there is multiple occurence of same value in list/tuple/string.
l1 = ["eat", "sleep", "repeat", "eat"]

l1.index("eat")

solve: using enumerate concept
solve: using looping concept(for/while)'''

#Using enumerate method

l1 = ["eat", "sleep", "repeat", "eat"]
sample = [i for i, j in enumerate(l1) if(l1.count(j) > 1)]
print(sample)

#Using for loop
s = [item for item in range(0, len(l1)) if(l1.count(l1[item])>1)]
print(s)



'''2) Find if below two strings anagrams or not
str1 = "save"
str2 = "vase"'''

s1 = input("Enter a string1: ")
s2 = input("Enter a string2: ")
check = [s2[i] in s1 for i in range(len(s2))]
print("Anagram") if(len(set(check)) == 1) else print("Not an anagram")

'''3) find if any given string is palindrome or not "madam" & "maths"'''
s1 = input("Enter a string: ")
print("Palindrome") if(s1 == s1[::-1]) else print("Not a palindrome")