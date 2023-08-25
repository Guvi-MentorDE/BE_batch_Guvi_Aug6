# First Method
# Getting 2 inputs and complete logic of add, sub, mul, div
class Calculator:
    def __init__(self,n1,n2):  
        self.a = n1
        self.b = n2
    
    def add(self,n1,n2):
        return (n1+n2)
    def sub(self,n1,n2):
        return (n1-n2)
    def multiply(self,n1,n2):
        return (n1*n2)
    def div(self,n1,n2):
        return (n1/n2)
        
def main():
    n1 = int(input('Enter first number:'))
    n2 = int(input('Enter second number:'))
    op = input('Enter any one operation:add/sub/multiply/div: ')
    obj = Calculator(n1,n2)  
    if op == "add":
        print(obj.add(n1,n2))
    elif op == "sub":
        print(obj.sub(n1,n2))
    elif op == "multiply":
        print(obj.multiply(n1,n2))
    elif op == "div":
        print(obj.div(n1,n2))
    else:
        print("Oops something went wrong")

if __name__ == '__main__':
    main()



#  Second Method
#Getting 2 inputs and complete logic of add, sub, mul, div
class Calculator:
    def __init__(self, n1, n2):  
        self.n1 = n1
        self.n2 = n2
    
    def add(self):
        return (self.n1+self.n2)
    def sub(self):
        return (self.n1-self.n2)
    def multiply(self):
        return (self.n1*self.n2)
    def div(self):
        return (self.n1/self.n2)

def main():
    n1 = int(input('Enter first number:'))
    n2 = int(input('Enter second number:'))
    op = input('Enter any one operation:add/sub/multiply/div: ')
    obj = Calculator(n1,n2)  
    if op == "add":
        print(obj.add())
    elif op == "sub":
        print(obj.sub())
    elif op == "multiply":
        print(obj.multiply())
    elif op == "div":
        print(obj.div())
    else:
        print("Oops something went wrong")

if __name__ == '__main__':
    main()