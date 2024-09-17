def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def bubble_sort(arr):
    for last in range(len(arr), 0, -1):
        for inner in range(0, last - 1):
            if arr[inner] > arr[inner + 1]:
                swap(arr, inner, inner + 1)


if __name__ == "__main__":
    import random
    arr = [random.randint(1, 100) for _ in range(10)]
    print("Unsorted array:", arr)
    bubble_sort(arr)
    print("Sorted array:", arr)
