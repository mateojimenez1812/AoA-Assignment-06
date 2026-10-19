"""
Analysis of Algorithms - Assignment 06
Exercise 2: Merge Sort implementation
Exercise 3: Stability experiment
"""
import random


def merge_sort(arr, key=lambda x: x):
    """Sort a list with Merge Sort (divide and conquer). Returns a new list."""
    if len(arr) <= 1:
        return arr[:]
    mid = len(arr) // 2
    left = merge_sort(arr[:mid], key)
    right = merge_sort(arr[mid:], key)
    return merge(left, right, key)


def merge(left, right, key=lambda x: x):
    """Merge two sorted lists into a single sorted list."""
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        # Using <= : on ties, the element from the LEFT half is taken first.
        # This is what makes Merge Sort STABLE.
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
    """Variant using < instead of <= (takes the right element on ties) -> NOT stable."""
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
    """Check that elements with equal keys keep their original relative order."""
    pos = {id(x): i for i, x in enumerate(original)}
    for a, b in zip(sorted_list, sorted_list[1:]):
        if key(a) == key(b) and pos[id(a)] > pos[id(b)]:
            return False
    return True


if __name__ == "__main__":
    print("EXERCISE 2: Merge Sort")
    data = [38, 27, 43, 3, 9, 82, 10]
    print("Input  :", data)
    print("Output :", merge_sort(data))

    random.seed(1)
    ok = True
    for _ in range(1000):
        lst = [random.randint(-1000, 1000) for _ in range(random.randint(0, 200))]
        if merge_sort(lst) != sorted(lst):
            ok = False
    print("1000 random lists compared with sorted():", "OK" if ok else "FAILED")

    print()
    print("EXERCISE 3: Is Merge Sort stable?")
    # Students (grade, name). We sort ONLY by grade.
    students = [(85, "Ana"), (90, "Luis"), (85, "Carlos"), (70, "Maria"),
                (90, "Sofia"), (85, "Pedro"), (70, "Jose")]
    grade = lambda s: s[0]
    print("Input (original order):")
    for s in students:
        print("   ", s)

    res = merge_sort(students, key=grade)
    print("\nMerge Sort (using <=), sorted by grade:")
    for s in res:
        print("   ", s)
    print("Stable?:", is_stable(students, res, grade))
    print("  -> Ana, Carlos and Pedro (grade 85) keep their original order.")

    res2 = merge_sort_unstable(students, key=grade)
    print("\nVariant using < (takes the right element on ties):")
    for s in res2:
        print("   ", s)
    print("Stable?:", is_stable(students, res2, grade))

    # Large stability test with many repeated keys
    random.seed(2)
    stable_all = True
    for _ in range(500):
        lst = [(random.randint(0, 5), i) for i in range(random.randint(1, 100))]
        if not is_stable(lst, merge_sort(lst, key=grade), grade):
            stable_all = False
    print("\n500 random lists with repeated keys -> stable in all of them:", stable_all)
