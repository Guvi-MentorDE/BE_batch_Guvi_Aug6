#python Strings:
#Description: Python string is the collection of the characters surrounded by quotes

#creating a string:
strx = 'creating a string'
print(strx)

print("Welcome to Python to Session")
print('Hello')

line = '''Welcome to Python Session 
python learning for
excellence'''
    
print(line)  

#python string index 
example='hello world'
print(example.index('h'))

# mutilple 'h' use case 

print(example[0])
print(example[1])
print(example[3])

#py interpreter  -> memory created for vaiable  
#hello world and hi how are you 
#012345678910         ........45         


#finding a length of a string variable 
print(len(example))

#python
#012345
x='python'
print(x[6])
#error: index out of range


#slicing
print('slicing')

print('index vs length')
#hello world
#012345678910      <- index 

#hello - > length is 5
#world  -> length is 5
#hello world -> lenth is 11 

example='hello world'
'ello'

example[1:5]    


#>>> print(example[:])
#hello world
#>>> print(example)
#hello world
#>>> print(example[0:])
#hello world


# varaible[starting position or index : length]

print(example[1:4])

print(example[:])

print(example[0:])

print(example[:-1])

print(example.index('l'))

#misc
str1='python'
print(str1*3)

#string concatination 
str2='learning'
print(str1+str2)
print(str1+''+str2)

#searching -> returns True/false 
print('i' in str1)
      
print('wo' not in str1) 

#Format:
print("value of  {0} +  {1} is =".format(1,2))

print("This is of {0} and {1} print format behaviour ".format("position0","position1"))  

print(str1.upper())

print(str1.lower())

print(len(str1))


#String reversal 

print(example[::-1])


#partition

inp = "python is a programming language"

print(inp.partition("a"))

#join
temp = '-'.join('python')
print(temp)

list1 = ['p', 'y', 't', 'h', 'o', 'n']
print("".join(list1))


#replace

temp = "Have a great day"

new_string = temp.replace("great", "good")


#rfind

result = temp.rfind('a')

#lfind

