


from itertools import chain, combinations

Inputfilename = "datasetA.data"
OutputFileName = "output1.txt"
min_support = 0.25



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
        print (row)
        row = list(row.strip().split(' '))
        print (row)

        transaction_list.append(frozenset(row))
        for item in row:
            if item:
                itemset.add(frozenset([item]))
        i+=1
        if i ==2:        
            break
    return itemset, transaction_list

def apriori(data, min_support=min_support):
    itemset , transaction_list= itemset_from_data(data)
    print (itemset)




if __name__ == "__main__":

    # data_from_csv()
    f = open(OutputFileName,'r',newline= None)
    apriori(f)
    root = Root()
    inter = interior()
    root.left = inter
    inter.Father = root
    print(root.left)
    print(inter.Father.hash)
    print(ord("C"))