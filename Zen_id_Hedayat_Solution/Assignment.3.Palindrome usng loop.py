"""
  Assignment 3
  Author  :   Saleh Md Hedayatullah
  Course  :   ML Guvi - Python
  Details :   Check Palindrome using loop
"""
inp_string="madam"
inp_string2="maths"
if inp_string ==inp_string[::-1]:
    print ('the word madam is a palindrome')
else:
    print ('the word madam is not a palindrome')
    
if inp_string2 == inp_string2[::-1]:
    print ('the word maths is a palindrome')
else:
    print ('the word maths is not a palindrome')