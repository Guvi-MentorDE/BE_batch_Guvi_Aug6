'''1. create a function for detmining palidrome , anagram and retun the result to the function call then print.'''

def check_palindrome(a_word):
  return(f"{a_word} is palindrome" if(a_word == a_word[::-1]) else f"{a_word} is not a palindrome")

def check_anagram(word1, word2):
  check = [word2[i] in word1 for i in range(len(word2))]
  return(f"{word1} & {word2} is anagram" if(len(set(check)) == 1) else f"{word1} & {word2} is not an anagram")

if __name__ == '__main__':
  try:
    print("To check palindrome")
    string = input("Enter a string: ")
    print(check_palindrome(string))
    print("----------------------------------------------------------------------------------------------")
    print("To check anagram")
    str1 = input("Enter a first word: ")
    str2 = input("Enter a second word to compare: ")
    print(check_anagram(str1, str2))
  except e:
    print(e)
  finally:
    print("Thank you!")