#import <modules>

# define once , call many time 


def looping_list(my_list):   #creatig a function # mandatory , priority 1 
     print("i am into looping_list function")
     for i in my_list:
         print(i)
         

def looping_insertion():   #creatig a function # mandatory , priority 1 
     print("i am into looping_list function")

    
def formule(local_x , local_y):
    print(local_x)
    print(local_y)
    result = (local_x)**2 + (local_y)**2 + 2*local_x*local_y 
    return result  

def formule_mul(local_x , local_y):
    print(local_x)
    print(local_y)
    x = local_x * 100 
    y = local_y * 100
    return x,y 
          

if __name__ == "__main__":   # main method , entry point for python program 
    print("i am into python main method")
    #my_list=[1,2,3,4,5]
    a = int (input("enter a ? "))  
    b = int (input("enter b ? "))  

    res1 = formule(a,b)
    print(res1)
    
    final_result = res1 * 100 
    print("final_result" + str(final_result))
    
    
    #c = int (input("enter c ? "))  
    #d = int (input("enter d ? "))  

    #res2 = formule2(c,d)
    #print("printing result for c +d ^2 :"+str(res2))
    
    
    x,y = formule_mul(a,b)
    
    print("result of x, y=" +str(x)+' '+str(y))
    
    
    #looping_list(my_list) #function calling # mandatory  priority 2
    #looping_insertion(my_list)
    
    
    
# python code -> interpretter -> byte code -> human redable o/p