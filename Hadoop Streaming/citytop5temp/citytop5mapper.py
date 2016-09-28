#!/usr/bin/env python
import re
import sys

top5temp = []

#for line in sys.stdin:
for line in sys.stdin:
    val = line.strip()
    splits = val.split(",")
    temp = splits[1]
    top5temp.append(int(temp))

top5temp.sort(reverse=True)

for  cnt in xrange(3):
    print"%s\t%s" %("0",top5temp[cnt])

