#QUESTION:
#1. create a function for detmining palidrome , anagram and retun the result to the function call then print.

#SOLUTION:
#Check if two strings are palindrome or not

def isPalindrome(string1):

    return string1 == string1[::-1]


#-------------------------------------------------------------

#Check if two strings are anagram or not

def check(string2, string3):

	return sorted(string2) == sorted(string3)		
		

if __name__ == "__main__":
    choice = int(input())
    match choice:
         case 1: #To check palindrome or not
              print("Check if given string are palindrome or not")
              string1 = input()
              result = isPalindrome(string1)
              if result:
                   print("The given string are palindrome.")
              else:
                   print("The given string are not palindrome.")

         case 2: #To check anagram or not
              print("Check if two given strings are anagram or not")
              string2 ="save"
              string3 ="vase"
              result1 = check(string2, string3)
              if result1:
                   print("The given strings are anagrams.")
              else:
                   print("The given strings are not anagrams.")