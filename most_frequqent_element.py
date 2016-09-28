import collections
import sys
def find_most_freq(arr):
    s1 = list(set(arr));
    print s1

    dict = collections.defaultdict(int)
    for i in arr:
        dict[i] +=1

    max_element= s1[0]
    max_count= dict[max_element]
    for i in s1:

        if dict[i] > max_count :
            max_count=dict[i]
            max_element= i
    return(max_element,max_count)






arr = [1,2,1,7,7,7,7,5,5,5,5,7,7,7,7,7,7,1,4,4,5,5,6]
print arr
print find_most_freq(arr)