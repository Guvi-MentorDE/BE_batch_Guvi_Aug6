#QUESTION
#2(A).find if below two strings annagrams or not 
#str1 = "save"
#str2 = "vase"

#SOLUTION
#Check if two strings are anagram or not				
string1 ="save"
string2 ="vase"

if sorted(string1) == sorted(string2):
     print("The given strings are anagrams.")
else:
     print("The given strings are not anagrams.")

#------------------------------------------------------------
#QUESTION
#2(B).find if any given string is palidrome or not 
#inp_string="madam"
#inp_string="maths"

#SOLUTION
#Check if two strings are palindrome or not
string1 = input()

if string1 == string1[::-1]:
    print("The given strings are palindrome.")
else:
    print("The given strings are not palindrome.")