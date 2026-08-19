def matrix_chain(p,n):
    # Create DP table
    dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    # Cost is 0 when multiplying one matrix
    for i in range(1, n + 1):
        dp[i][i] = 0

    # l = Chain Length
    for l in range(2, n + 1):
        for i in range(1, n - l + 2):
            j = i + l - 1
            dp[i][j] = float('inf')

            for k in range(i, j):
                q = (
                    dp[i][k]
                    + dp[k + 1][j]
                    + p[i - 1] * p[k] * p[j]
                )

                if q < dp[i][j]:
                    dp[i][j] = q

    return dp[1][n]
p = [1,3,4,5]
n = len(p) - 1
print("Minimum number of multiplications is:", matrix_chain(p, n))

# Time Complexity:
# Best Case    : O(n^3)
# Average Case : O(n^3)
# Worst Case   : O(n^3)

# Space Complexity:O(n^2)
