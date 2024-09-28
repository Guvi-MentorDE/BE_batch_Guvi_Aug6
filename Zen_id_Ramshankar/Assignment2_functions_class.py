def odd_or_even(arg1):
    if(arg1%2==0):
        print("It is an even number")
    else:
        print("It is an odd number")

if __name__=="__main__":
    print("Enter an integer:")
    inp=int(input())
    odd_or_even(inp)
