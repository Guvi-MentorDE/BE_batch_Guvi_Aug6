import math 

class Person:
    
    age=0
    def __init__(self, name, gender, profession):     #constructor
        # data members (instance variables)
        self.name = name                  
        self.gender = gender
        self.profession = profession
         
    # Behavior (instance methods)
    def show(self):
        print('Name:', self.name, 'gender:', self.gender, 'age:' ,self.age)
        print(self.name, 'I am working as a ', self.profession)


    # Behavior (instance methods)
    #def work(self):                         #methods 
    #    print(self.name, 'I am working as a ', self.profession)

if __name__ == "__main__": 
    Mary = Person('Mary', 'Female', 'Software Engineer')
    Mary.profession="civil engineer"
    Mary.age=24
    Mary.show()
    #Mary.work()
    
    Dave = Person('Dave', 'Male', 'Civil Engineer')
    Dave.show()
    #Dave.work()