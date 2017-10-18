


from itertools import chain, combinations

Inputfilename = "datasetA.data"
OutputFileName = "output1.txt"
min_support = 5



class Root(object):
    def __init__(self):
        self.left = None
        self.Middle = None 
        self.hash = 1 
class interior(object):
    def __init__(self):
        self.Father = None

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
    # print (itemset)


    item_dict = Make_dict(itemset,transaction_list)
    print(item_dict)
    item_dict, _ = Pop_from_dict(item_dict)

    #start second round 
    print("cccc",item_dict)
    itemset = NumberInSetPlusOne(item_dict)
    print("itemset",itemset)
    xx = Scan_all_the_file(itemset, transaction_list)
    # item_dict = Make_dict(itemset,transaction_list)
    item_dict, trash_dict = Pop_from_dict(xx)
    # print()
    # print("item_dict",item_dict)
    # print()
    # print ("trash dict",trash_dict)


    # Start third round
    # itemset = NumberInSetPlusOne(item_dict)
    print(item_dict)
    itemset = PlusOne_try(item_dict)
    print(itemset)

def Make_dict(Item_set,transaction_list):
    item_dict = {}
    for i in transaction_list:
        for element in i:
            if element not in item_dict:
                item_dict[element]= 1 
            else : 
                item_dict[element]+=1
    return item_dict

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
    # print(xx)
    for i in xx:
        temp_dict[i]  = item_dict[i]
    for i in yy:
        trash_dict[i] = item_dict[i]

    return temp_dict,trash_dict
def NumberInSetPlusOne(item_dict):
    #Input -> dict
    #output  ->list
    list_temp = []
    xxxx=[]
    yyyy=[]
    keys = list(item_dict.keys())
    temp_item_list = list(item_dict)
    # print(len(item_dict))
    for i in range(len(item_dict)):
        for j in range(i+1,len(item_dict)):
            # print(i,keys[i] )
            # print(j ,keys[j])
            xxxx.append(keys[i])
            yyyy.append(keys[j])
            # print((xxxx))
            # print((yyyy))
            a = set(xxxx)|set(yyyy)          
            list_temp.append(set(xxxx)|set(yyyy))
            xxxx[:] = []
            yyyy[:] = []
        
    return list_temp
def PlusOne_try(item_dict):
    temp_list = []
    # print(list(item_dict))
    x = list(item_dict)
    for i in range(len(x)):
        for j in range(i+1,len(x)): 
            print("x0 : ",x[0])
            Or_Product = x[0]|x[1]
            # print(Or_Product)
            temp_list.append(Or_Product)
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

    # data_from_csv()
    f = open(OutputFileName,'r',newline= None)
    apriori(f)
    # root = Root()
    # inter = interior()
    # root.left = inter
    # inter.Father = root
  
    


