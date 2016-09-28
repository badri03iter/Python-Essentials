from DataStructureDemo.DuplicateLL.Node import Node
class Linked_List(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_last(self,data):
        temp = Node(data)
        temp.data=data
        if self.head == None :
            self.head=temp
            self.tail=temp
        else :
            self.tail.next = temp
            self.tail = temp

    def insert_first(self,data):
        temp = Node(data)

        if self.head == None:
            self.head=temp
            self.tail=temp

        else :
            temp.next = self.head
            self.head=temp



    def traverse(self):
        temp = self.head
        while temp != None:
            if temp != self.tail:
                print str(temp.data) +"->",
                temp = temp.next
            else:
                print str(temp.data)
                break

        print "\n"



    def remove_duplicate(self):

        temp = self.head
        while temp.next != None :
            if temp.data != temp.next.data :
                temp = temp.next
            else:
                if temp.next != self.tail :
                    x=temp.next
                    temp.next = temp.next.next
                else :
                     temp.next=None
                     self.tail=temp
                     break


