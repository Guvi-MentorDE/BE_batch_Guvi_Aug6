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