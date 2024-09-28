class Palindrome:
    def __init__(self,str1):
        self.str1=str1
    
    def check_palindrome(self):
        str2=self.str1[::-1]
        if(self.str1==str2):
            print(self.str1," is a palindrome")
        else:
            print(self.str1," is not a palindrome")

if __name__=="__main__":
    print("Enter a string to check for palindrome")
    inp1=input()
    p1=Palindrome(inp1)
    p1.check_palindrome()
