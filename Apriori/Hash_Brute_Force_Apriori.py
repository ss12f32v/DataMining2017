import time
from Data.Data_helper import Loader

Inputfilename = "datasetA.data"
OutputFileName = "Data/outputb.txt"
min_support = 20
Round_Number = 3




def apriori(min_support=min_support):
    itemset , transaction_list= load.itemset_from_data()

    # Pipeline
    # Plus one element(second round)-> Scan all the file - > pop from dict

    item_dict = Scan_all_the_file(itemset, transaction_list)
    item_dict, trash_dict = Pop_from_dict(item_dict)
    item_dict = [set(x) for x in item_dict]
    trash_dict = [set(x) for x in trash_dict]
    print("1 Round........ ")
    print("Item set higher than min support : ",len(item_dict))
    print("Trash loew than min support : ",len(trash_dict))

    #start second round 
    for i in range(1,Round_Number):
        print()
        print(i+1,"Round........")
        itemset = PlusOne_try(item_dict, trash_dict)
        print("Original Itemset : ",len(itemset))
        xx = Scan_all_the_file(itemset, transaction_list)
        item_dict, trash_dict = Pop_from_dict(xx)
        print("After delete set which number lower than min support : ", len(item_dict))
        if len(item_dict) == 0:
            return 


# Pop element that lower than min_support
def Pop_from_dict(item_dict):
    # Input type -> dict
    # Output type -> dict
    xx = []
    yy = []
    temp_dict = {}
    trash_dict = {}
    for i in item_dict:
        if item_dict[i] >=  min_support:
            xx.append(i)
        else:
            yy.append(i)
    for i in xx:
        temp_dict[i]  = item_dict[i]
    for i in yy:
        trash_dict[i] = item_dict[i]

    return temp_dict,trash_dict

# Plus the element number in the set 
def PlusOne_try(item_dict,trash_dict,flag = True):
    temp_list = []
    x = list(item_dict)
    y = list(trash_dict)
    if flag:
        for k in range(len(x)):
            for j in range(k+1,len(x)): 
                continue_flag = 0
                Or_Product = x[k] | x[j]

                # Check the new item set including invalid subset or not
                for i in y:
                    if i.issubset(Or_Product):
                        continue_flag = 1
                        break

                if Or_Product not in temp_list and continue_flag == 0:
                    temp_list.append(Or_Product)
        temp_list = [set(x) for x in temp_list]
    else: 
        temp_list = [set(x) for x in temp_list]
    return temp_list

# Count how many times this set is appear in the transaction
def Scan_all_the_file(itemset, transaction_list):
    item_dict = {}
    print()
    for i in transaction_list:
        for j in itemset:
            j = frozenset(j)
            if  j.issubset(i):
                if j not in item_dict:
                    item_dict[j] = 1
                else :
                    item_dict[j] +=1
        
    return item_dict




if __name__ == "__main__":


    # f = open(OutputFileName,'r',newline= None)
    load = Loader(OutputFileName)
    t0 = time.clock()
    apriori()
    print(time.clock() - t0)
