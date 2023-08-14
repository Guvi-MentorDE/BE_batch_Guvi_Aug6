def if_even(loc_num):
    if loc_num % 2==0:
        return 'even'
    else:
        return 'odd'

if __name__ == "__main__":

    userinput= input()
    flag= True
    try:
        x= int(userinput)

    except ValueError:
        flag = False

    result = ' '
    if flag:
        result= if_even(x)
    else:
        print("please enter a valid number")
    
    print("The number entered is: " + result)