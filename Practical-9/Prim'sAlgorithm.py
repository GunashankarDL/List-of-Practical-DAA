
INF = float('inf')


def prim_mst(graph, n):
    selected = [False] * n
    selected[0] = True  # Start from vertex 0

    edge = 0
    cost = 0

    print("\nEdges in Minimum Spanning Tree:")

    while edge < n - 1:
        minimum = INF
        x = y = -1

        for i in range(n):
            if selected[i]:
                for j in range(n):
                    if not selected[j] and graph[i][j] < minimum:
                        minimum = graph[i][j]
                        x = i
                        y = j

        print(f"{x} --> {y}  Cost = {graph[x][y]}")
        cost += graph[x][y]
        selected[y] = True
        edge += 1

    print(f"\nMinimum Cost = {cost}")
arr = [[0, 2, 0, 6, 0],
       [2, 0, 3, 8, 5],
         [0, 3, 0, 0, 7],
         [6, 8, 0, 0, 9],
         [0, 5, 7, 9, 0]]
n = len(arr)
prim_mst(arr, n)