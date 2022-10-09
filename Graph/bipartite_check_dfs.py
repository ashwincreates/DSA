'''
    BIPARTITE CHECK USING DFS
    
    We can check if the graph is bipartite by bipartite coloring. We traverse 
    from node to it's children and color them alternatively. For example if 
    a node has color red it's children will get color blue and it's children
    will be colored red and so on. If a node is already colored it should match
    the color it has to be colored in, otherwise the graph is not bipartite

    Adjacent node should not have same color for the graph to be bipartite

    For example:

        0 --------- 1      R --------- B
        |           |      |           |
        |           |      |           |
        |           |      |           |
        |           |      |           |
        3 --------- 2      B --------- R

'''

adj = [[1,3],[0,2],[1,3],[0,2]]
no_of_nodes = 4

colors = [0] * no_of_nodes

def valid_color(node, color):
    if colors[node] != 0:
        return colors[node] == color
    colors[node] = color
    for i in adj[node]:
        if not valid_color(i, -color):
            return False
    return True

for i in range(0, no_of_nodes):
    if colors[i] == 0 and not valid_color(i, 1):
        print("Not Bipartite")
        exit()

print("Bipartite")
