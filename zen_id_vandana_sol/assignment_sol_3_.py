"""
Date       :   13,Aug,2013
Topic      :   OOPS
Question.1 :   1.create a class called calculator.
               2. accept 2 inputs from user, and pass it to the class. 
                      2.a) create a constructor for the same.
               3. objects has to be add, sub, mul , div 
               4. create seperate methods to do above object realted operations.
               5. complete the logic within add, sub  , mul, div and return.
"""

class calculator:
    def __init__(self):
        self.x=float(input("enter first number"))
        self.y=float(input("enter second number"))
    def ADD(self):
       return self.x+self.y
    def SUB(self):
        return self.x-self.y
    def MUL(self):
        return self.x*self.y
    def DIV(self):
        if self.y!=0:
            return self.x/self.y
        else:
            return("must enter non zero value")
        
if __name__=="__main__":
  C1=calculator()
  print("adittion:", C1.ADD())
  print("subtraction:",C1.SUB())
  print("Multiplication:",C1.MUL())
  print("Division:",C1.DIV())

"""
Question 2   :    1. accept a string from user.
                  2. check if the list is palindrome or not.
                  3. create a class and object 
                         3.a) create a constructor. 
                  4. access the logic of palindrome using object.method() 
"""
class String:
    def pelindrom(self,x):
        if x[::-1]==x:
            return "given string is palindrom"
        else:
            return "given string is not palindrom"
if __name__=="__main__":
    x=input("enter a string")
    obj=String()
    print(obj.pelindrom(x))
