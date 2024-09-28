import math

class Strng_reverse:
    def __init__(self,inp_str):
        self.str1=inp_str
    
    def reverse(self):
        length=len(self.str1)-1
        rev=[]
        while length>=0:
            rev.append(self.str1[length])
            length=length-1
        print("Reversed string:",''.join(rev))

if __name__=="__main__":
    print("Enter the string to be reversed:")
    string_input=input()
    str_rev_obj=Strng_reverse(string_input)
    str_rev_obj.reverse()
    


