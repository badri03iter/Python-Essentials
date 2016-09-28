from DataStructureDemo.BFSdemo.Node import Node

import BFS

nodeA=Node("A")
nodeB=Node("B")
nodeC=Node("C")
nodeD=Node("D")
nodeE=Node("E")
nodeF=Node("F")
nodeG=Node("G")
nodeH=Node("H")

nodeA.adjacent_vertex=[nodeB,nodeC,nodeH]
nodeB.adjacent_vertex=[nodeD,nodeE]
nodeC.adjacent_vertex=[nodeF,nodeG]

BFS.bfs_search(nodeA)

