'''
Q3)
1. Reverse a string without using any inbuilt function
hint: looping
'''

#Class
class reverse_string_class:
    #Constructor
    def __init__(self, string_ele):
        self.string_ele = string_ele
    
    #Reverse a string method
    def reverse_string_method(self, string_ele):
        reversed = ''
        for ele in self.string_ele:
            reversed = ele+reversed
        return f"Reversed string of {self.string_ele} is {reversed}"

#Main
if __name__ == '__main__':
    #try - block
    try:
        string = input("Enter a string: ")
        #Create an object for the class
        str1 = reverse_string_class(string)
        #Call reverse a string method
        print(str1.reverse_string_method(string))
    #except - block
    except Exception as e:
        print(e)
    #finally - block
    finally:
        print("Thank you!")