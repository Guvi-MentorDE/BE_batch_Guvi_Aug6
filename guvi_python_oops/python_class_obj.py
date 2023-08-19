#import stmsts 


#.py -> interpreter -> go to main line , check for class - objects -> if there is __init__ 


#class declaration
class Arithmetic:
    a=0;
    b=0;                #initialization 
    pi=3.14;
    operation='sub'
    
    #def __init__(self): #constructor 
    #    pass 
    
    def fun(self):
        #print("self.operation="+self.operation)
        if self.operation=='add':
            return self.a+self.b 
        
        
if __name__ == "__main__":
#object creation for class     
    obj = Arithmetic()
    print("creating object")
    obj.a =1
    obj.b =2
    obj.operation='add'
    print("calling a class method")
    result = obj.fun()  #method call  #(functions/methods)
    print("result:",result)