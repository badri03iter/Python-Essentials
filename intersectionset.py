def set_intersection(arr1,arr2):
    set1 = set(arr1)
    set2 = set(arr2)
    print set1,set2
    output = []

    for element in set1 :
        if element in set2 :
            print element
            print output.append(element)

    print output


arr1 = [1,2,3,4,4]
arr2 = [1,4,4]
set_intersection(arr1,arr2)