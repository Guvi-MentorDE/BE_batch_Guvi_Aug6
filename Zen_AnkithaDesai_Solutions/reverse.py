'''
Author: Ankitha Desai
Date Created:: 19-08-2023
Description: This file contains the code for reverse a string using looping
'''


'''
Reverse a string without using any inbuilt function
hint: looping
'''

class Reverse:
    def __init__(self, input_string):
        self.input_string = input_string
        self.reversed_string = self.reverse()

    def reverse(self):
        reversed_string = ""
        for char in self.input_string:
            reversed_string = char + reversed_string
        return reversed_string

    def get_reversed_string(self):
        return self.reversed_string

if __name__ == "__main__":
    user_input = input("Enter a string: ")
    reverser = Reverse(user_input)
    reversed_result = reverser.get_reversed_string()
    print("Reversed:", reversed_result)
