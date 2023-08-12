#Python Generators are the functions that return the traversal object and used to create iterators. 
#It traverses the entire items at once.
#def function_name():
#    yield statement 
    
def simple():
    for i in range(10):  
        if(i%2==0):  
            yield i  
  
#Successive Function call using for loop  
#for i in simple():  
#    print(i)  

#yield vs. return
#The yield statement is responsible for controlling the flow of the generator function. 
#It pauses the function execution by saving all states and yielded to the caller.
#Later it resumes execution when a successive function is called. 
#We can use the multiple yield statement in the generator function