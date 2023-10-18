
# code to check if number is even or odd 

def check(a):
  print(a)
  if(a % 2 == 0):
    print("Given number is even")
  else:
    print("Given number is odd ")
  return a 

if __name__ == "__main__":

   
  try:
    b = int(input())
    flag = True 
    res1 = check(b)
    int(b)
    #print("great ")
  except ValueError:
      flag = False

      if flag :
        print("Entered value is integer")
      else:
        print("Entered value is not integer: ")
