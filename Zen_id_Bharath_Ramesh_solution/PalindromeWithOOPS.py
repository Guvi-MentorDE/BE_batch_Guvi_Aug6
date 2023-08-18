#import

class Ispalindrome:
    
    def __init__(self,str):
        self.str = str

    def check_if_palindrome(self):
        str1 = self.str
        str2 = str1[::-1]
        
        if str1 == str2:
            return 'The input string is a palindrome'
        else:
            return 'The input string is not a palindrome'

if __name__ == "__main__":
    print("Enter a input string/n")
    str = input()
    main_obj = Ispalindrome(str)

    result = main_obj.check_if_palindrome()

    print(result)