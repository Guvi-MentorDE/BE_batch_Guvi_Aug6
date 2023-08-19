l1 = ["eat", "sleep", "repeat" , "eat"]
#
for count, i in enumerate(l1):
    #print(count, i)
    if l1.count(i) > 1:
        print(i, "is available at index position", count)