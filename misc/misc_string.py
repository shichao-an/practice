import unittest


def get_first_non_duplicate(s):
    """Get the first non-duplicate character in string `s`"""
    d = {}
    for c in s:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    for c in s:
        if d.get(c) == 1:
            return c


class TestString(unittest.TestCase):
    def test_get_first_non_duplicate(self):
        s1 = "what happened?"
        s2 = "you are out of yard!"
        f1 = get_first_non_duplicate(s1)
        f2 = get_first_non_duplicate(s2)
        assert f1 == 'w'
        assert f2 == 'e'


if __name__ == '__main__':
    unittest.main()
