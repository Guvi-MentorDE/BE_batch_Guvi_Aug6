def Find_Palindrome(Str):
    ''' This function will check the given string
        are palindrome or not '''
    ln = len(Str) - 1

    reversed_str = ''

    while ln >= 0:
        reversed_str  = reversed_str + str[ln]
        ln = ln - 1

    if  Str ==  reversed_str :
        print('Input string is palidrome')
    else:
        print('Input string is not palidrome')


if __name__ == '__main__':
    str = input('Enter a string to check palindrome :')    
    Find_Palindrome(str)