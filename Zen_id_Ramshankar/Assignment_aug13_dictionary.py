import math

if __name__=="__main__":
    dict1 ={"INDIA":"INR","US":"USD"}
    dict2 ={"INDIA":"INR","UK":"GBP","JAPAN":"YEN"}
    dict_common={}
    for key1,val1 in dict1.items():
        for key2,val2 in dict2.items():
            if(key1==key2):
                dict_common[key1]=val1
    print("The common keys between both the dictionary values",dict_common)