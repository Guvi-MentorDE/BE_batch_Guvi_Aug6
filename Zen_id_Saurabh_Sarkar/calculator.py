
"""
Q) 
1. create a class called calculator.
2. accept 2 inputs from user, and pass it to the class. 
    2.a) create a constructor for the same.
3. objects has to be add, sub, mul , div 
4. create seperate methods to do above object realted operations.
5. complete the logic within add, sub  , mul, div and return.
"""

def add(P, Q):    
      return P + Q   
def subtract(P, Q):   
     return P - Q   
def multiply(P, Q):   
      return P * Q   
def divide(P, Q):   
    return P / Q    
  
print ("Please select the operation.")    
print ("a. Add")    
print ("b. Subtract")    
print ("c. Multiply")    
print ("d. Divide")    
    
choice = input("Please enter choice (a/ b/ c/ d): ")    
    
num_1 = int (input ("Please enter the first number: "))    
num_2 = int (input ("Please enter the second number: "))    
    
if choice == 'a':    
   print (num_1, " + ", num_2, " = ", add(num_1, num_2))    
    
elif choice == 'b':    
   print (num_1, " - ", num_2, " = ", subtract(num_1, num_2))    
    
elif choice == 'c':    
   print (num_1, " * ", num_2, " = ", multiply(num_1, num_2))    
elif choice == 'd':    
   print (num_1, " / ", num_2, " = ", divide(num_1, num_2))    
else:    
   print ("This is an invalid input")

