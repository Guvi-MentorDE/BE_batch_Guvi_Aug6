class calculator :
    #Special methods to initialize paramters
   def __init__(self,num1,num2):
       self.num1 = num1
       self.num2 = num2

   # Class methods
   def addition(self):
       ''' This method will add two number'''
       try:
          result = self.num1 + self.num2
          return result
       except ValueError:
           print('Addition allowed only for numbers.')

   def subtraction(self):
       ''' This method will subtract for the given number'''
       try:
          result = self.num1 - self.num2
          return result
       except ValueError:
           print('Subtraction allowed only using numeric values. ')

   def division(self):
       ''' This method will do division of two number '''
       try:
          result = self.num1 / self.num2
          return round(result,2)
       except ZeroDivisionError:
            print('Can not dive by zero. ')

   def multiplication(self):
       ''' This method will do Multiplication of two number '''
       try:
           result = self.num1 * self.num2
           return round(result,2)
       except ZeroDivisionError:
           print('Multiplication allowed only using numeric values. ')

if __name__ == '__main__':
       # Creating object for the class calculator
    try:
       ask_again = True
       while ask_again:
           print('\n---------Arithmetic calculation--------------')
           n1 = int(input('\nPlease enter first number :'))
           n2 = int(input('Please enter second number :'))
           cal = calculator(n1,n2)
           print('\nPlease select your option:')
           print('     1. Addition')
           print('     2. Subtraction')
           print('     3. Division')
           print('     4. Multiplication')
           n3 = int(input(' \nYour Option :'))
           if n3 == 1 :
               add_res = cal.addition()
               print(f'\nAddition of two number is {add_res}')
           elif n3 == 2:
               sub_res = cal.subtraction()
               print(f'\nSubtraction of two number is {sub_res}')
           elif n3 == 3:
               div_res = cal.division()
               print(f'\nDivision of two number is {div_res}')
           elif n3 == 4:
               mul_res = cal.multiplication()
               print(f'\nMultiplication of two number is {mul_res}')
           else:
               print('Please select the correct option [1,2,3,4]')
           con_yn = input('Do you want to continue say (Y/N)?:')
           if con_yn.lower() == 'y':
               ask_again = True
           else:
               ask_again = False

    except(ValueError):
             print('Please provide only numeric inputs.')
    check = True
    while check :
        str2 = input('\nPlease enter a word to check it is palindrome or not:')
        obj1 = Palindrome(str2)
        result = obj1.check_palindrome()
        print(f'Given string is {result}')
        choice = input('Do you like to try with another word (Y/N):?')
        if choice.lower() == 'y':
            check = True
        else:
            check = False
