"""
Analysis of Algorithms - Assignment 06
Exercise 4: Quick Sort implementation, tested on randomly generated lists
"""
import random


class Counter:
    comparisons = 0


def partition(arr, low, high, counter=None):
    """Lomuto partition: uses arr[high] as the pivot."""
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if counter is not None:
            counter.comparisons += 1
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low=0, high=None, counter=None, randomized=True):
    """In-place Quick Sort. If randomized=True, the pivot is chosen at random."""
    if high is None:
        high = len(arr) - 1
    # Loop over the larger part to limit recursion depth
    while low < high:
        if randomized:
            r = random.randint(low, high)
            arr[r], arr[high] = arr[high], arr[r]
        p = partition(arr, low, high, counter)
        if p - low < high - p:
            quick_sort(arr, low, p - 1, counter, randomized)
            low = p + 1
        else:
            quick_sort(arr, p + 1, high, counter, randomized)
            high = p - 1
    return arr


if __name__ == "__main__":
    print("EXERCISE 4: Quick Sort on random lists")
    random.seed(42)
    for n in [10, 15, 20]:
        lst = [random.randint(0, 99) for _ in range(n)]
        print(f"\nn = {n}")
        print("Input  :", lst)
        print("Output :", quick_sort(lst[:]))

    print()
    tests, ok = 2000, 0
    for _ in range(tests):
        lst = [random.randint(-10**6, 10**6) for _ in range(random.randint(0, 500))]
        if quick_sort(lst[:]) == sorted(lst):
            ok += 1
    print(f"{ok}/{tests} random lists sorted correctly (compared with sorted())")
