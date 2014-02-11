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


class TestPermutation(unittest.TestCase):
    def test_get_permutations(self):
        s1 = ''
        perms1 = get_permutations(s1)
        self.assertEqual(len(perms1), 1)
        assert '' in perms1
        s2 = 'abcd'
        perms2 = get_permutations(s2)
        self.assertEqual(len(perms2), 24)
        current = perms2[0]
        for i in range(1, 24):
            _current = perms2[1]
            assert _current != current
            _current = current


if __name__ == '__main__':
    unittest.main()
