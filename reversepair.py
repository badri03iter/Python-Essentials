inverse_pair_cnt=0
def shift(left,right,arr):
    global inverse_pair_cnt
    i=0
    j=0
    k=0

    while i < len(left) and j < len(right) :
        if left[i] < right[j] :
            arr[k]=left[i]
            i+=1
        else :
            arr[k]=right[j]
            j+=1
            inverse_pair_cnt = inverse_pair_cnt + len(left)- i
        k+=1

    while i < len(left):
        arr[k]=left[i]
        i+=1
        k+=1


    while j < len(right):
        arr[k]=right[j]
        j+=1
        k+=1
    print arr

def reversepair(arr):
    global inverse_pair_cnt

    if len(arr)> 1:
        mid = len(arr)/2
        left=arr[: mid]
        right=arr[mid :]
        print left,right
Un        reversepair(left)
        reversepair(right)
        shift(left,right,arr)
    return inverse_pair_cnt


arr = [15,12,3,1]
print arr
print reversepair(arr)

