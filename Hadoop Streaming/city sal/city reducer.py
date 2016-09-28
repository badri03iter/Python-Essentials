#!/usr/bin/env python
import re
import sys
sumsal =  0
last_key_city = None

for line in sys.stdin:
    val = line.strip()
    (incity,insal)=val.split("\t")
    if last_key_city and last_key_city != incity :
        print "%s\t%s" %(last_key_city,sumsal)
        (last_key_city,sumsal)=(incity,int(insal))

    else :
        last_key_city =incity
        sumsal +=int(insal)
if last_key_city :
    print "%s\t%s" %(last_key_city,sumsal)



