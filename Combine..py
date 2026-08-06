
from encodings.punycode import insertion_sort

from MergeSort import merge_sort
from OneDrive.Documents.BubbleSort import bubble_sort
from QuickSort import quick_sort
from SelectionSort import selection_sort


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
arr = [20,10,8,15,2,1]
print("Before sorting:", arr)
bubble_sort(arr)
selection_sort(arr)
insertion_sort(arr)
merge_sort(arr, 0, len(arr) - 1)
quick_sort(arr, 0, len(arr) - 1)
print("After sorting:", arr)