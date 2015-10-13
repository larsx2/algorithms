import random

def qsort(a):
    A = len(a)
    if not A:
        return a

    pivot = a[0]
    left = qsort([x for x in a if x < pivot])
    right = qsort([x for x in a[1:] if x >= pivot])

    return left + [pivot] + right


def qsort_randomized(a):
    A = len(a)
    if A < 2:
        return a

    pivot = random.randint(0, A-1)
    left, right = [], []

    for i in xrange(A):
        if i == pivot:
            continue

        if a[i] < a[pivot]:
            left.append(a[i])
        else:
            right.append(a[i])

    return  qsort_randomized(left) + [a[pivot]] + qsort_randomized(right)


sample = [9, 8, 7, 3, 1, 2, 5, 4, 6, 8]
assert qsort(sample) == sorted(sample)
assert qsort_randomized(sample) == sorted(sample)

