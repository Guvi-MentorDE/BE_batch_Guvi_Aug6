
class dict:

    def __init__(self,dict1={},dict2={}):
        self.dict1 = dict1
        self.dict2 = dict2
    
    def compare_dictionary(self,dict1={},dict2={}):
        set1=set(dict1.keys())
        set2=set(dict2.keys())
        intersection_set=set1.intersection(set2)
        dict3 = {k: dict1[k] for k in intersection_set}
        print("Common key value of dictionary1 and dictionary2 are")
        return dict3

if __name__ == "__main__":
    dict1={}
    dict2={}
    number=int(input("Enter no of key pair values for dictionary1\n"))
    for i in range(number):
        key=input("Enter key: ")
        value=input("Enter the value: ")
        dict1.update({key:value})
    print("Dictionary 1 values are")
    print(dict1)
    number2=int(input("Enter no of key pair values for dictionary2\n"))
    for i in range(number2):
        key=input("Enter key: ")
        value=input("Enter the value: ")
        dict2.update({key:value})
    print("Dictionary 2 values are")
    print(dict2)
    dictionary=dict()
    dict3=dictionary.compare_dictionary(dict1,dict2)
    print(dict3)