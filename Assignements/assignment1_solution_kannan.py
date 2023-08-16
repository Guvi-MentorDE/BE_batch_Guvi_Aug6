"""
  Assignment 1
  Author  :   Kannan Kandasamy
  Course  :   ML Guvi - Python
  Date    :   06/08/2023
  Details :   Assignments using class
"""

class Strings:
  def __init__(self,s1="",s2=""):
    self.str1 = s1
    self.str2 = s2

  #function definition for palindrome
  def is_palindrome(self, str):
    return(str == str[::-1])

  #function to check two strings are anagram
  def is_anagram(self, str1, str2):
    return(sorted(str1)==sorted(str2))    

#main function
if __name__ == "__main__":
  ip = input("Enter a string to check: ")
  obj = Strings()
  print("yes" if obj.is_palindrome(ip) else "no")
  ip1, ip2 = input("Enter string1 to check anagram: "), input("Enter string2 to check anagaram: ")
  print("yes" if obj.is_anagram(ip1,ip2) else "no")