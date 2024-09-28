'''
Author: Ankitha Desai
Date Created:: 19-08-2023
Description: This file contains the code for Occurance of strings, lists and tuples.
'''
'''
how to find if there is mutiple occurnce of same value in list/sting/tuple. 

'''

class Occurrence:
    def __init__(self, data):
        self.data = data
        self.element_count = self._count_occurrences()

    def _count_occurrences(self):
        element_count = {}

        for _, element in enumerate(self.data):
            if element in element_count:
                element_count[element] += 1
            else:
                element_count[element] = 1

        return element_count

    def has_multiple_occurrences(self):
        return any(count > 1 for count in self.element_count.values())

if __name__ == "__main__":
    list_data = [1, 2, 3, 2, 4, 5, 4]
    string_data = "hello"
    tuple_data = (1, 2, 3, 2, 4, 5, 4)

    list_checker = Occurrence(list_data)
    string_checker = Occurrence(string_data)
    tuple_checker = Occurrence(tuple_data)

    print(list_checker.has_multiple_occurrences())   
    print(string_checker.has_multiple_occurrences()) 
    print(tuple_checker.has_multiple_occurrences())  
