def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def selection_sort(arr):
    for outer in range(len(arr) - 1):
        min = outer
        for inner in range(outer + 1, len(arr)):
            if arr[inner] < arr[min]:
                min = inner
        swap(arr, outer, min)


if __name__ == "__main__":
    import random
    arr = [random.randint(1, 100) for _ in range(10)]
    print("Unsorted array:", arr)
    selection_sort(arr)
    print("Sorted array:", arr)
