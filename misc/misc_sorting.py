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


def quicksort(A, left, right):
    if left < right:
        p = partition(A, left, right)
        quicksort(A, left, p - 1)
        quicksort(A, p + 1, right)


def swap(A, i, j):
    A[i], A[j] = A[j], A[i]


if __name__ == '__main__':
    args = sys.argv[1:]
    A = map(int, args)
    #pdb.set_trace()
    quicksort(A, 0, len(A) - 1)
    print A
