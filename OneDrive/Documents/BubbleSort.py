def bubble_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

arr = [38,29,17,43,3,9,82,10]

print("Before sorting:",arr)

bubble_sort(arr)
print("After sorting:",arr)