class palindrome_check:
    def __init__(self,checkword):
        self.checkword = checkword

    def Find_Palindrome(self):
        ''' This function will check the given string
            are palindrome or not '''
        ln = len(self.checkword) - 1

        reversed_str = ''

        while ln >= 0:
            reversed_str  = reversed_str + self.checkword[ln]
            ln = ln - 1

        if  self.checkword ==  reversed_str :
            print('Input string is palidrome')
        else:
            print('Input string is not palidrome')


if __name__ == '__main__':
    str = input('Enter a string to check palindrome :')   
    check = palindrome_check(str) 
    check.Find_Palindrome()