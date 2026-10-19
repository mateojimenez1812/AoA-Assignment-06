"""
Lab 06 - Analysis of Algorithms
Ejercicio 4: Implementación de Quick Sort y pruebas con listas aleatorias
"""
import random


class Counter:
    comparisons = 0


def partition(arr, low, high, counter=None):
    """Partición de Lomuto: usa arr[high] como pivote."""
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
    """Quick Sort in-place. Si randomized=True, el pivote se elige al azar."""
    if high is None:
        high = len(arr) - 1
    # Iteración sobre la parte más grande para limitar la profundidad de recursión
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
    print("=" * 60)
    print("EJERCICIO 4: Quick Sort con listas aleatorias")
    print("=" * 60)
    random.seed(42)
    for n in [10, 15, 20]:
        lst = [random.randint(0, 99) for _ in range(n)]
        print(f"\nn = {n}")
        print("Entrada :", lst)
        print("Salida  :", quick_sort(lst[:]))

    print()
    tests, ok = 2000, 0
    for _ in range(tests):
        lst = [random.randint(-10**6, 10**6) for _ in range(random.randint(0, 500))]
        if quick_sort(lst[:]) == sorted(lst):
            ok += 1
    print(f"{ok}/{tests} listas aleatorias ordenadas correctamente (comparadas con sorted())")
