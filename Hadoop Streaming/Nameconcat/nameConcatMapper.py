#!/usr/bin/env python
import re
import sys

for line in sys.stdin:
    val = line.strip()
    (first_name,second_name) = val.split(",")
    concat_name =  first_name+second_name
    print "%s\t%s" %("hi",concat_name)