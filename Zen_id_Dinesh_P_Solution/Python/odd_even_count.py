
'''
1. create a python project structure in code 
	a) main 
	b) fucntion def
	c) function call with parameters 	
2. impliment the logic : odd_or_even 
3. modify the code for the above logic thats fits into class and objects. 

'''

class compare:

    def __init__(self,mylist):
        self.mylist = mylist
        

    def odd_even_count(self):
        oddcount=[]
        evencount=[]
        for i in self.mylist:
            if i%2==0:
                evencount.append(i)
            else:
                oddcount.append(i)

        return len(oddcount),len(evencount)   
        
if __name__ == "__main__":

    list1 = [1,3,6,7,10,12,34,13,88,3,8,7,28,70,2]

    compareobj = compare(list1)

    odd , even = compareobj.odd_even_count()

    print(f"odd count :{odd}\neven count:{even}")