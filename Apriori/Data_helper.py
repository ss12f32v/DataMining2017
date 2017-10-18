



class Loader(object):

    def __init__(self, datapath):
        self.datapath = datapath

    def data_from_csv(self ,filename ,output):
        f = open(self.datapath, 'r')
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