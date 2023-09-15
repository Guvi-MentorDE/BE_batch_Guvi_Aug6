#                                             ASSIGNMENT 1b

#           Question 1. Create a function for detmining palidrome ,anagram and retun the result to the function call then print.

#           Solution :


def isPalindrome(s1):

    s2=s1[::-1]
    if s1==s2:
        return print(f"Entered string '{s1}' is a palindrome")
    else:
        return print(f"Entered string '{s1}' is not a palindrome")


def isAnagram(s1,s2):
    
    n=0
    for i in s1:
        for j in s2:
            if i==j:
                n+=1
    if n==len(s1):
        return print(f"Strings '{s1}' and '{s2}' are anagrams of eachother")
    else:
        return print(f"Strings '{s1}' and '{s2}' are not anagrams of eachother")
    
        
if __name__ == "__main__":
    
    str1 = input("Enter first string : ")
    str2 = input("Enter second string : ")
    isAnagram(str1,str2)
    
    str3 = input("Enter the string to check for palindrome : ")
    isPalindrome(str3)




#           Question 2. Create a function to accept one variable , which will return weather it is odd or even number.

#           2(a). Check if the accpeted input is interger or not , if not then throw exception.

#           Solution :


def isEvenorOdd(n1):
    if n1%2==0:
        return print(f"Entered number {n1} is an even number")
    else:
        return print(f"Entered number {n1} is an Odd number")
    
if __name__ == "__main__":
    try:
        num1 = input("Enter the number : ")
        int_num1 = int(num1)
        print(f"Input {int_num1} is an integer")
        isEvenorOdd(int_num1)
        
    except ValueError:
        print("Entered value is not an integer")