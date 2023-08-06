#enumerate(iterable, start=0)

# enumerate function in loops
l1 = ["eat", "sleep", "repeat"]
  
# printing the tuples in object directly
for ele in enumerate(l1):
    print (ele)
  
# changing index and printing separately
for count, ele in enumerate(l1, 100):
    print (count, ele)