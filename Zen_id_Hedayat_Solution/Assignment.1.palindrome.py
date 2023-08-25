"""
  Assignment 1
  Author  :   Saleh Md Hedayatullah
  Course  :   ML Guvi - Python
  Details :   Palindrome
"""
class String:  
    def __init__(self, word):  
        self.word = word
   
    def palindrome(self):
        return self.word == self.word[::-1]

def main():
    word = input('Enter a word:').lower()
    obj = String(word)
    
    if obj.palindrome():
        print("The word you entered is a Palindrome")
    else:
        print("N0, the word you entered is not a Palindrome")
    
if __name__== "__main__":
    main()