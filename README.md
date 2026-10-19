# Analysis of Algorithms – Assignment 06

Yachay Tech – School of Mathematical and Computational Sciences

## Contents

| File | Exercise | Description |
|---|---|---|
| `merge_sort.py` | 2, 3 | Merge Sort implementation and stability experiment |
| `quick_sort.py` | 4 | Quick Sort implementation (randomized pivot, Lomuto partition) tested on random lists |
| `empirical_analysis.py` | 5 | Empirical analysis of Quick Sort (average and worst case) |

Exercise 1 (Master Theorem) is solved in the PDF submission.

## Requirements

- Python 3.8+
- matplotlib (only for `empirical_analysis.py`)

```bash
pip install -r requirements.txt
```

## How to run

```bash
python merge_sort.py
python quick_sort.py
python empirical_analysis.py
```

`empirical_analysis.py` prints the measurement tables and saves the plot `quicksort_empirical.png`.

## Summary of results

**Exercise 3 – Stability.** Merge Sort is stable when the merge step uses `<=`: on ties, the element from the left half (which appeared first in the input) is taken first. The script sorts students by grade and shows that students with equal grades keep their original order. A variant using `<` is included as a counterexample and is not stable.

**Exercise 5 – Empirical analysis.**
- Average case (random lists, random pivot): the measured number of comparisons is within about ±3% of the exact expected value 2(n+1)Hₙ − 4n, and time / (n log₂ n) stays roughly constant, confirming Θ(n log n).
- Worst case (already sorted list, fixed last-element pivot): the number of comparisons is exactly n(n−1)/2 and time / n² stays roughly constant, confirming Θ(n²).
