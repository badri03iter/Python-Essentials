import sys

def largest_continuos_sum(arr):
    if len(arr ) > 0 :
        max_sum = arr[0]
        curr_sum = arr[0]
        for i in xrange(1,len(arr)):
            curr_sum +=arr[i]
            if curr_sum > arr[i] :
                pass
            else:
                curr_sum =arr[i]
            if curr_sum > max_sum:
                max_sum=curr_sum
            else :
                pass


        print max_sum

def large_cont_sum(arr):

    # Check to see if array is length 0
    if len(arr)==0:
        return 0

    # Start the max and current sum at the first element
    max_sum=current_sum=arr[0]

    # For every element in array
    for num in arr[1:]:

        # Set current sum as the higher of the two
        current_sum=max(current_sum+num, num)

        # Set max as the higher between the currentSum and the current max
        max_sum=max(current_sum, max_sum)

    return max_sum

arr = [1,2,-1,3,4,10,10,-10,-1]
arr1 = [2,-1,3,4,-2]
arr2=[-1,-1,-2,-3,-4,-5,10,11]
arr3 =[-2,-3 ,7,5,11,23,21,56,-101,45,-67,999]
#
arr4 =[-1,1,2]
largest_continuos_sum(arr4)
print large_cont_sum(arr4)