import operator
def odd_occuring(arr):
    res = arr[0]
    for i in xrange(1,len(arr)):
        res =operator.xor(res,arr[i])
    print res


arr =[2,2,7,6,7,3,3]
odd_occuring(arr)