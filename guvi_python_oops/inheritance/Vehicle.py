# Base class/Parent class 
class Vehicle:
    def Vehicle_info(self):
        print('Inside Vehicle class')

# Child class
class Car(Vehicle):
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def car_info(self):
        print('Inside Car class')

# Create object of Car
car = Car(10,11)

# access Vehicle's info using car object
car.Vehicle_info()
car.car_info()
