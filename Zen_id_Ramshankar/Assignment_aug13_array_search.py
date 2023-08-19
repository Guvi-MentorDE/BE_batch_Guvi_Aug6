import math

class Array_search:
    def  __init__(self,arr):
        self.arr=arr
    
    def search(self):
        count=1
        flag=0
        for i in self.arr:
            if(i==5):
                print("We found the number 5 in position",count,"of the input")
                flag=1
            count=count+1
        if(flag==0):
            print("There are no occurrences of number 5 in the input")



if __name__=="__main__":
    print("Enter input of numbers seperated by comma:")
    input_elements=list(map(int,input().split(',')))
    array_obj=Array_search(input_elements)
    array_obj.search()
    
    