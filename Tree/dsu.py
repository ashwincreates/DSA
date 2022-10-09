'''
    DISJOINT SET UNION

    1. A DSU will have an operation to combine any two sets, and it will be 
       able to tell in which set a specific element is

    2. Operations
        -> make set
        -> union of set
        -> find set

    Naive:
        
        0 1 2 3 => (0 3) 1 2 => (0, 3) (1, 2) => (0, 3, 1, 2)

        0  1 2 =>  0  1 =>   1
       /          /  /      / |
      3          3  2      0  2
                          /
                         3
'''

no_of_set = 4
set_union = [[0, 3], [1, 2], [1, 3]]

parent = [i for i in range(0, no_of_set)]
size = [0] * no_of_set

def make_set(x):
    parent[x] = x
    size[x] = 1

def find_set(x):
    print(x, "-> ", end='')
    if x == parent[x]:
        print(x)
        return x
    parent[x] = find_set(parent[x]) # Path Compression
    return parent[x] 

def union_set(a, b):
    a = find_set(a)
    b = find_set(b)
    if a != b:
        if size[b] > size[a]:
            a, b = b, a
        parent[b] = a       # b became linked to a
        size[a] += size[b]  # a's size increases

for i in range(0, no_of_set):
    make_set(i)

for a, b in set_union:
    union_set(a, b)
    print(a, " U ", b)
    print(parent)
