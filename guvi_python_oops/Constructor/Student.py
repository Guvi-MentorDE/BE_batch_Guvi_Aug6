class Student:

    # constructor
    # initialize instance variable
    def __init__(self, name):
        print('Inside Constructor')
        self.name = name
        print('All variables initialized')

    # instance Method
    def show(self):
        print('Hello, my name is', self.name)

if __name__ == "__main__":      #<-------- start 
    # create object using constructor
    s1 = Student('Emma')
    s1.show()
