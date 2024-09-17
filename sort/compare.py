from BubbleSort import bubble_sort
from SelectionSort import selection_sort
from InsertionSort import insertion_sort

import timeit
import random

random.seed(3.14159)


def get_random_data(number):
    return [random.randint(1, 1000) for _ in range(number)]


def compare(n):
    bubble_sort_time = timeit.timeit(
        lambda: bubble_sort(get_random_data(n)), number=100)
    selection_sort_time = timeit.timeit(
        lambda: selection_sort(get_random_data(n)), number=100)
    insertion_sort_time = timeit.timeit(
        lambda: insertion_sort(get_random_data(n)), number=100)

    print('=' * 50)
    print(f"data length {n}:")
    print(f"Bubble Sort:    {bubble_sort_time:.6f} seconds")
    print(f"Selection Sort: {selection_sort_time:.6f} seconds")
    print(f"Insertion Sort: {insertion_sort_time:.6f} seconds")


for n in [10, 100, 1000]:
    compare(n)
