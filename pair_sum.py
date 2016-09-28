
def pair_sum(ar,sum):

    s1 = set()
    output = set()
    for i in ar :
        pair_elemtn = sum - i
        if pair_elemtn not in s1 :
            s1.add(i)
            print s1
        else:
            output.add((min(i,pair_elemtn),max(i,pair_elemtn)))
    print output

ar = [1,3,2,2,5,1,3]
pair_sum(ar,4)