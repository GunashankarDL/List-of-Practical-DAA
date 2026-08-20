INF = float('inf')
def coin_change(coins, n, amount):
    # Initialize DP array
    dp = [INF] * (amount + 1)
    dp[0] = 0

    # Fill DP table
    for i in range(1, amount + 1):
        for j in range(n):
            if coins[j] <= i:
                dp[i] = min(dp[i], dp[i - coins[j]] + 1)

    if dp[amount] == INF:
        return -1

    return dp[amount]
arr = [1, 2, 5]
n = len(arr)
amount = 18
result = coin_change(arr, n, amount)
print(f"Minimum coins required for amount {amount} = {result}")
