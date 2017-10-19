f = open("datasetB.data","rb")

customer_dict = dict()
item_dict = []
for transation in f:
	cid = int(transation.split("\t")[1])
	item = transation.split("\t")[2]
	item = item.strip("\r\n")
	item_num = int(item)
	if item_num not in item_dict:
		item_dict.append(item_num)

	if cid not in customer_dict.keys():
		customer_dict[cid] = []
		customer_dict[cid].append(item)
	else:
		customer_dict[cid].append(item)


f.close()


f = open("customerB_CSV.txt","wb")

item_dict = sorted(item_dict)
index = 0 
for i in item_dict:
	if index == 0 :
		f.write(str(i))
	else:
		f.write(","+str(i))
	index = index +1
f.write("\n")


for cid in sorted(customer_dict.keys()):
	index = 0
	for item_title in item_dict:
		if index == 0:
			if str(item_title) in customer_dict[cid]:
				f.write(str("T"))
			else:
				f.write("")
		else:
			if str(item_title) in customer_dict[cid]:
				f.write(","+str("T"))
			else:
				f.write(",")
		index = index +1
	f.write("\n")
	

