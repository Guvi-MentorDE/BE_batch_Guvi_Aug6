class loop:
  def __init__(self):
    pass

class ind(loop):
  def check_index(self , inp):
    b = len(inp)
    #print(b)
    for i in range(1 , 6):
      print([i])

if __name__=="__main__":
  inp = input("enter a 5 digit number : ")
  inp= list(map(int,inp))
  check = ind()
  check.check_index(inp)