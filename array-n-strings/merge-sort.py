def merge_sort(l):
    if len(l) <= 1:
        return l

    mid = len(l) / 2
    a, b = merge_sort(l[:mid]), merge_sort(l[mid:])

    return merge(a, b)


def merge(a, b):
    i, j = 0, 0

    c = []
    while i <= len(a) and j <= len(b):
        if i == len(a): return c + b[j:]
        if j == len(b): return c + a[i:]

        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1

    return c

print merge_sort([5,4,3, -2,2,-1,-1,11,1,-2])
