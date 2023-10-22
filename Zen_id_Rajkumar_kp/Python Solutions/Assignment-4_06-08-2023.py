#QUESTION:
#2. Create a function to accept one variable , which will return weather it is odd or even number. 
#    2.(a) check if the accpeted input is interger or not , if not then throw exception.

#SOLUTION:
#Check given integer is odd or even by using function
def odd_or_even(Number):
    return Number%2 == 0

if __name__ == "__main__":
    try:
        Number = int(input())
        result = odd_or_even(Number)
        if result:
            print("The given integer is even")
        else:
            print("The given integer is odd")

    except(ValueError):
        print("You must enter integer value!")