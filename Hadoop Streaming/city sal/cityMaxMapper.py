#!/usr/bin/env python
import re
import sys

for line in sys.stdin:
    val= line.strip()
    (incity,intemp) = val.split(",")
    print "%s\t%s" %(incity,intemp)
