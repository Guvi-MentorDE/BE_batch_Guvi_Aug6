'''Q1)

1. accept a string from user.
2. check if the list is palindrome or not.
3. create a class and object 
    3.a) create a constructor. 
4. access the logic of palindrome using object.method() '''

#Class
class palindrome:
  #Constructor
  def __init__(self, my_str):
    self.my_str = my_str

  #Palindrome method
  def check_palindrome(self):
    return(f"{self.my_str} is palindrome" if(self.my_str == self.my_str[::-1]) else f"{self.my_str} is not a palindrome")

#Main
if __name__ == '__main__':
  #Get the string
  get_str = input("Enter a string: ")

  #Create an object for the class
  obj = palindrome(get_str)
  #Call the methods
  print(obj.check_palindrome())
