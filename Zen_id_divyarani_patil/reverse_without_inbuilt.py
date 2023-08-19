def reverse(a):
    str = ""
    for i in a:
        str = i + str
    return str
 
a = input()
 
print("The string is : ", end="")
print(a)
 
print("Reversed string is  : ", end="")
print(reverse(a))