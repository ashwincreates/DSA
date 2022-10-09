'''
    TOPOLOGICAL SORTING

    Topological sorting for Directed Acyclic Graph (DAG) is a linear ordering 
    of vertices such that for every directed edge u v, vertex u comes before v 
    in the ordering

    for example:

     u -> v
     if we get to v after u, so in a linear order v comes after u i.e [u, v]

    Uses:
        1. Find Cycles

    Note:
        1. DFS Approach 

    Example:

        5   4
       /|  /|
      / | / |
     /  |/  |
    2   0   1
    |      /
    |    /
    |  /
    |/
    3
''' 

adj = [[], [], [3], [1], [0, 1], [0, 2]]
no_of_nodes = 6

visited = [False] * no_of_nodes

def dfs(node):
    if visited[node]:
        return
    visited[node] = True
    for i in adj[node]:
        dfs(i)
    print(node)

for i in range(0, no_of_nodes):
    dfs(i)

