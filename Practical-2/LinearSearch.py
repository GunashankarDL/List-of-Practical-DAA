Linear Search
def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1
arr = [5, 3, 8, 4, 2]
key = 4
result = linear_search(arr, key)
print(f"Element found at index: {result}")
# Linear Search
#
# Time Complexity:
# Best Case    : O(1)
# Average Case : O(n)
# Worst Case   : O(n)
#
# Space Complexity:
# O(1)
