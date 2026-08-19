def print_array(arr):
    print("\nSorted Array:")
    print(*arr)

def main():
    n = int(input("Enter number of elements: "))

    arr = list(map(int, input("Enter elements:\n").split()))

    print("\nSorting Algorithms")
    print("1. Bubble Sort")
    print("2. Selection Sort")
    print("3. Insertion Sort")
    print("4. Merge Sort")
    print("5. Quick Sort")

    choice = int(input("\nEnter your choice: "))

    if choice == 1:
        bubble_sort(arr)

    elif choice == 2:
        selection_sort(arr)

    elif choice == 3:
        insertion_sort(arr)

    elif choice == 4:
        merge_sort(arr, 0, n - 1)

    elif choice == 5:
        quick_sort(arr, 0, n - 1)

    else:
        print("Invalid Choice")
        return

    print_array(arr)


if __name__ == "__main__":
    main()
