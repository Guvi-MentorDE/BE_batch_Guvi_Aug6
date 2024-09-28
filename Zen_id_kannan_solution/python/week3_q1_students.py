"""
  Assignment 3
  Author  :   Kannan Kandasamy
  Course  :   ML Guvi - Python
  Date    :   13/08/2023
  Details :   Inheritance, identifying pass or fail
"""

class High_School:
  pass_mark = 40

  def __init__(self, pm=40):
    self.pass_mark = pm

  def get_pass_mark(self):
    return self.pass_mark

class Students(High_School):
  def is_pass(self,marks):
    return all(True if i>=self.pass_mark else False for i in marks)

if __name__=="__main__":
  arun = Students()
  ip = input("Enter marks for English,maths,science,social in comma separated : ").split(",")
  ip = list(map(int, ip))
  print("Students Results : ")
  print("PASS" if arun.is_pass(ip) else "FAIL")
  print("Actual Passmark : ")
  print(arun.get_pass_mark())

  #with passmark of 60  
  grad_student = Students(60)
  ip = input("Enter marks for English,maths,science,social in comma separated : ").split(",")
  ip = list(map(int, ip))
  print("Students Results : ")
  print("PASS" if grad_student.is_pass(ip) else "FAIL")
  print("Actual Passmark : ")
  print(grad_student.get_pass_mark())