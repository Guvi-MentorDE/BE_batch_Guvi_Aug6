"""
  Assignment : Week 3 - Q2 - Index of a number
  Author  :   Kannan Kandasamy
  Course  :   ML Guvi - Python
  Date    :   15/08/2023
  Details :   Getting an index position of a number using looping
"""
class Numbers:
  def __init__(self, n=0):
    self.num = n

  def get_index(self, lis, n):
    op = next((i for i,val in enumerate(lis) if val==n),-1)
    return op

  def get_index_manual(self, lis):
    for i in enumerate(lis):
      if i[1]==self.num:
        return i[0]
        break
    return -1


if __name__=="__main__":
  try:
    ip = list(map(int,input("Enter list of numbers in space separated : ").split()))
    n = int(input("Enter number to find : "))
    num_obj = Numbers()
    op = num_obj.get_index(ip,n)
    print("Not found" if op==-1 else "Found at "+str(op))    
  except:
    print("Enter valid numbers")