'''
    ARTICULATION POINTS

    1. An articulation point (or cut vertex) is defined as a vertex which, when
       removed along with associated edges, makes the graph disconnected

    for example:

        1---2---4
        |  /|  /
        | / | /
        |/  |/
        3   5
'''
no_of_nodes = 5
adjacency_list = [[1, 2], [0, 2, 4, 3], [0, 1], [1, 4], [1, 3]]
entry_time = [-1] * no_of_nodes # entry time for node v
visited = [False] * no_of_nodes
low = [-1] * no_of_nodes # lowest entry time for node v

timer = 0

def dfs(node, parent_node = -1):
    global timer
    visited[node] = True
    entry_time[node] = low[node] = timer
    timer += 1
    children = 0
    for child_node in adjacency_list[node]:
        if child_node == parent_node:
            continue
        if visited[child_node]:
            low[node] = min(low[node], entry_time[child_node])
        else:
            dfs(child_node, node)
            low[node] = min(low[node], low[child_node])
            if low[child_node] >= entry_time[node] and parent_node != -1:
                print(node + 1, " is a cut point")
            children += 1
    if parent_node == -1 and children > 1:
        print(node + 1, " is a cut point")

def find_cutpoints():
    for node in range(0, no_of_nodes):
        if not visited[node]:
            dfs(node)

find_cutpoints()
