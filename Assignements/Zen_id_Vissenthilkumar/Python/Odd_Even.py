class Odd_even:
     def __init__(self,num1):
       self.num1 = num1

     def Find_Odd_Even(self):
         if self.num1 % 2 == 0:
             return ('Even')
         else:
             return('Odd')

if __name__ == '__main__':
       # Creating object for the class calculator
    
       ask_again = True
       
       while ask_again:
          num = int(input('Please enter a number to check Odd or Even Number:'))
          oddEven = Odd_even(num)
          print(f'Entered number is :{oddEven.Find_Odd_Even()}')
          ask = input('Do you want to check with any other number (Y/N):')
          if ask.lower() == 'n':
              ask_again = False


