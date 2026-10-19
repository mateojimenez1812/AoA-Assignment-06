"""
Lab 06 - Analysis of Algorithms
Ejercicio 2: Implementación de Merge Sort
Ejercicio 3: Experimento de estabilidad
"""
import random


def merge_sort(arr, key=lambda x: x):
    """Ordena una lista con Merge Sort (divide y vencerás). Devuelve una lista nueva."""
    if len(arr) <= 1:
        return arr[:]
    mid = len(arr) // 2
    left = merge_sort(arr[:mid], key)
    right = merge_sort(arr[mid:], key)
    return merge(left, right, key)


def merge(left, right, key=lambda x: x):
    """Mezcla dos listas ordenadas en una sola lista ordenada."""
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        # Se usa <= : ante empate se toma primero el de la IZQUIERDA.
        # Esto es lo que hace que Merge Sort sea ESTABLE.
        if key(left[i]) <= key(right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def merge_unstable(left, right, key=lambda x: x):
    """Variante con < en vez de <= (ante empate toma el de la derecha) -> NO estable."""
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if key(left[i]) < key(right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def merge_sort_unstable(arr, key=lambda x: x):
    if len(arr) <= 1:
        return arr[:]
    mid = len(arr) // 2
    return merge_unstable(merge_sort_unstable(arr[:mid], key),
                          merge_sort_unstable(arr[mid:], key), key)


def is_stable(original, sorted_list, key):
    """Verifica que los elementos con la misma clave conserven su orden relativo original."""
    pos = {id(x): i for i, x in enumerate(original)}
    for a, b in zip(sorted_list, sorted_list[1:]):
        if key(a) == key(b) and pos[id(a)] > pos[id(b)]:
            return False
    return True


if __name__ == "__main__":
    print("=" * 60)
    print("EJERCICIO 2: Merge Sort")
    print("=" * 60)
    data = [38, 27, 43, 3, 9, 82, 10]
    print("Entrada :", data)
    print("Salida  :", merge_sort(data))

    random.seed(1)
    ok = True
    for _ in range(1000):
        lst = [random.randint(-1000, 1000) for _ in range(random.randint(0, 200))]
        if merge_sort(lst) != sorted(lst):
            ok = False
    print("1000 listas aleatorias comparadas con sorted():", "OK" if ok else "FALLO")

    print()
    print("=" * 60)
    print("EJERCICIO 3: ¿Es Merge Sort estable?")
    print("=" * 60)
    # Estudiantes (nota, nombre). Ordenamos SOLO por la nota.
    students = [(85, "Ana"), (90, "Luis"), (85, "Carlos"), (70, "María"),
                (90, "Sofía"), (85, "Pedro"), (70, "José")]
    nota = lambda s: s[0]
    print("Entrada (orden original):")
    for s in students:
        print("   ", s)

    res = merge_sort(students, key=nota)
    print("\nMerge Sort (con <=), ordenado por nota:")
    for s in res:
        print("   ", s)
    print("¿Estable?:", is_stable(students, res, nota))
    print("  -> Ana, Carlos y Pedro (nota 85) mantienen su orden original.")

    res2 = merge_sort_unstable(students, key=nota)
    print("\nVariante con < (toma el de la derecha en empates):")
    for s in res2:
        print("   ", s)
    print("¿Estable?:", is_stable(students, res2, nota))

    # Prueba masiva de estabilidad con muchas claves repetidas
    random.seed(2)
    stable_all = True
    for _ in range(500):
        lst = [(random.randint(0, 5), i) for i in range(random.randint(1, 100))]
        if not is_stable(lst, merge_sort(lst, key=nota), nota):
            stable_all = False
    print("\n500 listas aleatorias con claves repetidas -> estable en todas:", stable_all)
