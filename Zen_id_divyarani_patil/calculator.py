# Q2) 1. create a class called calculator 
#2. accept 2 input from user and pass it to class 
   #3.a create a constructor (init method )
#3. objects has to be add , sub , mu;l , div
#4. creat sepeate methods to do above object related operations 
#5.complete the logic within add , sub , mul , div return 
class calculator:

    def __init__(Self):
      pass
    def add(Self,input1 , input2):
      c = input1 + input2
      print(c)

    def sub(Self,input1 , input2):
        c = input1 - input2
        print(c)

    def mul(Self,input1 , input2):
        c = input1 * input2
        print(c)
    def div(Self,input1 , input2):
        d = input1 / input2
        print(d)
if __name__=="__main__":

  (input1,input2) = map(int,input().split())
  s2 = calculator()
  s2.add(input1,input2)
  s2.sub(input1,input2)
  s2.mul(input1,input2)
  s2.div(input1,input2)
    