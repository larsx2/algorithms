def merge_sort(li, c=0, label=None):
    Len = len(li)

    print c *" ", "MERGE_SORT: {} {}".format(li, "({})".format(label) if label else '')

    if Len < 2:
        print (c+4) *" ", "RETURN {} ({})\n".format(li, label)
        return li

    mid = Len / 2
    print (c+4) *" ","(left) {} ++ {} (right)\n".format(li[:mid], li[mid:])

    left = merge_sort(li[:mid], c+4, label='left')
    right = merge_sort(li[mid:], c+4, label='right')

    print (c+4) *" ", "MERGE({}, {})".format(left, right)
    ret = merge(left, right)
    print (c+4) *" ", "RETURN {}\n".format(ret)
    return ret


def merge(a, b):
    i, j = 0, 0
    A, B = len(a), len(b)

    result = []
    while i < A or j < B:
        if i == A:
            result.extend(b[j:])
            break

        if j == B:
            result.extend(a[i:])
            break

        if a[i] < b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1

    return result

print merge_sort([3,4,1,5,2])
