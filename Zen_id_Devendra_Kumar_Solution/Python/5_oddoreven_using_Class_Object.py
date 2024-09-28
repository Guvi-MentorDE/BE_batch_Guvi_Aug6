"""
                                               Assignment
                                          --------------------
   Author    :   Devendra Kumar Rajendran
   Course    :   ML - Python
   Date      :   12/08/2023
-------------------------------------------------------------------------------------------------------- 
   Question  :  
   Vs code :
   --------
2. impliment the logic : odd_or_even
3. modify the code for the above logic thats fits into class and objects.
------------------------------------------------------------------------------------------------------------
"""

# Solutions :


#import <modules>  

class Number_check:               # Define Class
 
 def __init__(self,num):          # Constructor
  self.num = num
  
 def oddoreven(self):             # Define method
   if self.num%2==0:
    print(f" Number {self.num} is Even number")
   else:
    print (f" Number {self.num} is Odd number")

if __name__ == "__main__":       # Main Method 
 
 n = int(input("Enter the number to check Odd or Even : "))
 obj_check = Number_check(n) 
 obj_check.oddoreven()             # object method call






















# class oddoreven:
  
#  def validate(num):             # Define Function
#   if num%2==0:
#    print(f" Number {num} is Even number")
#   else:
#    print (f" Number {num} is Odd number")

# if __name__ == "__main__":       # Main Method 

#  n = int(input("Enter the number to check Odd or Even : "))
#  obj_num = oddoreven()                 # function call
#  obj_num.validate(n)
 