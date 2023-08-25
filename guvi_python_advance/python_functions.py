#from ast import main
from cmath import e
import pandas
import time 
import csv 

#function is defined by a keyword 'def'

#(a+b)^2 = a2 + b2 + 2ab
#def which can be used commenly across the programs or process or by developers. 
#write once and use it many time. 


def main():                 #<--- function definetion  , function without argument 
  print("Hello from a my first function")

def myfun():
    a=10
    b=5
    c=a+b
    print("next function",c)
    
def foumule(a,b):    # a=1, b = 2 ;  # main method i can pass any value to a,b 
    result = (a*a)+(b*b)+ 2*(a*b) 
    #print('my calulated result for (a+b)^2:',result)
    return result 

def fun2(listx):        #<---- function with argument , [20,30,10,40] will be copied into list1 
    for x in listx:     #list1 is a local variable , scope only within def fun2
        print(x)
    else:
        print("Task finished")


def math(a,b,operation):
    try:
        if operation == 'div':
            print("division result of a/b=",a/b) 
        elif operation == 'mul':
            print("multiplication result a*b=",a*b )    
    except e:
        print("Oops! Something went wrong!",e)
         

def case_method(a,b,operation):
    try:
        match operation:
            case 'div':
                print("division result of a/b=",a/b)
            case 'mul':
                print("division result of a/b=",a*b)
            case _:
                print("invalid")
    except e:
        print("exception occured in the case method",e)
        
def math_op(a,b,operation):
    if operation == 'div':
        return a/b
    elif operation == 'mul':
        return a*b
    else: 
        return 0  
   


if __name__ == "__main__":                  #1. main - exution begins
    #basic function: without arguments 
    #method , function = one and same
    main()      #<--------calling a function
    myfun()
    result_frm_function1=foumule(1,2)
    
    result_frm_function2=foumule(3,4)
    
    result_frm_function3=foumule(3,4)
    
    #function with arguments 
    #fun2([20,30,10,40])
   
    #math(2,2,'div')
    case_method(2,0,'div')
    
    #function with return value 
    result=math_op(2,2,'mul')
    print("result of math_op function:",result)
     



#call by value and reference : for later