'''
    BRIDGES 

    1. Find the edges that connects the component.
    2. Lowest Time in a component is same
    
    Time Complexity : O(n + m), where n -> no. of vertices, m -> no. of edges

    example graph:
        
        1 ------ 2 -- 5 ---- 6 -- 7
        |        |   /       |   /
        |        |  /        |  /
        |        | /         | /
        3 ------ 4           8
                                           Entry Time       Lowest entry time
        adjacency list = 1 -> [2, 3]        0                0 
                         2 -> [1, 4, 5]     1                0
                         3 -> [1, 4]        3                0
                         4 -> [2, 3, 5]     2                0
                         5 -> [2, 4, 6]     4                1
                         6 -> [5, 7, 8]     5                5
                         7 -> [6, 8]        6                5
                         8 -> [6, 7]        7                5
'''
adjacency_list = [[1, 2], [0, 3, 4], [0, 3], [1, 2, 4], [1, 3, 5], [4, 6, 7], [5, 7], [5, 6]]
no_of_nodes = 8

entry_time = [-1] * no_of_nodes # entry time for node v
visited = [False] * no_of_nodes
low = [-1] * no_of_nodes # lowest entry time for node v

timer = 0

def dfs(node, parent_node = -1):
    global timer
    visited[node] = True
    entry_time[node] = low[node] = timer
    timer += 1
    for child_node in adjacency_list[node]:
        if child_node == parent_node:
            continue
        if visited[child_node]:
            low[node] = min(low[node], entry_time[child_node])
        else:
            dfs(child_node, node)
            low[node] = min(low[node], low[child_node])
            if (low[child_node] > entry_time[node]):
                print(node + 1, " to ", child_node + 1, " is a bridge")

def find_bridges():
    for node in range(0, no_of_nodes):
        if not visited[node]:
            dfs(node)

find_bridges()

print("Nodes:             ", [i for i in range(0, no_of_nodes)])
print("Entry time:        ", entry_time)
print("Lowest entry time: ", low)

''' OUTPUT
5  to  6  is a bridge
Nodes:              [0, 1, 2, 3, 4, 5, 6, 7]
Entry time:         [0, 1, 3, 2, 4, 5, 6, 7]
Lowest entry time:  [0, 0, 0, 0, 1, 5, 5, 5]
'''
