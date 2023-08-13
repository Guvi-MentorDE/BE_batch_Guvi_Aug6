##Assignment 1 - Mulitple occurences of a word

l1 = ["eat", "sleep", "repeat" , "eat"]
#
for count, i in enumerate(l1):
    #print(count, i)
    if l1.count(i) > 1:
        print(i, "is available at index position", count)

##Assignment 2 - Anagram

str1 = "save"
str2 = "vase"

str1 = list(str1)
str2 = list(str2)
str1.sort()
str2.sort()

str1 = ''.join(str1)
str2 = ''.join(str2)

if str1 == str2:
    print("The string is an anagram")
else:
    print("The string is not an anagram")

##Assignment 3 - Palindrome

inp_string="madam"
inp_string1="maths"

if inp_string == inp_string[::-1]:
    print(inp_string + " is a palindrome")
else:
    print(inp_string + " is not a palindrome")

if inp_string1 == inp_string1[::-1]:
    print(inp_string1 + " is a palindrome")
else:
    print(inp_string1 + " is not a palindrome")