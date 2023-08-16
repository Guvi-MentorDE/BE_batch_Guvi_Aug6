class Student:
    # class variables
    school_name = 'ABC School'

    # constructor
    def __init__(self, name, age):
        # instance variables
        self.name = name   # object variables / intance variable 
        self.age = age
    
    def show():        # class methods 
        print("hi my name and age is:" +self.name+' '+ self.age)

if __name__ == "__main__": 
    s1 = Student("Harry", 12)
    # access instance variables
    print('Student:', s1.name, s1.age)

    # access class variable
    print('School name:', s1.school_name)


    # Modify instance variables
    s1.name = 'Jessa'
    s1.age = 14
    print('Student:', s1.name, s1.age)

    # Modify class variables
    s1.school_name = 'XYZ School'
    print('School name:', s1.school_name)
    
    
    s2 = Student()
    s2.name= 'abc'
    s2.age = '10'