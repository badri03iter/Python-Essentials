def multiply(arr):
    output = [1] * len(arr)
    print arr
    for i in xrange(len(arr)):
        for j in xrange(len(arr)):
            if i !=j :
             output[j]  = output[j]* arr[i]

    print output








arr=[1,2,3,4]
multiply(arr)