def insertion_sort(li):
    for i in xrange(1, len(li)):
        j = i
        while j > 0 and li[j] < li[j-1]:
            li[j], li[j-1] = li[j-1], li[j]
            j -= 1
    return li


if __name__ == "__main__":
    sample = [4, 6, 7, 5, 8, 9, 3, 1, 2]
    result = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert insertion_sort(sample) == result
