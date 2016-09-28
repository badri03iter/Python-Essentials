#!/usr/bin/env python
import re
import sys

last_key = None
maxtemp = -sys.maxint

for line in sys.stdin:
    val= line.strip()
    (inkey,intemp) = val.split("\t")
    if last_key and last_key == inkey:
        pass
    else:
        last_key=inkey
        maxtemp= intemp
        print "%s\t%s" %(last_key,maxtemp)



