'''
Q1)
1. accept a string from user.
2. check if the list is palindrome or not.
3. create a class and object 
    3.a) create a constructor. 
4. access the logic of palindrome using object.method() 
'''

class stringcheck:

    def __init__(self,strinput):
        self.strinput=strinput

    def ispalindrome(self):
        length = len(self.strinput)   
        for i in range(0,length//2):
            if self.strinput[i] != self.strinput[length-1-i]:
                return False
        return True    

if __name__=="__main__":

    getstring=str(input())
    check = stringcheck(getstring)
    if check.ispalindrome():
        print("Yes Palindrome")
    else:
        print("Not a Palindrome")    