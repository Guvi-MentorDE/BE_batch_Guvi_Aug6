'''
Author: Ankitha Desai
Date Created:: 19-08-2023
Description: This file contains the code for palidrome
'''

'''1. Create a function for detmining palidrome and retun the result to the function call then print.'''

# Palindrome
class Palindrome:
    def __init__(self,str):
        self.str=str
    
    def check_palindrome(self):
        str1=self.str[::-1]
        if(self.str==str1):
            print(self.str," is a palindrome")
        else:
            print(self.str," is not a palindrome")

if __name__=="__main__":
    print("Enter a string: ")
    input_string=input()
    p1=Palindrome(input_string)
    p1.check_palindrome()