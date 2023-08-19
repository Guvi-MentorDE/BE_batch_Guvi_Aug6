import math

class Dict:
    def __init__(self,dict_inp1,dict_inp2):
        self.dict_inp1=dict_inp1
        self.dict_inp2=dict_inp2

    def intersect(self):
        dict_common={}
        for key1,val1 in dict1.items():
            for key2,val2 in dict2.items():
                if(key1==key2):
                    dict_common[key1]=val1
        return dict_common

if __name__=="__main__":
    dict1 ={"INDIA":"INR","US":"USD"}
    dict2 ={"INDIA":"INR","UK":"GBP","JAPAN":"YEN"}
    dict_obj=Dict(dict1,dict2)
    print("The common keys between both the dictionary values",dict_obj.intersect())