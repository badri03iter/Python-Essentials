dataset = [(1,2),(2,3),(3,4),(4,5)]
print dataset
tot_count = 0
for element in dataset:
    item,count = element[0],element[1]
    tot_count += element[1]
    print item,count,tot_count

