"""
  Assignment : Week 3 - Q3 - Reverse a string manually
  Author  :   Kannan Kandasamy
  Course  :   ML Guvi - Python
  Date    :   15/08/2023
  Details :   Manually reverse using string
"""

class Strings:
  def __init__(self,s1="",s2=""):
    self.str1 = s1
    self.str2 = s2

  def get_reverse(self,str=""):
    rev = lambda x: "".join(x[i] for i in range(len(x)-1,-1,-1))
    return rev(str)

#main function
if __name__ == "__main__":
  ip = input("Enter a string to Reverse: ")
  obj = Strings()
  print(obj.get_reverse(ip))