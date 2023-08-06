
class Calculator:
  
  def __init__(self, lst1):
        self.lst1 = lst1                  

  
  def odd_or_even(self):
    count_odd=0
    count_even=0
    itr=0
    while itr < len(self.lst1):
      if self.lst1[itr] % 2 ==0:
        count_even +=1
      else:
        count_odd = count_odd + 1
      itr +=1 
    return count_even, count_odd 
    #print(count_even, count_odd)

  def odd_or_even_using_for(self):
    count_odd=0
    count_even=0
    for itr in self.lst1:
      if itr % 2 ==0:
        count_even +=1
      else:
        count_odd = count_odd + 1
    return count_even, count_odd 
    #print(count_even, count_odd)
    
if __name__ == "__main__":
  list1=[1,3,6,7,10,12,34,13,99,101,310,399,101]
  obj1 = Calculator(list1)
  count_even, count_odd=obj1.odd_or_even()
  print("from while loop result :",count_even, count_odd)
  
  count_even1, count_odd1 =obj1.odd_or_even_using_for()
  print("from for loop result :",count_even, count_odd)