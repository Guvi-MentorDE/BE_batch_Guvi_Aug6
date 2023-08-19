def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str
 
s = input()
 
print("The string is : ", end="")
print(s)
 
print("Reversed string is  : ", end="")
print(reverse(s))