
# (a) When string is to be given

string=input(("Enter a string:"))
if(string==string[::-1]):
      print("The string is a palindrome")
else:
      print("Not a palindrome")



# (b) When string is given


def isPalindrome(s):
    return s == s[::-1]

s = "madam"
ans = isPalindrome(s)
 
if ans:
    print("Yes")
else:
    print("No")

