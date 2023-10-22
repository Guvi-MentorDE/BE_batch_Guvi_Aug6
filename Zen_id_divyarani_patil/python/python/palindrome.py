
#Q1)
#1. accept a string from user 
#2. check if the list is palindrome or not 
#3. create a class and object 
       # 3.a create a constructor 
#4. access the logic of palindrome using object.method()

class palindrome:
    # write function 
    def __init__(self , str1):
        if(str1 == str1[::-1]):
            print("Is a Palindrome")
        else:
            print("Is not a palindrome")

if __name__=="__main__":
    str1 = input("Enter a string")
    s1 = palindrome(str1)



#palindrome -----------------------
str1 = "madam"
str2 = "maths"
#use for loop 
# input in the form of list[]

if(str1 == str1 [::-1]):
    print("palindrome")
else:
    print("not a palindrome")

if(str2 == str2[::-1]):
    print("palindrome")
else:
    print("not a palindrome")

# print the duplicate element's index number -------------
list1 = ["eat" , "sleep" , "repeat" , "eat"]
#for x in list1:
list2 = [i for i in range(len(list1)) if list1[i] == "eat"]
print(list2)





# create a function to check if the given string is palindrome or not 
def check2(str1):
  print(str1)
  if(str1== str1[::-1] ):
    print("The String is Palindrome")
  else:
    print("The string is not palindrome")
  return str1
if __name__ == "__main__":
  str1 = str(input("Enter a string  "))
  res = check2(str1)
