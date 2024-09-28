#QUESTION
#1. how to find if there is mutiple occurnce of same value in list/sting/tuple.
#l1 = ["eat", "sleep", "repeat" , "eat"]
#    solve: using "enumerate" concept. 
#    solve: using looping concept. (for/while)
#l1.index("eat") = 0,3 --> output

#SOLUTION
# Find if there is multiple occurance
l1 = ["eat", "sleep", "repeat" , "eat"] #list
choice = int(input())
match choice:
    case 1:
        #Display using enum
        print("Display using enum:")
        a=[i for i, val in enumerate(l1) if val == "eat"]
        print(a)
    case 2:
        #Display using for loop
        print("Display using for loop:")
        l2=len(l1)
        for val in range(l2):
            if(l1[val] == "eat"):
                print(val)