
# (1) Create a function to accept one variable , which will return whether it is odd or even number.

x = int(input("Enter a number "))
if (x % 2) == 0:
 print("%d is an Even Number" %x)
else:
 print("%d is an Odd Number" %x)


 # 1(a) Check if the accpeted input is interger or not , if not then throw exception.

if __name__ == '__main__':
  try:
    get_a_num = int(input("Enter a number: "))
    odd_or_even = lambda x: f"{x} is odd" if(x%2!=0) else f"{x} is even"
    print(odd_or_even(get_a_num))
  except ValueError:
    print("Please enter a number or integer ", ValueError)
  finally:
    print("Thank you!")