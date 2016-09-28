import collections

d1 ={}
d = collections.OrderedDict()

defdict = collections.defaultdict(int)

d[1]=1
d[2]= 2
d[3]=3
d[6]=1
d[5]= 2
d[4]=3


d1[1]=1
d1[2]= 2
d1[3]=3
d1[6]=1
d1[5]= 2
d1[4]=3

for i in xrange(5):
    defdict[i] +=1

print defdict
print d
print d1
