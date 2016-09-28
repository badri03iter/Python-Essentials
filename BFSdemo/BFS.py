def bfs_search(start_node):
    queue =[]
    start_node.visited=True
    queue.insert(0,start_node)
    while queue:
        node_visited =queue.pop()
        print node_visited.name

        for cnt_node in (node_visited.adjacent_vertex):
           if  cnt_node.visited== False:
               cnt_node.visited=True
               queue.insert(0,cnt_node)









