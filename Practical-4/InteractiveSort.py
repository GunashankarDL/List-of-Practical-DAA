Interactive Sort
def iterative_factorial(n):
    fact = 1

    for i in range(1, n + 1):
        fact *= i

    return fact
arr = [5, 3, 8, 4, 2]
n = 5
result = iterative_factorial(n)
print(f"Factorial of {n} is: {result}")
# Time Complexity:
# Best Case    : O(n)
# Average Case : O(n)
# Worst Case   : O(n)
#
# Space Complexity:
# O(1)
