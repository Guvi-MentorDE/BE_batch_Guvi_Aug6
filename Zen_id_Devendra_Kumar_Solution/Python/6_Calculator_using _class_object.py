"""
                                                 Assignment 
                                             ------------------                                    
  Author  :   Devendra Kumar Rajendran
  Course  :   ML - Python
  Date    :   12/08/2023
-----------------------------------------------------------------------------------------------------------
  Question :  
  1. create a class called calculator.
  2. accept 2 inputs from user, and pass it to the class. 
    2.a) create a constructor for the same.
  3. objects has to be add, sub, mul , div 
  4. create seperate methods to do above object realted operations.
  5. complete the logic within add, sub  , mul, div and return.

---------------------------------------------------------------------------------------------------------------
"""
# Solutions  :

class Calculator:
    
 def __init__(self, a, b):
  self.a = a
  self.b = b

 def add(self):
  return self.a + self.b
  

 def sub(self):
  return self.a - self.b

 def mul(self):
  return self.a * self.b

 def div(self):
  return self.a / self.b

if __name__ == "__main__":
  a = int(input( " Enter a value - a  :" ))
  b = int(input( " Enter a value - b  :"))

  arth_oper = Calculator(a,b)  

  result = arth_oper.add()
  print("*"*50)
  print("Addition Value is       :", result)
  
  result = arth_oper.sub() 
  print("subtraction Value is    :", result)
  
  result = arth_oper.mul()
  print("Multiplication Value is :", result)
  
  result = arth_oper.div()
  print("Division Value is       :", result)
  print("*"*50)

