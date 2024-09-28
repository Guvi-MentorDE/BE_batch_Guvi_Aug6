#Class
class my_class:
  #Constructor
  def __init__(self, str):
    self.str = str

  #Palindrome method
  def check_palindrome(self):
        if self.str == self.str[::-1]:
                return "the given string is palindrome"
        else:
                return "The given string is not palindrome"

#Main
if __name__ == '__main__':
  string = input("Enter a string: ")
  palin = my_class(string)
  print(palin.check_palindrome())
