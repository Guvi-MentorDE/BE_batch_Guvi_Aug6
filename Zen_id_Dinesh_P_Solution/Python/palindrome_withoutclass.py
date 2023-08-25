'''
Q2
objective : find if any given string is palidrome or not 
            inp_string="madam"
            inp_string="maths"
'''

#program to find pallindrome
    
#input here
inp_string="madam"

l=len(inp_string)
for i in range(0,l//2):
    if inp_string[i] != inp_string[l-1-i]:
        print("not a palindrome")
        break
    else:
        p = 1

if p == 1 : 
    print("yes pailndrome")
else:
    print("Not a palindrome")    