print("Enter a list of array values\n")
inp_str = input()

list_of_values = inp_str.split(',')
value_to_search = 5

# for i, value in enumerate(list_of_values):
#     if int(value) == 5:
#         print(f"{value_to_search} is available in index position: {i}")

counter = 0

for i in list_of_values:
    if int(i) == 5:
        print(f"{value_to_search} is available in index position: {counter}")
    counter+=1