
# create a function to check if the given string is anagram or not
def anagram(str1,str2):
  print(str1)
  print(str2)
  if(sorted(str1) == sorted(str2)):
    print("The string is anagram")
  else:
    print("The string is not anagram")
    return(str1,str2)

if __name__ == "__main__":
  str1 = str(input("Enter a string "))
  str2 = str(input("Enter a string "))
  res = anagram(str1,str2)


  # anagram -------------------------------------
str1 = "save"
str2 = "vase"

# try without sorted 

if (sorted(str1) == sorted(str2)):
    print("string is anagrams")
else:
    print("not an anagrams")
