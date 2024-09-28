'''
Q1
objective : To find if there is mutiple occurnce of same value in list/sting/tuple
            l1 = ["eat", "sleep", "repeat" , "eat"]
            solve: using "enumerate" concept. 
            solve: using looping concept. (for/while)

'''
if __name__=="__main__":

    l = ["eat", "sleep", "repeat" , "eat"]
    #creating an empty dictionary to store items and their occurance indices
    d = {}
    

    for index,i in enumerate(l):
        #check if the item is present in the dictionary and append the index number
        #into the dictionary with item name as the key if yes
        if i in d:
            d[i].append(index)
        else:
            #initialise a list of index for that item in dictionary if a new item is being added
            d[i] = [index]    

    print(d)       