
# (a) When strings are to be given

def check(s1, s2):
     
    
    if(sorted(s1)== sorted(s2)):
        print("The strings are anagrams.")
    else:
        print("The strings aren't anagrams.")        
         
s1 =input("Enter string 1: ")
s2 =input("Enter string 2: ")
check(s1, s2)

# (b) When strings are given

def check(s1, s2):
     
    
    if(sorted(s1)== sorted(s2)):
        print("The strings are anagrams.")
    else:
        print("The strings aren't anagrams.")        
         
s1 ="save"
s2 ="vase"
check(s1, s2)