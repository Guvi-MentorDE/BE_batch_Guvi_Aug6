'''Q1)

1. accept a string from user.
2. check if the list is palindrome or not.
3. create a class and object 
    3.a) create a constructor. 
4. access the logic of palindrome using object.method() '''

#Class
class my_class:
  #Constructor
  def __init__(self, my_str):
    self.my_str = my_str

  #Palindrome function
  def check_palindrome(self):
    return(f"{self.my_str} is palindrome" if(self.my_str == self.my_str[::-1]) else f"{self.my_str} is not a palindrome")

#Main
if __name__ == '__main__':
  get_str = input("Enter a string: ")

  #Call the class
  obj = my_class(get_str)
  print(obj.check_palindrome())


'''Q2) 

1. create a class called calculator.
2. accept 2 inputs from user, and pass it to the class. 
    2.a) create a constructor for the same.
3. objects has to be add, sub, mul , div 
4. create seperate methods to do above object realted operations.
5. complete the logic within add, sub  , mul, div and return.'''
