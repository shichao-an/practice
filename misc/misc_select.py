def partition(a, left, right):
    pivot = right
    j = left
    for i in range(left, right):
        if a[i] <= a[pivot]:
            a[i], a[j] = a[j], a[i]
            j += 1
    a[j], a[pivot] = a[pivot], a[j]
    return j


def partition2(a, left, right):
    pivot = right
    j = left
    for i in range(left, right):
        if a[i] > a[pivot]:
            a[i], a[j] = a[j], a[i]
            j += 1
    a[j], a[pivot] = a[pivot], a[j]
    return j


def quickselect(a, left, right, k):
    if left <= right:
        p = partition(a, left, right)
        if p == k:
            return a[k]
        elif p > k:
            return quickselect(a, left, p - 1, k)
        else:
            return quickselect(a, p + 1, right, k)


def quickselect2(a, left, right, k):
    """Iterative"""
    while left <= right:
        p = partition(a, left, right)
        if p == k:
            return a[k]
        elif p > k:
            right = p - 1
        else:
            left = p + 1


def get_k_smallest(a, k):
    left = 0
    right = len(a) - 1
    while left <= right:
        p = partition(a, left, right)
        if p == k - 1:
            return a[:k]
        elif p > k - 1:
            right = p - 1
        else:
            left = p + 1


def get_k_largest(a, k):
    left = 0
    right = len(a) - 1
    while left <= right:
        p = partition2(a, left, right)
        if p == k - 1:
            return a[:k]  # a[0...k - 1]
        elif p > k - 1:
            right = p - 1
        else:
            left = p + 1


def get_k_largest2(a, k):
    left = 0
    right = len(a) - 1
    # The k-th largest is (n + 1 - k)-th smallest
    k = len(a) + 1 - k
    while left <= right:
        p = partition(a, left, right)
        if p == k - 1:
            return a[k - 1:]  # a[k - 1...n - 1]
        elif p > k - 1:
            right = p - 1
        else:
            left = p + 1


def test_quickselect(a, k):
    left = 0
    right = len(a) - 1
    print quickselect(a, left, right, k - 1)


def test_quickselect2(a, k):
    left = 0
    right = len(a) - 1
    print quickselect2(a, left, right, k - 1)


if __name__ == '__main__':
    a1 = [1]
    a2 = [1, 2]
    a3 = [1, 2, 3, 4, 5, 6]
    a4 = [1, 2, 3, 4, 5, 6, 7, 8]
    import random
    random.shuffle(a4)
    print a4

    test_quickselect(a1, 1)
    test_quickselect(a2, 1)
    test_quickselect(a3, 3)
    test_quickselect2(a1, 1)
    test_quickselect2(a2, 1)
    test_quickselect2(a3, 3)
    test_quickselect2(a4, 5)
    print get_k_smallest(a4, 5)
    print get_k_largest(a4, 2)
    print get_k_largest2(a4, 2)
