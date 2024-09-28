'''
#Q2) 
1. get an input from user for an array as int  
2. make sure you have '5'
3. write a logic to seach the array for '5' and print its index position. 
hint : looping , dont use .index() 
'''


array = list(map(int,input("Enter input: ").split(' ')))

for index,i in enumerate(array):
    if str(i) == '5':
        print(f"Index of 5 is {index}")
        break