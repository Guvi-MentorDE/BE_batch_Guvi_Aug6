



class Odd_or_Even:
    def odd_or_even(self,n):
        if(n%2==0):
            print(n," is a even number")
        else:
            print(n," is a odd number")


if __name__=="__main__":
    obj=Odd_or_Even()
    ip_num=int(input("Enter a number to find whether odd or even? "))
    obj.odd_or_even(ip_num)
