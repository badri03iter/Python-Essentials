def compression(str1):
    print str1
    last_elemt = str1[0]
    cnt = 0
    output_arr =[]
    for curr in str1:
        if last_elemt == curr:
            cnt+=1
        else:
            output_arr.append(last_elemt)
            output_arr.append(cnt)
            cnt=1
        last_elemt=curr
    output_arr.append(last_elemt)
    output_arr.append(cnt)
    final_string=""
    for element in output_arr:
        final_string =final_string+ str(element)
    return final_string

str1 = 'AAAABBBBCCCCCDDEEEE'
print compression(str1)


sr =["A", 4]