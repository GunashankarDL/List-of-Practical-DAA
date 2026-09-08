
INF = 9999


def floyd_warshall(graph, n):
    # Floyd-Warshall Algorithm
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph[i][k] + graph[k][j] < graph[i][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]
arr = [[0, 3, INF, 7],
       [8, 0, 2, INF],
         [5, INF, 0, 1],
         [2, INF, INF, 0]]
n = len(arr)
floyd_warshall(arr, n)
print("The shortest distances between every pair of vertices are:")
for i in range(n):
    for j in range(n):
        if arr[i][j] == INF:
            print("INF", end="\t")
        else:
            print(arr[i][j], end="\t")
    print()
    