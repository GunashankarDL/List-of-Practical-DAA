class Edge:
    def __init__(self, u, v, w):
        self.u = u
        self.v = v
        self.w = w


# Find Parent
def find(parent, x):
    while parent[x] != x:
        x = parent[x]
    return x


# Union of Sets
def union(parent, a, b):
    parent[a] = b


# Sort Edges by Weight
def sort_edges(edges):
    edges.sort(key=lambda edge: edge.w)


arr = [[0, 2, 0, 6, 0],
       [2, 0, 3, 8, 5],
       [0, 3, 0, 0, 7],
       [6, 8, 0, 0, 9],
       [0, 5, 7, 9, 0]]

graph = []
n = len(arr)

for i in range(n):
    for j in range(i + 1, n):
        if arr[i][j] != 0:
            graph.append(Edge(i, j, arr[i][j]))

sort_edges(graph)

parent = [i for i in range(n)]

mst = []
cost = 0

for edge in graph:
    u = find(parent, edge.u)
    v = find(parent, edge.v)

    if u != v:
        mst.append(edge)
        cost += edge.w
        union(parent, u, v)

    if len(mst) == n - 1:
        break

print("Edges in Minimum Spanning Tree:")

for edge in mst:
    print(edge.u, "-", edge.v, ":", edge.w)

print("Minimum Cost =", cost)
