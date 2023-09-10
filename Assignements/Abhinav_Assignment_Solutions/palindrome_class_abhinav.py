
class Palindrome:
    def __init__(self, str1):
        self.str1= str1

    def if_palindrome(self):
        if self.str1 == self.str1[::-1]:
            return True
        else:
            return False
        
if __name__ == "__main__":

    userInput= input()
    obj= Palindrome(userInput)

    res= obj.if_palindrome()

    if res:
        print("string is plaindrome")
    else:
        print("string is not plaindrome")
