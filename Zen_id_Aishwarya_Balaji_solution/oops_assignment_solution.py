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

  #Palindrome method
  def check_palindrome(self):
    return(f"{self.my_str} is palindrome" if(self.my_str == self.my_str[::-1]) else f"{self.my_str} is not a palindrome")

#Main
if __name__ == '__main__':
  #Get the string
  get_str = input("Enter a string: ")

  #Create an object for the class
  obj = my_class(get_str)
  #Call the methods
  print(obj.check_palindrome())


'''Q2) 

1. create a class called calculator.
2. accept 2 inputs from user, and pass it to the class. 
    2.a) create a constructor for the same.
3. objects has to be add, sub, mul , div 
4. create seperate methods to do above object realted operations.
5. complete the logic within add, sub  , mul, div and return.'''

#Calculator class
class calculator:
  #Constructor
  def __init__(self, num1, num2):
    self.num1 = num1
    self.num2 = num2

  #Addition
  def add(self):
    return(f"Addition of {self.num1} & {self.num2} is {self.num1+self.num2}")

  #Subtraction
  def sub(self):
    return(f"Subtraction of {self.num1} & {self.num2} is {self.num1-self.num2}")

  #Multiplication
  def mul(self):
    return(f"Multiplication of {self.num1} & {self.num2} is {self.num1*self.num2}")

  #Decimal division
  def dec_div(self):
    return(f"Decimal division of {self.num1} & {self.num2} is {self.num1/self.num2}")

  #Integer division
  def int_div(self):
    return(f"Integer division of {self.num1} & {self.num2} is {self.num1//self.num2}")

  #Modulo
  def mod(self):
    return(f"Reminder of {self.num1} & {self.num2} is {self.num1%self.num2}")

#Main
if __name__ == '__main__':
  #Get two numbers
  no_1 = int(input("Enter number1: "))
  no_2 = int(input("Enter number2: "))

  #Create an object for the class
  calc = calculator(no_1, no_2)
  #Call the methods
  print(calc.add())
  print(calc.sub())
  print(calc.mul())
  print(calc.dec_div())
  print(calc.int_div())
  print(calc.mod())
