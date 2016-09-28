def merge(left,right,arr):
        i=0
        j=0
        k=0
        while i <len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i+=1
                k+=1
            else :
                arr[k]=right[j]
                j+=1
                k+=1
        while i < len(left) :
            arr[k]=left[i]
            i+=1
            k+=1
        while j < len(right):
            arr[k]=right[j]
            j+=1
            k+=1



def merge_sort(arr):

    if len(arr)> 1:
        mid =len(arr)/2
        left = arr[:mid]
        right=arr[mid:]
        print left,right
        merge_sort(left)
        merge_sort(right)
        merge(left,right,arr)
        print arr


arr =[400,300,200,100]
print arr
merge_sort(arr)
print arr