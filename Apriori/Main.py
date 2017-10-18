
from itertools import chain, combinations

Inputfilename = "datasetA.data"
OutputFileName = "output2.txt"
min_support = 2
Round_Number = 3


def data_from_csv(filename=Inputfilename,output = OutputFileName):
    f = open(filename, 'r')
    o = open(OutputFileName, "w")
    Data_list = []
    start = "1"
    for line in f:
        row = line.strip().split('\t')
        if row[0] != start:   
            for item in Data_list:
                item = item+" "
                o.write(item)
            o.write("\n")
            Data_list = []
            Data_list.append(row[2])
            start = row[0]
           
        else:
            Data_list.append(row[2])

def itemset_from_data(data):
    i = 0
    itemset = set()
    transaction_list = list()
    for row in data:
        # print (row)
        row = list(row.strip().split(' '))
        # print (row)

        transaction_list.append(frozenset(row))
        for item in row:
            if item:
                itemset.add(frozenset([item]))
        i+=1
        
    return itemset, transaction_list

def apriori(data, min_support=min_support):
    itemset , transaction_list= itemset_from_data(data)

    # Pipeline
    # Plus one element(second round)-> Scan all the file - > pop from dict

    item_dict = Scan_all_the_file(itemset, transaction_list)
    item_dict, trash_dict = Pop_from_dict(item_dict)
    item_dict = [set(x) for x in item_dict]
    trash_dict = [set(x) for x in trash_dict]
    print("1 Round........ ")
    print("Item set higher than min support : ",item_dict)
    print("Trash loew than min support : ",trash_dict)

    #start second round 
    for i in range(1,Round_Number):
        print()
        print(i+1,"Round........")
        itemset = PlusOne_try(item_dict, trash_dict)
        print("Original Itemset : ",itemset)
        xx = Scan_all_the_file(itemset, transaction_list)
        item_dict, trash_dict = Pop_from_dict(xx)
        # print (trash_dict)
        print("After delete pairs which number lower than min support : ", item_dict)



# Pop element that lower than min_support
def Pop_from_dict(item_dict):
    # Input type -> dict
    # Output type -> dict
    xx = []
    yy = []
    temp_dict = {}
    trash_dict = {}
    for i in item_dict:
        # print(item_dict[i])
        if item_dict[i] >=  min_support:
            xx.append(i)
        else:
            yy.append(i)
    for i in xx:
        temp_dict[i]  = item_dict[i]
    for i in yy:
        trash_dict[i] = item_dict[i]

    return temp_dict,trash_dict

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


def Scan_all_the_file(itemset, transaction_list):
    item_dict = {}
    # print("xx",itemset)
    print()
    for i in transaction_list:
        for j in itemset:
            # print (j)
            j = frozenset(j)
            if  j.issubset(i):
                # print("check")
                if j not in item_dict:
                    item_dict[j] = 1
                    # print("check")
                else :
                    item_dict[j] +=1
        
    return item_dict




if __name__ == "__main__":

    
    f = open(OutputFileName,'r',newline= None)
    apriori(f)
   
  
    


