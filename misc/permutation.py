import math
import unittest


def get_permutations(s):
    """
    Get permutations of a given string `s`
    Return a list of strings
    """
    if len(s) == 0:
        return ['']
    else:
        perms = []
        for i, char in enumerate(s):
            rest_chars = s[:i] + s[i + 1:]
            rest_perms = get_permutations(rest_chars)
            for _perm in rest_perms:
                perms.append(_perm + char)
        return perms


def get_permutations_alt_aux(s, c, res):
    """
    :param res: a list for storing permutations (list of lists)
    """
    if not s:
        res.append(''.join(c[:]))
    else:
        for i in range(len(s)):
            c.append(s[i])
            get_permutations_alt_aux(s[:i] + s[i + 1:], c, res)
            c.pop()


def get_permutations_alt(s):
    res = []
    c = []
    get_permutations_alt_aux(s, c, res)
    return res


class TestPermutation(unittest.TestCase):
    def _test_get_permutations(self, func=get_permutations):
        s1 = ''
        perms1 = func(s1)
        self.assertEqual(len(perms1), 1)
        assert '' in perms1
        s2 = 'abcd'
        f = math.factorial(len(s2))
        perms2 = func(s2)
        self.assertEqual(len(perms2), f)
        current = perms2[0]
        assert len(current) == len(s2)
        for i in range(1, f):
            _current = perms2[1]
            assert len(_current) == len(s2)
            for c in s2:
                assert c in _current
            assert _current != current
            _current = current

    def test_get_permutations(self):
        self._test_get_permutations(get_permutations)

    def test_get_permutations_alt(self):
        self._test_get_permutations(get_permutations_alt)


if __name__ == '__main__':
    unittest.main()
