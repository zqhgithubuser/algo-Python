def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    less_than_pivot = [x for x in arr[1:] if x < pivot]
    greater_than_pivot = [x for x in arr[1:] if x > pivot]
    return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)


if __name__ == "__main__":
    import random

    arr = [random.randint(1, 100) for _ in range(10)]
    print("Unsorted array:", arr)
    sorted_arr = quick_sort(arr)
    print("Sorted array:", sorted_arr)
