
'''
    DEPTH FIRST SEARCH

    1. Path found is the shortest to a node in a tree.
    
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

starting_node = 0
visited = [False] * no_of_nodes

# TODO: DFS by iteration

def dfs(node):
    visited[node] = True
    for child_node in adjacency_list[node]:
        if not visited[child_node]:
            print(child_node + 1)
            dfs(child_node)

dfs(starting_node)
