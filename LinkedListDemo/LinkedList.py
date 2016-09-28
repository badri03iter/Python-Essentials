from DataStructureDemo.LinkedListDemo.Node import Node
class LinkedList(object):

    def __init__(self):
        self.head= None
        self.cnt =0
        self.tail=None
        pass


    def insert_start(self,data):
        newNode =Node(data)

        if self.head==None:
           self.head =newNode
           self.tail=newNode

        else :
            newNode.next = self.head
            self.head=newNode

        self.cnt+=1
        print "new node created %d "%(newNode.data)

    def traverse_list(self):

        if self.head==None:
            print "Linked list is empty"
            exit()
        else :
            temp = self.head

            while(temp != None):
                print str(temp.data) +"->",
                temp= temp.next
        print "\n"
        print "{0} nodes traversed".format(self.cnt)


    def insert_end(self,data):
        if self.head==None and self.tail==None:
            print "linked list empty.creating 1st node"
            newnode = Node(data)
            newnode.next=None
            self.head = newnode
            self.tail=newnode
            self.cnt+=1


        else :
            newnode= Node(data)
            self.tail.next = newnode
            self.tail = newnode
            self.cnt+=1








ll= LinkedList()
ll.insert_start(5)
ll.insert_start(15)
ll.insert_start(15)
ll.insert_start(15)
ll.insert_start(25)
ll.traverse_list()
ll.insert_end(56)
ll.insert_end(79)
ll.insert_end(89)
ll.insert_end(99)
ll.insert_start(15)
ll.insert_start(101)
ll.traverse_list()

