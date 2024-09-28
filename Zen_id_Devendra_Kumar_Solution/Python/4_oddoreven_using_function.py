"""
                                                  Assignment
                                               ----------------
  Author   :   Devendra Kumar Rajendran
  Course   :   ML - Python
  Date     :   12/08/2023

  ------------------------------------------------------------------------------------------------------
  Question :  
  Vs code  :
  --------
      1. create a python project structure in code
	      a) main
       	b) fucntion def
	      c) function call with parameters
      2. impliment the logic : odd_or_even
      3. modify the code for the above logic thats fits into class and objects.
---------------------------------------------------------------------------------------------------------
"""
# Solutions : 

#import <modules>

def oddoreven(num):             # Define Function
  if num%2==0:
   print(f" Number {num} is Even number")
  else:
    print (f" Number {num} is Odd number")

if __name__ == "__main__":       # Main Method 

 n = int(input("Enter the number to check Odd or Even : "))
 oddoreven(n)                     # function call