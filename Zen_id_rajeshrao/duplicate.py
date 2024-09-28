
# how to find if there is mutiple occurnce of same value in list/sting/tuple
my_list=('eat','sleep','repeate','eat')
for index,item in enumerate(my_list):
    if item == 'eat':
        print(index)
