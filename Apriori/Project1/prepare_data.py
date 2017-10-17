f = open("datasetD.data","rb")

customer_dict = dict()

for transation in f:
	cid = int(transation.split("\t")[1])
	item = transation.split("\t")[2]
	if cid not in customer_dict.keys():
		customer_dict[cid] = []
		customer_dict[cid].append(item)
	else:
		customer_dict[cid].append(item)


f.close()

f = open("customerD.txt","wb")
for cid in sorted(customer_dict.keys()):
	for item in customer_dict[cid]:
		f.write(item.strip("\r\n")+" ")
	f.write("\n")
	

