"""
Analysis of Algorithms - Assignment 06
Exercise 5: Empirical analysis of Quick Sort
"""
import math
import random
import sys
import time

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from quick_sort import quick_sort, Counter

sys.setrecursionlimit(20000)
random.seed(0)
REPS = 5


def expected_comps(n):
    """EXACT expected number of comparisons of randomized Quick Sort: 2(n+1)H_n - 4n."""
    H = sum(1.0 / k for k in range(1, n + 1))
    return 2 * (n + 1) * H - 4 * n


def measure(n, make_list, randomized):
    times, comps = [], []
    for _ in range(REPS):
        lst = make_list(n)
        c = Counter()
        t0 = time.perf_counter()
        quick_sort(lst, counter=c, randomized=randomized)
        times.append(time.perf_counter() - t0)
        comps.append(c.comparisons)
    return sum(times) / REPS, sum(comps) / REPS


rand_list = lambda n: [random.random() for _ in range(n)]
sorted_list = lambda n: list(range(n))

# --- Average case: random lists ---
sizes = [1000, 2000, 5000, 10000, 20000, 50000, 100000, 200000]
print("EXERCISE 5: Empirical analysis of Quick Sort")
print()
print(f"AVERAGE CASE: random lists, random pivot (average of {REPS} runs)")
print(f"{'n':>8} {'time (s)':>10} {'comparisons':>13} {'2n ln n':>12} {'2(n+1)Hn-4n':>13} {'measured/exact':>15} {'t/(n log2 n) ns':>16}")
avg = []
for n in sizes:
    t, c = measure(n, rand_list, True)
    theo = 2 * n * math.log(n)
    exact = expected_comps(n)
    avg.append((n, t, c))
    print(f"{n:>8} {t:>10.4f} {c:>13.0f} {theo:>12.0f} {exact:>13.0f} {c/exact:>15.3f} {t/(n*math.log2(n))*1e9:>16.2f}")

# --- Worst case: already sorted list, fixed pivot (last element) ---
wsizes = [500, 1000, 2000, 3000, 4000, 5000]
print()
print("WORST CASE: already sorted list, pivot = last element (not randomized)")
print(f"{'n':>8} {'time (s)':>10} {'comparisons':>13} {'n(n-1)/2':>12} {'t/n^2 (ns)':>12}")
worst = []
for n in wsizes:
    t, c = measure(n, sorted_list, False)
    worst.append((n, t, c))
    print(f"{n:>8} {t:>10.4f} {c:>13.0f} {n*(n-1)//2:>12} {t/n**2*1e9:>12.2f}")

# --- Plots ---
fig, axes = plt.subplots(1, 3, figsize=(17, 5))

ns = [x[0] for x in avg]
ax = axes[0]
ax.plot(ns, [x[2] for x in avg], "o-", label="Measured comparisons")
ax.plot(ns, [expected_comps(n) for n in ns], "--", label="Exact expected 2(n+1)Hₙ − 4n")
ax.plot(ns, [2 * n * math.log(n) for n in ns], ":", color="gray", label="Asymptotic 2n ln n")
ax.set_title("Average case: comparisons")
ax.set_xlabel("n"); ax.set_ylabel("comparisons"); ax.legend(); ax.grid(alpha=.3)

ax = axes[1]
ts = [x[1] for x in avg]
k = ts[-1] / (ns[-1] * math.log2(ns[-1]))
ax.plot(ns, ts, "o-", label="Measured time")
ax.plot(ns, [k * n * math.log2(n) for n in ns], "--", label="c · n log₂ n (fitted)")
ax.set_title("Average case: running time")
ax.set_xlabel("n"); ax.set_ylabel("seconds"); ax.legend(); ax.grid(alpha=.3)

ax = axes[2]
wn = [x[0] for x in worst]
wt = [x[1] for x in worst]
k2 = wt[-1] / wn[-1] ** 2
ax.plot(wn, wt, "o-", color="tab:red", label="Measured time (sorted list)")
ax.plot(wn, [k2 * n ** 2 for n in wn], "--", color="gray", label="c · n² (fitted)")
ax.set_title("Worst case: fixed pivot on sorted list")
ax.set_xlabel("n"); ax.set_ylabel("seconds"); ax.legend(); ax.grid(alpha=.3)

plt.tight_layout()
plt.savefig("quicksort_empirical.png", dpi=130)
print("\nPlot saved to quicksort_empirical.png")
