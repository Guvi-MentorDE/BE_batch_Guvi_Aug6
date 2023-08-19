
# (a) When strings are to be given

def check(s1, s2):
   
    if(sorted(s1)== sorted(s2)):
        print("The strings ARE anagrams.")
    else:
        print("The strings ARE NOT anagrams.")        
         
s1 =input("Enter string 1: ")
s2 =input("Enter string 2: ")
check(s1, s2)


# (b) When strings are given

def check(s1, s2):
     
    if(sorted(s1)== sorted(s2)):
        print("The strings ARE anagrams.")
    else:
        print("The strings ARE NOT anagrams.")        
         
s1 ="save"
s2 ="vase"
check(s1, s2)


# (c) Without using sorted function

s1="save"
s2="vase"
s1_set=set(s1)
s2_set=set(s2)
if s1_set==s2_set:
    print("The strings ARE anagrams.")
else:
    print("The strings ARE NOT anagrams.")
