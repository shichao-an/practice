from __future__ import print_function


def get_subsets(l, k):
    """Get subsets of size `k` of list `l`"""
    if k == 0:
        return [[]]
    else:
        res = []
        for i in range(len(l)):
            rest_subsets = get_subsets(l[i + 1:], k - 1)
            for subset in rest_subsets:
                subset.insert(0, l[i])
            res += rest_subsets
        return res


def get_all_subsets_aux(l, k):
    if k == 0:
        return [[]]
    else:
        res = [[]]
        for i in range(len(l)):
            rest_subsets = get_all_subsets_aux(l[i + 1:], k - 1)
            for subset in rest_subsets:
                subset.insert(0, l[i])
            res += rest_subsets
        return res


def get_all_subsets(l):
    return get_all_subsets_aux(l, len(l))


def test_get_subsets():
    a = [1, 2, 3]
    res = get_subsets(a, 2)
    print(res)


def test_get_all_subsets():
    a = [1, 2, 3]
    res = get_all_subsets(a)
    print(res)


if __name__ == '__main__':
    test_get_subsets()
    test_get_all_subsets()
