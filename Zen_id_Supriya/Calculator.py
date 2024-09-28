class Calculator:
    
    def __init__(self,number1,number2):
        self.number1 = number1
        self.number2 = number2
    
    def addition(self):
       return(self.number1+self.number2)

    def substraction(self):
       return(self.number1-self.number2)
    
    def multiplication(self):
        return(self.number1*self.number2)

    def division(self):
        try:
            return(self.number1/self.number2)
        except(ZeroDivisionError):
            print("Please enter valid numbers")

if __name__ == "__main__":
    a=int(input("Enter first number\n"))
    b=int(input("Enter second number\n"))
    cal = Calculator(a,b)
    result_add = cal.addition()
    result_sub = cal.substraction()
    result2_multiply = cal.multiplication()
    result3_divide = cal.division()
    print("Addition of numbers is",result_add)
    print("Substraction of numbers is",result_sub)
    print("Multiplication of numbers is",result2_multiply)
    print("Division of numbers is",result3_divide)