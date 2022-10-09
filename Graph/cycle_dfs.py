'''
    FINDING A CYCLE USING DFS 

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

todo = [False] * no_of_nodes
done = [False] * no_of_nodes

def isCyclic(node):
    if todo[node]:
        return True;
    if done[node]:
        return False;
    todo[node] = done[node] = True
    for i in adj[node]:
        if not done[i] and isCyclic(i):
            return True
    todo[node] = False
    return False

for node in range(0, no_of_nodes):
    if not done[node] and isCyclic(node):
        print("Cycle Exists")
        exit()
print("No Cycle")
