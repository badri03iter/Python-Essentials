def find_disticnt(input):
    i =0
    for anchor in xrange(len(input)) :
        print input
        distinct_cnt = 0
        if input[anchor] == input[i]:
           input[i]= input[i+1]
        else:
            anchor +=1
            distinct_cnt+=1
        i=+1
    print input



input = [1,2,2,3,3,4,4]
find_disticnt(input)