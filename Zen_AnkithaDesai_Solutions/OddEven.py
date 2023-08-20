class OddorEven:
    def __init__(self, n):
        self.n = int(n)
    
    def check_oddEven(self):
        if (self.n % 2 ==0 ):
            print("Number is Even")
        else:
            print ("Number is odd ")

if __name__ == "__main__":
    num=int(input())
    result = OddorEven(num)
    result.check_oddEven()