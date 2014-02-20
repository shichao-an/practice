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
