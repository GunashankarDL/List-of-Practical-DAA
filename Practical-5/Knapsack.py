knapsack
def knapsack(wt, val, n, W):
   
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if wt[i - 1] <= w:
                dp[i][w] = max(
                    val[i - 1] + dp[i - 1][w - wt[i - 1]],
                    dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][W]
arr = [60, 100, 120]
wt = [10, 20, 30]
W = 70
n = len(arr)
result = knapsack(wt, arr, n, W)
print(f"Maximum value in Knapsack = {result}")
 Time Complexity:
# Best Case    : O(n * W)
# Average Case : O(n * W)
# Worst Case   : O(n * W)
#
# Space Complexity:
# O(n * W)
