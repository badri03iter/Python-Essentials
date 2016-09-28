#!/usr/bin/env python
import re
import sys

for line in sys.stdin:
    val = line.strip()
    if len(val) > 5:
        (cityid,cityname)=val.split(",")
        print "%s\t%s\t%s" %(cityid,"A",cityname)

    else :
        (cityid,citytemp)=val.split(",")
        print "%s\t%s\t%s" %(cityid,"B",citytemp)
