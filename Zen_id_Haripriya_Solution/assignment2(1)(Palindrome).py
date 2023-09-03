
class Palindrome:
    def check_palindrome(self,st):
        if st==st[::-1]:
            print(s," is a palindrome")
        else:
            print(s," is not a palindrome")



if __name__=="__main__":
    obj=Palindrome()
    s=input("Enter the string to find whether palindrome or not?")
    obj.check_palindrome(s)
