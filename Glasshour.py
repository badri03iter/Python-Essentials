import collections
import sys
def glass_hour(arr):
    row = 0
    col = 0
    max_sum =-sys.maxint
    sum = -sys.maxint
    while row <=3 :
        i= row
        j=0
        while j <=3 :
            a=arr[i][j]
            b=arr[i][j+1]
            c=arr[i][j+2]
            d=arr[i+1][j+1]
            e=arr[i+2][j]
            f=arr[i+2][j+1]
            g=arr[i+2][j+2]
            sum = a+b+c+d+e+f+g
            print sum

            j+=1
        row+=1



arr = [
    [1, 1, 1, 0, 0,70],
    [0, 1, 0, 0 ,70, 0],
    [1, 1, 1, 70, 0 ,0],
    [0, 0, 80, 50, 0, 0],
    [0, 0, 0, 0, 50, 0],
    [0, 0, 0, 0, 0, 50]]
glass_hour(arr)
'''
    for i in xrange(6):
        for j in xrange(6):
            print arr[i][j],
        print "\n"
'''




st = collections