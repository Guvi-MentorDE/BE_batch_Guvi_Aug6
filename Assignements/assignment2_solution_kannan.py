"""
  Assignment 2
  Author  :   Kannan Kandasamy
  Course  :   ML Guvi - Python
  Date    :   06/08/2023
  Details :   Find a number is odd or even, if it is not an integer throw and exception
"""

class Numbers:
  #function definition to check even or odd
  def is_odd_or_even(self, i):
    return("even" if i%2==0 else "odd")

#main function
if __name__ == "__main__":
  obj_num = Numbers()
  ip = input("Enter a number: ")
  try:
    op = obj_num.is_odd_or_even(int(ip))
    print("Number is " + op)
  except:
    print("Number entered is not an integer")