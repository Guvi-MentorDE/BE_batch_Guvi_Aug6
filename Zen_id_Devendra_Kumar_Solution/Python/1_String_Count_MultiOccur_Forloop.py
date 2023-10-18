"""
                                                 Assignment 
                                             ------------------                                    
  Author  :   Devendra Kumar Rajendran
  Course  :   ML - Python
  Date    :   12/08/2023
-----------------------------------------------------------------------------------------------------------
  Question :  
  1. Count the multiple occurence of the element in the list using looping 

---------------------------------------------------------------------------------------------------------------
"""
# Solutions  :

class Multi_occurence:
 
 
 def count(self, list):
  for i in set(list):
   print(f"{i} is repeated for {list.count(i)} times")


if __name__ == "__main__":
 
 list = ["eat", "sleep", "repeat","eat", "sleep", "repeat", "eat", "sleep", "repeat","eat"]
 obj = Multi_occurence()
 obj.count(list)

