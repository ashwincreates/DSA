'''
    CONNECTED COMPONENTS

    1. Path found is the shortest to a node.
    
    Time Complexity : O(n + m), where n -> no. of vertices, m -> no. of edges

    example graph:
        
        1 ------ 2 -- 5    6 -- 7
        |        |   /     |   /
        |        |  /      |  /
        |        | /       | /
        3 ------ 4         8

        adjacency list = 1 -> [2, 3]
                         2 -> [1, 4, 5]
                         3 -> [1, 4]
                         4 -> [2, 3, 5]
                         5 -> [2, 4]
                         6 -> [7, 8]
                         7 -> [6, 8]
                         8 -> [6, 7]
'''

adjacency_list = [[1, 2], [0, 3, 4], [0, 3], [1, 2, 4], [1, 3], [6, 7], [5, 7], [5, 6]]
no_of_nodes = 8

starting_node = 0
visited = [False] * no_of_nodes

component = []

def dfs(node):
    visited[node] = True
    component.append(node + 1)
    for child_node in adjacency_list[node]:
        if not visited[child_node]:
            dfs(child_node)

def find_components():
    for node in range(0, no_of_nodes):
        if not visited[node]:
            component.clear()
            dfs(node)
            print("component ", component)

find_components()
