import math
class Calculator:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    
    def add(self):
        res=self.num1+self.num2
        return res
    
    def subtract(self):
        res=self.num1+self.num2
        return res
    
    def multiply(self):
        res=self.num1*self.num2
        return res
    
    def divide(self):
        try:
            res=(self.num1/self.num2)
        except ZeroDivisionError:
            print("The second number should not be 0")
        return res
    
if __name__=="__main__":
    print("Enter 2 numbers to check the arithmatic operations")
    print("Enter 1st number")
    a=int(input())
    print("Enter 2nd number")
    b=int(input())
    cal_obj=Calculator(a,b)
    add_result=cal_obj.add()
    print("The result of addition:",add_result)
    sub_result=cal_obj.subtract()
    print("The result of subtraction:",sub_result)
    mul_result=cal_obj.multiply()
    print("The result of multiplication is:",mul_result)
    div_result=cal_obj.divide()
    print("The result of division is:",div_result)


