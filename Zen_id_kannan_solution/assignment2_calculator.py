"""
  Assignment 2 - Calculator
  Author  :   Kannan Kandasamy
  Course  :   ML Guvi - Python
  Date    :   13/08/2023
  Details :   Getting 2 inputs and complete logic of add, sub, mul, div
"""

class Calculator:
  
  def __init__(self, n1, n2):
    self.num1 = n1
    self.num2 = n2

  #adding two numbers
  def add(self):
    return(self.num1+self.num2)

  #adding two numbers
  def add(self, n1, n2):
    return(n1+n2)

  def sub(self):
    return(self.num1-self.num2)

  #adding two numbers
  def mul(self):
    return(self.num1*self.num2)

  #adding two numbers
  def div(self):
    return(self.num1/self.num2)    

#main function
if __name__ == "__main__":
  ip1, ip2 = int(input("Enter first number: ")), int(input("Enter second number: "))
  op = input("""Enter operation: 
                add
                sub
                mul
                div
                """)
  calc = Calculator(ip1,ip2)
  print("Result : ")
  match op:
    case "add":
      print(calc.add())
    case "sub":
      print(calc.sub())
    case "mul":
      print(calc.mul())
    case "div":
      print(calc.div())
    case _:
      print("command not recognized")