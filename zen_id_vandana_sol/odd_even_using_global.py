"""its working in collab ---------------------------Querry
"""
class NUM:
    x=[int(i) for i in input("enter string of numbers").split(",")]
    
    def __init__(self):
        self.even_num=[]
        self.odd_num=[]
    def even(self):
        for i in range(len(self.x)):
            if self.x[i]%2==0:
                self.even_num.append(self.x[i])
        return self.even_num
    def odd(self):
        for i in range(len(self.x)):
            if self.x[i]%2!=0:
                self.odd_num.append(self.x[i])
        return self.odd_num
if __name__=="__main__":
    object1=NUM()
    print(object1.even())
    print(object1.odd())
