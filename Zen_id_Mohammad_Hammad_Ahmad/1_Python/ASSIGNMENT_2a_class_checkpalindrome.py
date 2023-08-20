'''                                                     
                                                ASSIGNMENT-2


                                        Author  :   Mohammad Hammad Ahmad
                                        Course  :   ML Guvi - Python
                                        Date    :   19/08/2023



        Question 1 :

            1. accept a string from user.
            2. check if the list is palindrome or not.
            3. create a class and object
               3.a) create a constructor.
            4. access the logic of palindrome using object.method()
             
 '''

#          Solution :

#class checkpalindrome
class checkpalindrome:

    #constructor
    def __init__(self, s1):
        self.s1 = s1
        
    #methods   
    def show(self):
        print(f"Entered string is : {self.s1}")

    #method to check if input string is palindrome or not   
    def isPalindrome(self):
        
        s2=self.s1[::-1]
        s2=s2.lower()
        s3=self.s1.lower()

        if s3==s2:
            return print(f"Entered string '{self.s1}' is a palindrome")
        else:
            return print(f"Entered string '{self.s1}' is not a palindrome")
            
            
            
if __name__ == "__main__":
    
    #input
    str1 = input("Enter first string : ")

    # palindrome is an object of class checkpalindrome
    palindrome = checkpalindrome(str1)

    #checking if str1 is palindrome or not
    palindrome.isPalindrome()