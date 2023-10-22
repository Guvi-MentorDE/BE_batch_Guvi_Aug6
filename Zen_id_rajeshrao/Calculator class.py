#Calculator class
class calculator:
  def __init__(self, num1, num2):
    self.num1 = num1
    self.num2 = num2

  #Addition
  def add(self):
        return (self.num1 + self.num2)

    #Subtraction
  def sub(self):
        return self.num1 - self.num2

    #Multiplication
  def mul(self):
        return self.num1*self.num2

    #Decimal division
  def dec_div(self):
            return self.num1/self.num2

    #Integer division
  def int_div(self):
            return self.num1//self.num2

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
