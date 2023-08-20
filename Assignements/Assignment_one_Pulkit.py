# 1. create a function for detmining palidrome , anagram and retun the result to the function call then print. 

'''Assignment 1
  Author  :   Pulkit Khetarpal
  Course  :   Data Engineering_Guvi
  Date    :   13-aug-2023
  Details :   Assignment 1
  '''

class Checker:
    def __init__(self,s1='',s2=''):
        self.str1=s1
        self.str2=s2
    def check_palindrome(self,string1):
        string2=string1[::-1]
        if string1==string2:
          return ('palindrome')
        else:
          return ('not a palindrome')
        
    def check_anagram(self,str1,str2):
       if(sorted(str1)==sorted(str2)):
          return ('anagram')
       else:
          return('not anagram')
       

if __name__ == "__main__":
    obj1=Checker()
    string_name=input('Enter the string to check for palindrome : ')
    result=obj1.check_palindrome(string_name)
    print('String entered is '+result)
    string1_name,string2_name=input('Enter first string to check for anagram :'),input('Enter second string to check for anagram :')
    result1=obj1.check_anagram(string1_name,string2_name)
    print('String entered is '+result1)

