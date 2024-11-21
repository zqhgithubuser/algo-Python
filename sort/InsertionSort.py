def insertion_sort(arr):
    for outer in range(1, len(arr)):
        temp = arr[outer]
        inner = outer
        while inner > 0 and temp < arr[inner - 1]:
            arr[inner] = arr[inner - 1]
            inner -= 1
        arr[inner] = temp


if __name__ == "__main__":
    import random

    arr = [random.randint(1, 100) for _ in range(10)]
    print("Unsorted array:", arr)
    insertion_sort(arr)
    print("Sorted array:", arr)
