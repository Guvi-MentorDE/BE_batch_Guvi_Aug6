file = open('sample.txt', 'r')
 
# This will print every line one by one in the file
for each in file:
    print (each)
    
#read mode , option 2
with open("sample.txt") as file: 
    data = file.read()
 
print(data)


#read certain no of characters:
file = open("sample.txt", "r")
print (file.read(5))




with open("python_tuple.txt", "r") as file:
    data = file.readlines()
    for line in data:
        word = line.split()
        print (word)
        
#write_mode:
    
    
file = open('python_tuple.txt','w')
file.write("new line")
file.close()