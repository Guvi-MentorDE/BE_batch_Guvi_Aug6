
"""
Question 4   :    1. accept a string from user.
                  2. check if the list is palindrome or not.
                  3. create a class and object 
                         3.a) create a constructor. 
                  4. access the logic of palindrome using object.method() 
"""
class String:
    def pelindrom(self,x):
        if x[::-1]==x:
            return "given string is palindrom"
        else:
            return "given string is not palindrom"
if __name__=="__main__":
    x=input("enter a string")
    obj=String()
    print(obj.pelindrom(x))
