class st:

    def __init__(self,strinput):
        self.strinput=strinput

    def ispalindrome(self):
        length = len(self.strinput)   
        for i in range(0,length//2):
            if self.strinput[i] != self.strinput[length-1-i]:
                return False
        return True    

if __name__=="__main__":

    getstring=str(input())
    check = st(getstring)
    if check.ispalindrome():
        print("Yes Palindrome")
    else:
        print("Not a Palindrome")    