#QUESTION
#1. accept a string from user.
#2. check if the list is palindrome or not.
#3. create a class and object 
#    3.a) create a constructor. 
#4. access the logic of palindrome using object.method() 

#SOLUTION-1:
#Check if two strings are palindrome or not by using class and oject method call

#class palindrome:
#    def isPalindrome(string1):
#        return string1 == string1[::-1]

#if __name__ == "__main__":
#    string1 = input()
#    object = palindrome
#    result = object.isPalindrome(string1)
#    if result:
#        print("The given string is palindrome.")
#    else:
#        print("The given string is not palindrome.")

#---------------------------------------------------------------

#SOLUTION-2:
#Check if two strings are palindrome or not by using constructor __init__ function
class palindrome:
    def __init__ (self, string1):
        self.string1 = string1
        self.result = self.string1 == self.string1[::-1]
    def result(self):
        if self.result:
            print("The given string is palindrome.")
        else:
            print("The given string is not palindrome.")

if __name__ == "__main__":
    string1 = input()
    object = palindrome(string1)
    object.result()