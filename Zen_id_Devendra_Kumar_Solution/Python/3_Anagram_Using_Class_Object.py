"""
                                                 Assignment 
                                             ------------------                                    
  Author  :   Devendra Kumar Rajendran
  Course  :   ML - Python
  Date    :   19/08/2023
-----------------------------------------------------------------------------------------------------------
  Question :  
   1. Anagram using class and objects 
---------------------------------------------------------------------------------------------------------------
"""

class Anagram():
  
  def __init__(self, str1, str2):
    self.str1 = str1
    self.str2 = str2

  def anagram_check(self):
     if (sorted(self.str1)==sorted(self.str2)):
      print (f" Strings are anagram  ")
     else:
      print(f"Strings are not anagram ") 


if __name__ == "__main__":
  
  str1 = input("Enter the string 1 : ")
  str2 = input("Enter the string 2 : ")
  obj_a = Anagram(str1,str2)
  obj_a.anagram_check() 







