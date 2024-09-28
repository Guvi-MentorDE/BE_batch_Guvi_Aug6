#QUESTION
#dict1 ={"INDIA":"INR","US":"USD"}
#dict2 ={"INDIA":"INR","UK":"GBP","JAPAN":"YEN"}

#write a logic to compare dict1 and dict2 , create a new dict3 with only commen keys.

#RESULT:
#dict3={"INDIA":"INR"}

class common:
    def __init__(self,dict3,dict4):
        self.dict3 = dict3
        self.dict4 = dict4

    def check(self):
        common={}
        for key1,val1 in dict1.items():
            for key2,val2 in dict2.items():
                if(key1 == key2):
                    common[key1]=val1
        return common

if __name__== "__main__":
    dict1 = {"INDIA":"INR","US":"USD"}
    dict2 = {"INDIA":"INR","UK":"GBP","JAPAN":"YEN"}
    obj=common(dict1,dict2)
    print("The common keys and values from both the dictionaries",obj.check())