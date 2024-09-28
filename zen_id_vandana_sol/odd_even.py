"""
Question 3 :impliment the logic : odd_or_even and modify the code for the above logic thats fits into class and objects. 
"""
class NUM:
    def __init__(self):
        self.even_num=[]
        self.odd_num=[]
    def even(self):
        for i in range(len(x)):
            if x[i]%2==0:
                self.even_num.append(x[i])
        return self.even_num
    def odd(self):
        for i in range(len(x)):
            if x[i]%2!=0:
                self.odd_num.append(x[i])
        return self.odd_num
if __name__=="__main__":
    x=[int(i) for i in input("enter string of numbers").split(",")]
    object1=NUM()
    print(object1.even())
    print(object1.odd())