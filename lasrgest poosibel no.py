def lasrgest_psble_no(arr):
    dict = {}  # hashmap in java
    output = []
    for element in arr:

        left_most_elment = str(element)[0]
        if dict.has_key(left_most_elment):
            value.append(element)
            dict[left_most_elment]= value
            pass
        else :
            value = []
            value.append(element)

            dict[left_most_elment] =value

    keyset = sorted(dict.keys(),reverse=True)

    for key in keyset:
        valueset = sorted(dict[key],reverse=True)
        print key,valueset



arr = [21,27,26,9,90,17,61]
#arr = [29,2,7]
lasrgest_psble_no(arr)