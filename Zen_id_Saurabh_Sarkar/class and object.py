
"""
1. create a class and object 
    1.a) create a constructor.
"""


# 1. create a class and object solution

class Employee:    
    employee_id = 0

employee1 = Employee()
employee2 = Employee()

employee1.employeeID = 1001
print(f"Employee ID: {employee1.employeeID}")

employee2.employeeID = 1002
print(f"Employee ID: {employee2.employeeID}")


# 1.a) create a constructor.

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Amit", 35)

print(p1.name)
print(p1.age)
