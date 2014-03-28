import sys
#import pdb


def partition(A, left, right):
    """
    Basic partition (easier to understand but prone to bug while coding)
    """
    pivot = A[left]
    l = left + 1
    r = right
    while l < r:
        # Use latter edge condition to prevent index overflow
        while A[l] <= pivot and l < right:
            l += 1
        while A[r] > pivot and r > left + 1:
            r -= 1
        if l < r:
            swap(A, l, r)
    # For extreme case like: [1, 3]
    if A[left] > A[r]:
        swap(A, left, r)
    return r


def partition2(A, left, right):
    """CLRS variant"""
    pivot = A[right]
    i = left
    for j in range(left, right):
        if A[j] <= pivot:  # or equivalent: A[j] <= pivot
            swap(A, i, j)
            i += 1
    swap(A, i, right)
    return i


def quicksort(A, left, right):
    if left < right:
        p = partition2(A, left, right)
        quicksort(A, left, p - 1)
        quicksort(A, p + 1, right)


def quicksort_test(A):
    left = 0
    right = len(A) - 1
    quicksort(A, left, right)
    return A


def swap(A, i, j):
    A[i], A[j] = A[j], A[i]


def countingsort(A, k):
    """
    Elements of A are integers between 0 to k - 1
    """
    n = len(A)
    C = [0] * k
    B = [0] * n
    for i in range(n):
        C[A[i]] += 1
    for i in range(1, k):
        C[i] += C[i - 1]
    for i in range(n - 1, -1, -1):
        B[C[A[i]] - 1] = A[i]
        C[A[i]] -= 1
    return B


def test_sorting(func):
    print func.func_name
    assert func([]) == []
    assert func([1]) == [1]
    assert func([1, 2]) == [1, 2]
    assert func([2, 1]) == [1, 2]
    A = [3, 3, 2, 1]
    assert func(A) == sorted(A)
    B = [3, 1, 4, 2, 5]
    assert func(B) == sorted(B)
    C = [1, 1, 4, 3, 3]
    assert func(C) == sorted(C)
    D = [1] * 2 + [0] + [1] * 2
    assert func(D) == sorted(D)


if __name__ == '__main__':
    args = sys.argv[1:]
    #A = map(int, args)
    #pdb.set_trace()
    #quicksort(A, 0, len(A) - 1)
    #print A
    test_sorting(quicksort_test)
    #a = [3, 0, 2, 3, 1]
    #k = 4
    #print countingsort(a, k)
