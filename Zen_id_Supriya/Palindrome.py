#1. accept a string from user.
#2. check if the list is palindrome or not.
#3. create a class and object 
#    3.a) create a constructor. 
#4. access the logic of palindrome using object.method() 


#import

class palindrome:

    def __init__(self,input):
            self.input=input

    def check_palindrome(self,user_input):
        reverse_string=''
        str_length=len(user_input)
        for i in range(0,str_length):
             reverse_string=user_input[i]+reverse_string
        print("Reverse of a string is",reverse_string)
        if user_input=='':
            print("Please enter a valid String")
        elif user_input==reverse_string:
            print("String is palindrome")
        else:
            print("String is not palindrome")
        return user_input

if __name__ == "__main__":
    user_input=input("Enter the string:")
    print("String entered is",user_input)
    palin=palindrome(user_input)
    palin.check_palindrome(user_input)



