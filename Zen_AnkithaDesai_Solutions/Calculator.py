'''
Author: Ankitha Desai
Date Created:: 19-08-2023
Description: This file contains the code for calculator
'''

'''
1. create a class called calculator.
2. accept 2 inputs from user, and pass it to the class. 
    2.a) create a constructor for the same.
3. objects has to be add, sub, mul , div 
4. create seperate methods to do above object realted operations.
5. complete the logic within add, sub  , mul, div and return.

'''

class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def sub(self):
        return self.num1 - self.num2

    def mul(self):
        return self.num1 * self.num2

    def div(self):
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            return "Cannot divide by zero"


if __name__ == "__main__":
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    calculator = Calculator(num1, num2)

    print("Sum:", calculator.add())
    print("Difference:", calculator.sub())
    print("Product:", calculator.mul())
    print("Quotient:", calculator.div())
