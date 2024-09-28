"""
  Assignment 4
  Author  :   Saleh Md Hedayatullah
  Course  :   ML Guvi - Python
  Details :   To check if a number is odd or even using try and except block
"""

class Numbers:
  def odd_or_even(self, num):         #function definition to check even or odd
    return("even" if num%2==0 else "odd")

#main function
if __name__ == "__main__":
  objectt = Numbers()
  numbr = input("Enter any number: ")
  try:
    result = objectt.odd_or_even(int(numbr))
    print("Number is " + result)
  except:
    print("Number entered is not an integer")