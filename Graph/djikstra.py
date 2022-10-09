'''
    DJIKSTRA'S ALGORITHM

    Algorithm for finding shortest path in a undirected/directed graph with
    positive weights.

    Example:

        0 ----------- 1 ----4 ---- 5
        |             |    /
        |             |   / 
        |             |  /
        |             | /
        2 ----------- 3

    RUNNING TIME:
        O(n ^ 2 + m)

    PROOF:

    Let there be a graph G -> (E, V)
    having weights initially to be inifinity.

    Let there be two sets S and S'
    Now,
        for every v in S: d[v] -> length of shortest path from s to 
                                  v that includes only vertices from S and
                                  d[v] will never change because it's the
                                  shortest path from s to v

        for every v in S': d[v] -> length of the shortest path from s to v 
                                    

        S                     S' 
    +-------+             +-------+ 
    |       |      P      |       |
    |   s   |-------------|   v   |
    |       |             |       |
    +-------+             +-------+ 

    let their be shortest path P from s to v
    now, P = P1 + P2
    P1 has all vertices from S
    P2 has a vertices from S' along with vertices from S

    s ---- P1 ---- q <------> p ---- P2 ---- v

    Here,
        d[p] = d[q] + l(p, q) 
    

    NOTE:

    1. Does not work on graph with negative cycle.
'''

adj = [[1, 2], [0, 3, 4], [0, 3], [1, 2, 4], [1, 3, 5], [4]]
no_of_nodes = 6

distance = [int(1e9)] * no_of_nodes
visited = [False] * no_of_nodes
path = [-1] * no_of_nodes

starting_node = 0
distance[starting_node] = 0

# Choosing N vertices
for i in range(0, no_of_nodes):
    v = -1
    # Choosing ith vertice having least distance and not marked
    for j in range(0, no_of_nodes):
        if not visited[j] and (v == -1 or distance[j] < distance[v]):
            v = j

    # if vertice is still at infinity it means it's not reachable
    if distance[v] == 1e9: 
        break
    
    visited[v] = True
    for i in adj[v]:
        if distance[v] + 1 < distance[i]:
            distance[i] = distance[v] + 1
            path[i] = v

print(distance)
print(path)