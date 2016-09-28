def nested(list1,output):

    for element in list1:
        if type(element) != list:
            output.append(element)
        else:
            nested(element,output)


output=[]
lsit = [1,2,[3,4,[5,6],7,[8,[9]]],10]
nested(lsit,output)
print output
