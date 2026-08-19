Recursive Factorial
def recursive_factorial(n):
    if n == 0 or n == 1:
        return 1

    return n * recursive_factorial(n - 1)
arr = [5, 3, 8, 4, 2]
n = 3
result = recursive_factorial(n)
print(f"Factorial of {n} is: {result}")
# Time Complexity:
# Best Case    : O(n)
# Average Case : O(n)
# Worst Case   : O(n)
#
# Space Complexity:
# O(n)
