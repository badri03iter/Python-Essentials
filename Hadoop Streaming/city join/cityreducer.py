#!/usr/bin/env python
import re
import sys

city_name =None
city_grp_id = None

for line in sys.stdin:
    val = line.strip()
    splits =val.split("\t")
    city_id = splits[0]

    if city_id !=city_grp_id:
        if splits[1]=="A":
            city_name = splits[2]
            city_grp_id=city_id


    else :
         city_temp =splits[2]
         print "%s\t%s\t%s" %(city_id,city_temp,city_name)


