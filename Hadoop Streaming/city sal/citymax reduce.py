#!/usr/bin/env python
import re
import sys
maxtemp = -sys.maxint
last_key_city = None

for line in sys.stdin:
    val = line.strip()
    (incity,intemp)=val.split("\t")
    if last_key_city and last_key_city != incity :
        print "%s\t%s" %(last_key_city,maxtemp)
        (last_key_city,maxtemp)=(incity,int(intemp))
    else:
        last_key_city =incity
        maxtemp= max(maxtemp,int(intemp))
if last_key_city:
    print "%s\t%s" %(last_key_city,maxtemp)
