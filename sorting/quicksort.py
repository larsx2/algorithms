import random

def qsort(a):
    A = len(a)
    if not A:
        return a

    pivot = a[0]
    left = qsort([x for x in a if x < pivot])
    right = qsort([x for x in a[1:] if x >= pivot])

    return left + [pivot] + right


print qsort([9, 8, 7, 3, 1, 2, 5, 4, 6, 8])
