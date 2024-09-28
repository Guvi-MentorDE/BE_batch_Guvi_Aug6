'''
Author: Ankitha Desai
Date Created:: 19-08-2023
Description: This file contains the code for anagram
'''

# Anagram

class Anagram:

    def check_Anagram(str1,str2):
        if(sorted(str1)==sorted(str2)):
            print("The strings are anagrams")
        else:
            print("The strings are not anagrams")
        
    if __name__ == "__main__":
        str1 = input()
        str2 = input()
        result = check_Anagram(str1,str2)