'''
    KAHN's ALGORITHM

    "A directed acyclic graph (DAG) G has at least one vertex with the indegree
        zero and one vertex with the out-degree zero."

    if indegree is one throughout the DAG then, travelling in BFS manner and 
    decrementing indegree we should be able to traverse the whole graph i.e all
    n nodes. If not possible, the graph contains a cycle

    Uses:
        1. Topological Sort
        2. Find Cycles

    Note:
        1. BFS approach, going level by level

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

indegree = [0] * no_of_nodes

for i in adj:
    for j in i:
        indegree[j] += 1

queue = []
for i in range(0, no_of_nodes):
    if indegree[i] == 0:
        queue.append(i)

while len(queue) != 0:
    node = queue[0]
    queue.pop(0)
    print(node, end=" -> ")
    for i in adj[node]:
        indegree[i] -= 1
        no_of_nodes -= 1
        if indegree[i] == 0:
            queue.append(i)

print("graph has a cycle" if no_of_nodes != 0 else "graph is acyclic")