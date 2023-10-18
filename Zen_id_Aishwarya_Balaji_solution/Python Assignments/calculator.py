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