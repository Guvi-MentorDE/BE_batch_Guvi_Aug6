'''
Q2) 
1. create a class called calculator.
2. accept 2 inputs from user, and pass it to the class. 
   2.a) create a constructor for the same.
3. objects has to be add, sub, mul , div 
4. create seperate methods to do above object realted operations.
5. complete the logic within add, sub  , mul, div and return.
'''

class calculator:

    def __init__(self,num1,num2):
        if num1>num2:
            self.num1=num1
            self.num2=num2
        else:
            self.num1=num2
            self.num2=num1                

    def add(self):
        return self.num1+self.num2

    def sub(self):
        return self.num1-self.num2

    def multiply(self):
        return self.num1*self.num2       

    def divide(self):
        return self.num1/self.num2    

if __name__=="__main__":

    num1=int(input("Enter num1:"))
    num2=int(input("Enter num2:"))
    #creating a calculator object
    cal = calculator(num1,num2)

    print("add:",cal.add())
    print("sub:",cal.sub())
    print("multiply:",cal.multiply())
    print("divide:",cal.divide())