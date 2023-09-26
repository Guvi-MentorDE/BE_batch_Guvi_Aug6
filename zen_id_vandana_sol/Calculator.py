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
       try:
           return self.x+self.y
       except ValueError:
           print("Only numeric value allowed to be added")
    def SUB(self):
        try:
          return self.x-self.y
        except ValueError:
            print("only numeric value can be subtracted")
    def MUL(self):
        try:
            return self.x*self.y
        except ValueError:
            print("only numeric value can be multiplied")
    def DIV(self):
        try:
          if self.y!=0:
              return round(self.x/self.y,2)
        except ZeroDivisionError:
              print("must enter non zero value")
                
if __name__=="__main__":
  C1=calculator()
  print("adittion:", C1.ADD())
  print("subtraction:",C1.SUB())
  print("Multiplication:",C1.MUL())
  print("Division:",C1.DIV())
