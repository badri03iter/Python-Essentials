#!/usr/bin/env python
import re
import sys

for line in sys.stdin:
    val = line.strip()
    (city_name,sal_name) = val.split(",")
    print "%s\t%s" %(city_name,sal_name)