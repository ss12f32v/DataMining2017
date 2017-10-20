
input_file ="Data/datasetB.data"

class Loader(object):

    def __init__(self, datapath):
        self.datapath = datapath

    def data_from_csv(self):
        f = open(input_file, 'r')
        o = open(self.datapath, "w")
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


    # For Hash
    def itemset_from_data(self):
        data = open(self.datapath,'r',newline= None)
        i = 0
        itemset = set()
        transaction_list = list()
        for row in data:
            row = list(row.strip().split(' '))

            transaction_list.append(frozenset(row))
            for item in row:
                if item:
                    itemset.add(frozenset([item]))
            i+=1
            
        return itemset, transaction_list
    # For FP-growth
    def transaction_for_FP(self):
        data = open(self.datapath,'r',newline= None)
        OutputList = []
        for row in data:
            row = row.strip().split(' ')
            OutputList.append(row)
        return (OutputList)
          

if __name__ == "__main__":
    load = Loader("Data/output2.txt")
    print(load.transaction_for_FP())

