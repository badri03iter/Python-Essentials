def swap(arr,i,j):
    temp = arr[i]
    arr[i]= arr[j]
    arr[j] = temp

def partition(arr,start,end) :
    pivot = start
    left = start +1
    right = end
    done = True
    while done :
        while left <= right and arr[left] <= arr[pivot] :
            left = left +1

        while right >= left and arr[right] >= arr[pivot] :
            right = right - 1

        if left < right :
            swap(arr,left,right)
        else:
            done = False

    swap(arr,pivot,right)
   # print right
    return right

def find_kth_element(arr,k):
    start = 0
    end = len(arr) - 1
    if k > end :
        print " invalid rank asked "
        exit()
    if len(arr) < 1 :
        print " arr size 0"
        exit()

    while start <= end :

        pivot = partition(arr,start,end)

        if pivot+1 == k :
            print arr[pivot]
            break
        elif pivot+1 > k :

            start = 0
            end = pivot -1
            print arr,start,end
            pivot = partition(arr,start,end)


        else :

            start = pivot +1
            end = len(arr) -1
            pivot = partition(arr,start,end)






    print " The end "


arr = [5,4,3,10,21,76,7,8]
find_kth_element(arr,3)