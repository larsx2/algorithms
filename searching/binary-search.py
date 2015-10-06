#!/usr/bin/env python

def bisect(li, n):
    lo, hi = 0, len(li)-1

    while lo <= hi:
        mid = (lo+hi)/2
        if n < li[mid]:
            hi = mid - 1
        elif n > li[mid]:
            lo = mid + 1
        else:
            return mid

    return None


def bisect_r(li, n, lo=0, hi=None):
    hi = len(li)-1 if hi is None else hi

    if lo > hi:
        return None

    mid = (lo+hi)/2
    if n == li[mid]:
        return mid

    if n > li[mid]:
        return bisect_r(li, n, lo=mid+1, hi=hi)
    elif n < li[mid]:
        return bisect_r(li, n, lo=lo, hi=mid-1)


if __name__ == "__main__":

    List = [1,2,3,4,5,6,7,8,9]
    assert bisect(List, 3) == bisect_r(List, 3)
    assert bisect(List, 9) == bisect_r(List, 9)
    assert bisect(List, 10) == bisect_r(List, 10)
