#import <>  
 
 
def create_file(filename):
    with open(filename, 'w') as f:
        f.write('Hello, world!\n')
    print("File " + filename + " created successfully.")
   
        
if __name__ == "__main__":
    create_file("sample.txt")