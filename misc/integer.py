def get_single_integer(integers):
    """
    Given a list of `integers`, every element appears twice except for one.
    Return that single one.
    """
    if not integers:
        return None
    p = integers[0]
    for i in range(1, len(integers)):
        p = p ^ integers[i]
    return p


def reverse_integer(number):
    t = 0
    if number > 0:
        positive = True
    else:
        positive = False
        number = -number
    while number != 0:
        t = 10 * t + number % 10
        number /= 10
    return t if positive else -t


if __name__ == '__main__':
    assert reverse_integer(-173) == -371
    assert reverse_integer(976) == 679
    assert reverse_integer(500) == 5
    assert reverse_integer(0) == 0
    a = [2, 5, 5, 8, 9, 6, 2, 3, 9, 3, 6]
    print(get_single_integer(a))
