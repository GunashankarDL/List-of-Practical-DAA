from collections import deque

def bfs(graph, visited, start, n):
    queue = deque()

    visited[start] = True
    queue.append(start)

    while queue:
        v = queue.popleft()
        print(v, end=" ")

        for i in range(n):
            if graph[v][i] == 1 and not visited[i]:
                visited[i] = True
                queue.append(i)


arr = [[0, 1, 1, 0, 0],
       [1, 0, 0, 1, 1],
       [1, 0, 0, 0, 1],
       [0, 1, 0, 0, 1],
       [0, 1, 1, 1, 0]]

n = len(arr)
visited = [False] * n

bfs(arr, visited, 0, n)
