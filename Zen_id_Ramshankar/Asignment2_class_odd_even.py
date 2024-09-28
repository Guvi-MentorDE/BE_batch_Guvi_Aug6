class num_check:
    def odd_or_even(arg1):
        if(arg1%2==0):
            print("It is an even number")
        else:
            print("It is an odd number")

if __name__=="__main__":
    print("Enter a number to check if it is odd or even:")
    inp=int(input())
    n1=num_check
    n1.odd_or_even(inp)

