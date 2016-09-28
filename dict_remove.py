def dup_remove(arr):
    s1 =set(arr)
    print s1
    dict ={}
    for i in arr:
        if dict.has_key(i):
            s1.remove(i)
            print s1
        else :
            dict[i]= True
            print dict
    print  s1




arr = [1,1,2,2,37,4,4,5,5]
dup_remove(arr)