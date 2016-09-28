#!/usr/bin/env python
import re
import sys


top3temp =[]
#for line in sys.stdin:
for line in sys.stdin:
    temp = line.strip().split("\t")[1]
    top3temp.append(int(temp))

for cnt in xrange(3):
    print "%s" %(top3temp[cnt])




