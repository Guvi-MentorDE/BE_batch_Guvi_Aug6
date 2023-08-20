'''
                                                ASSIGNMENT-2


                                        Author  :   Mohammad Hammad Ahmad
                                        Course  :   ML Guvi - Python
                                        Date    :   19/08/2023

        Question 2:

            1. create a class called calculator.
            2. accept 2 inputs from user, and pass it to the class. 
                2.a) create a constructor for the same.
            3. objects has to be add, sub, mul , div 
            4. create seperate methods to do above object realted operations.
            5. complete the logic within add, sub, mul, div and return.

'''

# Solution : 

#class
class calculator:

    #constructor
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
    #methods in calculator
    def add(self, n1, n2):
        sum = n1+n2
        return sum
    def sub(self, n1, n2):
        diff = n1-n2
        return diff
    def multiply(self, n1, n2):
        prod = n1*n2
        return prod
    def divide(self, n1, n2):
        div = n1/n2
        return div
    
if __name__ == "__main__":
    
    #input
    num1 = int(input("Enter first number : "))
    num2 = int(input("Enter second number : "))
    operator = input(" Select the operation which you want to do ( E.g: + , - , * , /) : ")

    #c1 is object of class calculator
    c1 = calculator(num1,num2)
    
    #matching with input 'operator' so as to which operation to perform
    match operator:
        case '+':
            addc1 = c1.add(num1,num2)
            print(f"{num1} + {num2} = {addc1}")
        case '-':
            subc1 = c1.sub(num1,num2)
            print(f"{num1} - {num2} = {subc1}")
        case '*':
            mulc1 = c1.multiply(num1,num2)
            print(f"{num1} * {num2} = {mulc1}")
        case '/':
            divc1 = c1.divide(num1,num2)
            print(f"{num1} / {num2} = {divc1}")
        