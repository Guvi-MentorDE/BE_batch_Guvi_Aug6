
class Calculator:
       
    def add(self, a, b):
        print("add results is: " + str(a+b))

    def subtract(self, a, b):
        print("subtract results is: "+ str(a-b))

    def multiply(self, a, b):
        print("multiply results is : "+ str(a*b))

    def divide(self, a, b):
        print("devide result is: "+ str(a/b))


if __name__ == "__main__":
    a = 10
    b= 2
    obj= Calculator()

    obj.add(a,b)
    obj.subtract(a,b)
    obj.multiply(a,b)
    obj.divide(a,b)