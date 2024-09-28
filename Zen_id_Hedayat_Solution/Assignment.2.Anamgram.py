"""
  Assignment 2
  Author  :   Saleh Md Hedayatullah
  Course  :   ML Guvi - Python
  Details :   To check if a given string is Anamgram 
"""
str1 = "save"
str2 = "vase"

str1 = sorted(str1.lower())
str2 = sorted(str2.lower())

if str1 == str2:
    print("yes, the given two string are annagram")
else:
    print("No , the given two strings are not annagram")