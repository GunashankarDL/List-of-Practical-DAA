def dfs(graph, visited, v, n):
    visited[v] = True
    print(v, end=" ")

    for i in range(n):
        if graph[v][i] == 1 and not visited[i]:
            dfs(graph, visited, i, n)
arr = [[0, 1, 1, 0, 0],
       [1, 0, 0, 1, 1],
       [1, 0, 0, 0, 1],
       [0, 1, 0, 0, 1],
       [0, 1, 1, 1, 0]]
n = len(arr)
visited = [False] * n
dfs(arr, visited, 0, n)
