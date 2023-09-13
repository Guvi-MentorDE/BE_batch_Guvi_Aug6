'''
Q2) 
1. Get an input from user for an array as int
2. make sure you have '5'
3. write a logic to search the array for '5' and print its index position
hint: looping, don't use .index()
'''

#Class
class search_class:
    #Constructor
    def __init__(self, num_list, search_elemt):
        self.num_list = num_list
        self.search_elemt = search_elemt

    #Is the element available in list
    def is_elemt_in_list(self, num_list, search_elemt):
        return True if self.search_elemt in num_list else False

    #Search the element in the list
    def search_method(self, num_list, search_elemt):
        for i in range(len(self.num_list)):
            if(self.num_list[i] == self.search_elemt):
                yield f"Index of {self.search_elemt} in {self.num_list} is {i}"

#Main
if __name__ == '__main__':
    #try - block
    try:
        no = list(map(int, input("Enter the numbers to the list: ").strip().split()))
        search = int(input("Enter the number for search: "))
        #Object - created for the class
        search1 = search_class(no, search)
        #If element exists checked by calling is_elemt_in_list() using object
        if(search1.is_elemt_in_list(no, search)):
            #Calling search_method() using object
            for i in search1.search_method(no, search):
                print(i)
        #If no such element exists in the list
        else:
            print(f"No such element {search} in the list {no}")
    #except - block
    #Value error exception
    except ValueError as ve:
        print("Enter the number: ", ve)
    #Other exception
    except Exception as e:
        print("Raise of an exception: ", e)
    #finally - block
    finally:
        print("Thank you!")
