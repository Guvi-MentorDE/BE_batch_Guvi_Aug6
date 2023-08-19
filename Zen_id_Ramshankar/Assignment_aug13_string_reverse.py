import math

if __name__=="__main__":
    print("Enter the string to be reversed:")
    string_input=input()
    length=len(string_input)-1
    rev=[]
    while length>=0:
        rev.append(string_input[length])
        length=length-1
    print(''.join(rev))


