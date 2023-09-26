"""
1. create a class and object 
    1.a) create a constructor.
"""
class Employee:
    id=0
    def __init__(self,Age,Name):
      self.age=Age
      self.name=Name
    

if __name__=="__main__":
  Employee_1=Employee(20,"vipin")
  Employee_2=Employee(23,"kajal")
  Employee_1.id="25"
  Employee_2.id="100"
  print("ist employee","id:",Employee_1.id,"Age:",Employee_1.age, "Name:",Employee_1.name)
  print("2nd employee","id:",Employee_2.id,"Age:",Employee_2.age, "Name:",Employee_2.name)
