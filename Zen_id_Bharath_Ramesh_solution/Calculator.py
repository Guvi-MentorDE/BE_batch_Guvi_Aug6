#import#

class Calculator:
    
    def __init__(self, a, b): #constructor
        self.a = a
        self.b = b
    
    def add(self):
        c = "Addition of two numbers is " + str(self.a + self.b)
        return c

    def sub(self):
        c = "Subtraction of two numbers is " + str(self.a - self.b)
        return c

    def multip(self):
        c = "Multiplication of two numbers is " + str(self.a * self.b)
        return c

    def divis(self):
        c = "Division of two numbers is " + str(self.a / self.b)
        return c

if __name__ == "__main__":
    print("Enter the first number: ")
    a = int(input())
    print("Enter the second number: ")
    b = int(input())

    obj = Calculator(a, b)

    result = obj.add()
    print(result)

    result = obj.sub()
    print(result)

    result = obj.multip()
    print(result)

    result = obj.divis()
    print(result)