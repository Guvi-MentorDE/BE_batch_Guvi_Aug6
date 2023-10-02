'''
Q2
objective : find if below two strings annagrams or not 
            str1 = "save"
            str2 = "vase"
'''

if __name__=="__main__":

#program to find anagram   

    #input here  
    str1 = "save"
    str2 = "vase"

    c1 = [0]*256
    c2 = [0]*256

    for i in str1:
        c1[ord(i)] += 1 
    for i in str2:
        c2[ord(i)] += 1 
    
    if c1==c2:
        print("yes anagram")
    else:
        print("Not an anagram")   
