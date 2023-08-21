#QUESTION
#reverse a string without using any inbuilt functions 
#hint: looping.

#if __name__ == "__main__":
#    string = input("Enter a string: ")
#    print("Before reversal: ", string)
#    string1 = string[::-1]
#    print("After reversal: ", string1)


class reverse:
    def reverse_string(string):
        new_string = ""
        for item in range(len(string)-1,-1,-1):
            new_string += string[item]
        return new_string

if __name__ == "__main__":
    string = input("Enter a string: ")
    print("Before reversal", string)
    s1 = reverse
    print("After reversal", s1.reverse_string(string))