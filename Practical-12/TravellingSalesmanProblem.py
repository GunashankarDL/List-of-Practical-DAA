
INF = float('inf')


# Recursive Function
def tsp(graph, visited, city, count, cost, n):
    global min_cost

    # All cities visited
    if count == n and graph[city][0] != 0:
        cost += graph[city][0]
        min_cost = min(min_cost, cost)
        return

    for i in range(n):
        if not visited[i] and graph[city][i] != 0:
            visited[i] = True

            tsp(graph, visited, i, count + 1, cost + graph[city][i], n)

            visited[i] = False
arr = [[0, 10, 15, 20],
       [10, 0, 35, 25],
         [15, 35, 0, 30],
         [20, 25, 30, 0]]
n = len(arr)
min_cost = INF
visited = [False] * n
visited[0] = True
tsp(arr, visited, 0, 1, 0, n)
print(f"Minimum cost of travelling salesman problem = {min_cost}")
