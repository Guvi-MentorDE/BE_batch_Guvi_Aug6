'''
4) 
dict1 = {"INDIA": "INR", "US": "USD"}
dict2 = {"INDIA": "INR", "UK": "GBP", "JAPAN": "YEN"}

write a logic to compare dict1 and dict2, create a new dict3 with only common keys
dict3 = {"INDIA": "INR"}
'''
#Base class
class dictionary():
    #intersection method for two dictionaries
    def intersection(self, d1, d2):
        dict3 = {}
        for i, j in d1.items():
            for x, y in d2.items():
                if(i==x):
                    dict3[i] = j
        return(f"Intersection of {d1} & {d2} is {dict3}")

#Child class
class dictionary_subclass(dictionary):
    #Constructor with optional parameters
    def __init__(self, no=None, d1=None, d2=None):
        self.no = no
        self.d1 = d1
        self.d2 = d2
    
    #Get elements for the dictionary
    def get_ele_method(self, no):
        dict1 = {}
        for i in range(no):
            key = input(f"{i} Enter a country name: ")
            value = input(f"{i} Enter the currency being used by {key}: ")
            dict1[key] = value
        return dict1

#Main
if __name__ == '__main__':
    #try - block
    try:
        #Create an object for the child class
        dic1 = dictionary_subclass(int(input("Enter no. of items in dictionary 1: ")))
        #Call the method in child class
        d1 = dic1.get_ele_method(dic1.no)
        print(d1)
        #Create another object for the child class
        dic2 = dictionary_subclass(int(input("Enter no. of items in dictionary 2: ")))
        #Call the method in child class
        d2 = dic2.get_ele_method(dic2.no)
        print(d2)
        #Create another object for the child class
        d3 = dictionary_subclass(d1, d2)
        #Call the method in base class
        print(d3.intersection(d1, d2))
    #except - block
    except ValueError as ve:
        print("Kindly the number: ", ve)
    except Exception as e:
        print("Raise of an exception: ", e)
    #finally - block
    finally:
        print("Thank you!")