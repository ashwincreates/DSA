'''
    BREADTH FIRST SEARCH

    1. Path found is the shortest to a node.
    
    Time Complexity : O(n + m), where n -> no. of vertices, m -> no. of edges

    example graph:
        
        1 ------ 2 -- 5
        |        |   /
        |        |  / 
        |        | /
        3 ------ 4

        adjacency list = 1 -> [2, 3]
                         2 -> [1, 4, 5]
                         3 -> [1, 4]
                         4 -> [2, 3, 5]
                         5 -> [2, 4]
'''

adjacency_list = [[1, 2], [0, 3, 4], [0, 3], [1, 2, 4], [1, 3]]
no_of_nodes = 5

queue = []
level = [0] * 5
parent = [0] * 5
used = [False] * no_of_nodes

starting_node = 0
print(starting_node + 1)

queue.append(starting_node) # starting node
used[starting_node] = True 
parent[starting_node] = -1

while (len(queue) != 0): # while queue is not empty
    new_source = queue[0]
    queue.pop(0)

    for node in adjacency_list[new_source]:
        if not used[node]:
            used[node] = True
            queue.append(node)
            level[node] = level[new_source] + 1 # a node deeper than their parent
            parent[node] = new_source

print(parent)
print(level)

# Printing path of a node from root
u = 2
path = []
if not used[u]:
    print("No path")
else:
    v = u
    while v != -1:
        path.append(v)
        v = parent[v]
    print(" ".join([str(i) for i in path]))
