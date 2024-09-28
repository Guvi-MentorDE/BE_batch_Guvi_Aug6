#import

class search:
    lst=[]
    def __init__(self,lst,number):
        self.lst=lst
        self.number=number
    def search_number(self,lst,number):
        number=5
        for i in range(0,len(self.lst)):
            if(number==self.lst[i]):
                print(f"The number {self.lst[i]} is searched and its index position is {i}")
                return lst[i]
            
            
if __name__ == "__main__":
    lst=[]
    numbers=int(input("Enter no.of numbers\n"))
    for i in range(0,numbers):
        num=int(input())
        lst.append(num)
    print("Entered numbers are",lst)
    searc=search(lst,num)
    if searc.search_number(lst,num):
        print("Number found")
    else:
        print("No element found")
        