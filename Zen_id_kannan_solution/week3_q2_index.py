"""
  Assignment : Week 3 - Q2 - Index of a number
  Author  :   Kannan Kandasamy
  Course  :   ML Guvi - Python
  Date    :   15/08/2023
  Details :   Getting an index position of a number using looping
"""
class Numbers:
  def __init__(self, n):
    self.num = n

  def get_index(self, lis, n):
    for i in enumerate(lis):
      if i[1]==n:
        return i[0]
        break
    return -1

  def get_index(self, lis):
    for i in enumerate(lis):
      if i[1]==self.num:
        return i[0]
        break
    return -1


if __name__=="__main__":
  try:
    ip = list(map(int,input("Enter list of numbers in space separated : ").split()))
    n = int(input("Enter number to find : "))
    num_obj = Numbers(n)
    op = num_obj.get_index(ip)
    print("Not found" if op==-1 else "Found at "+str(op))    
  except:
    print("Enter valid numbers")