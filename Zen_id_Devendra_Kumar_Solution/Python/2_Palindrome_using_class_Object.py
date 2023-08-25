"""
                                                 Assignment 
                                             ------------------                                    
  Author  :   Devendra Kumar Rajendran
  Course  :   ML - Python
  Date    :   12/08/2023
-----------------------------------------------------------------------------------------------------------
  Question :  
    1. accept a string from user.
    2. check if the list is palindrome or not.
    3. create a class and object 
     3.a) create a constructor. 
    4. access the logic of palindrome using object.method()
-----------------------------------------------------------------------------------------------------------
"""
# Solutions  :

#import <modules>  

class Palindrome:                         # Define Class
 def __init__(self,str,rev_str):          # Constructor
  self.str = str
  self.rev_str = rev_str
  
 def validate(self):                     # Define Class method 
    for i in self.str:
      self.rev_str = i + self.rev_str
    if self.rev_str == self.str:
     print(f" {self.str} is palidrome ")
    else: 
     print(f" {self.str} is not palindrome") 
    
  
if __name__ == "__main__":               # Main Method 
 
 str = input("Enter the string to check Palindorome: ")
 obj_check = Palindrome(str, "")
 obj_check.validate()                    # method call



