# QUESTION:
#1. create a class called calculator.
#2. accept 2 inputs from user, and pass it to the class. 
#    2.a) create a constructor for the same.
#3. objects has to be add, sub, mul , div 
#4. create seperate methods to do above object realted operations.
#5. complete the logic within add, sub  , mul, div and return.

#SOLUTION:
#Create class and perform arthimetic operations using constructor
class calculator:

    def __init__ (self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    def add(self):
        return self.number1 + self.number2
    
    def sub(self):
        return self.number1 - self.number2
    
    def mul(self):
        return self.number1 * self.number2
    
    def div(self):
        return self.number1 / self.number2

if __name__ == "__main__":
    number1, number2 = int(input("Enter first Number: ")),int(input("Enter second Number: "))
    
    add = calculator(number1, number2)
    sub = calculator(number1, number2)
    mul = calculator(number1, number2)
    div = calculator(number1, number2)

    print("Addition = ", add.add())
    print("Subtraction = ", sub.sub())
    print("Multiplication = ", mul.mul())
    print("Division = ", div.div())