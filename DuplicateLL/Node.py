class Node(object):

    def __init__(self,data):
        self .data=data
        self.next = None


a1= Node("A")
b1= Node("B")
c1= Node("C")
d1= Node("D")
e1= Node("E")
f1= Node("F")
g1= Node("G")


a1.next= b1
b1.next= c1
c1.next= d1
d1.next= e1
e1.next= f1
f1.next= c1

n1= Node("1")
n2= Node("2")
n3= Node("3")
n4= Node("4")
n5= Node("5")
n6= Node("6")

n1.next= n2
n2.next= n3
n3.next= n4
n4.next= n5
n5.next= n6



def traverse1(node):
    temp = node
    while(temp !=None):
        if temp.next != None :
            print temp.data +">",
            temp= temp.next
        else :
            print temp.data
            break


def cycle_check(node):
    marker1 = node
    marker2 = node
    print marker1.data,marker2.data
    while marker2 != None and marker2.next.next !=None:
        marker2 = marker2.next.next
        marker1= marker1.next
        print marker1.data,marker2.data
        if (marker1 == marker2):
            print marker1.data,marker2.data
            return True
            break
    return False



print cycle_check(n1)
traverse1(n4)