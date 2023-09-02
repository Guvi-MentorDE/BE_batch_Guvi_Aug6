#QUESTION
#1. get an input from user for an array as int  
#2. make sure you have '5'
#3. write a logic to seach the array for '5' and print its index position. 
#hint : looping , dont use .index()

#import , class (methods , instance variables) , main , object

class numbers:
    def find_number():
        number = [int(item) for item in input().split()]
        if 5 in number:
            for item in range(len(number)):
                if(number[item] == 5):
                    print("Index of number '5' is: ", item)
        else:
            print("Number can't find.")

if __name__ == "__main__":
    n1 = numbers
    n1.find_number()