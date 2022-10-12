'''
    BELLMAN'S ALGORITHM

    Algorithm for finding shortest path in a undirected/directed graph with
    negative cycle. Negative is a cycle whose net weight is negative.

    Example:

        0 ----------- 1 ----4 ---- 5
        |             |    /
        |             |   /
        |             |  /
        |             | /
        2 ----------- 3
'''

INF = int(1e9)


class Edge:
    def __init__(self, a, b, weight):
        self.a = a
        self.b = b
        self.weight = weight


adj = [[1, 2], [0, 3, 4], [0, 3], [1, 2, 4], [1, 3, 5], [4]]
edges = []

for i in range(0, len(adj)):
    for j in adj[i]:
        edges.append(Edge(i, j, 1))

# -----------------------------------------------
no_of_nodes = 6
path = [-1] * no_of_nodes

distance = [INF] * no_of_nodes
distance[0] = 0

for i in range(0, no_of_nodes - 1):
    for j in range(0, len(edges)):
        edge = edges[j]
        if distance[edge.a] < INF:
            if distance[edge.a] + edge.weight < distance[edge.b]:
                # For negative cycle
                distance[edge.b] = max(-INF, distance[edge.a] + edge.weight)
                path[edge.b] = edge.a

print(distance)
print(path)
