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


def max_subarray(a):
    """
    Maximum subarray problem

    In case of all negative numbers, zero-length subarrays does not count.
    http://en.wikipedia.org/wiki/Maximum_subarray_problem
    """
    if not a:
        raise Exception('The input array must contain at least one number.')
    max_sum = a[0]

    # Initialize a list `m` of same size of a (which may be redundant for this
    # problem alone.
    # `m[i]` represents the max sum of all subarrays ending `i`
    m = [0] * len(a)
    m[0] = max_sum
    for i in range(1, len(a)):
        m[i] = max(a[i], m[i - 1] + a[i])

    # Find the largest in `m`
    for e in m:
        if e > max_sum:
            max_sum = e
    return max_sum


def max_subarray_alt(a):
    """
    Simpler implementation without extra space (auxiliary array `m`)
    """
    if not a:
        raise Exception('The input array must contain at least one number.')
    max_sum = a[0]
    max_current = max_sum
    for i in range(1, len(a)):
        max_current = max(a[i], max_current + a[i])
        max_sum = max(max_sum, max_current)
    return max_sum


def get_max_profit_ii(prices):
    """
    Multiple transactions allowed

    :param prices: array of prices where `prices[i]` represents the price on
        ith day
    """
    if not prices:
        return 0
    max_profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            max_profit += prices[i] - prices[i - 1]
    return max_profit


def get_max_profit_ii_alt(prices):
    """
    Utilized idea from `max_subarray`
    """
    if not prices:
        return 0
    max_profit = 0

    # `m[i]` represents the max profit ending `i`
    m = [0] * len(prices)
    m[0] = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            m[i] = m[i - 1] + prices[i] - prices[i - 1]
        else:
            m[i] = 0
    m += [0]
    # Get the sum of highest points
    for i, e in enumerate(m):
        if e == 0:
            max_profit += m[i - 1]
    return max_profit


def get_max_profit_iii(prices):
    """
    Two transactions allowed
    """
    if not prices:
        return 0
    n = len(prices)
    m1 = [0] * n
    m2 = [0] * n
    max_profit1 = 0
    min_price1 = prices[0]
    max_profit2 = 0
    max_price2 = prices[-1]
    for i in range(n):
        max_profit1 = max(max_profit1, prices[i] - min_price1)
        m1[i] = max_profit1
        min_price1 = min(min_price1, prices[i])
    for i in range(n):
        max_profit2 = max(max_profit2, max_price2 - prices[n - 1 - i])
        m2[n - 1 - i] = max_profit2
        max_price2 = max(max_price2, prices[n - 1 - i])
    max_profit = 0
    for i in range(n):
        max_profit = max(m1[i] + m2[i], max_profit)
    return max_profit


def get_max_profit_alt(prices):
    """
    :param prices: array of prices where `prices[i]` represents the price on
        ith day
    Only one transaction allowed
    """
    if not prices:
        return 0
    min_index = 0
    max_profit = 0
    buy_index = 0
    sell_index = 0
    for i in range(len(prices)):
        if prices[i] < prices[min_index]:
            min_index = i
        profit = prices[i] - prices[min_index]
        if profit > max_profit:
            max_profit = profit
            buy_index = min_index
            sell_index = i
    return prices[sell_index] - prices[buy_index]


def get_max_profit_alt2(prices):
    if not prices:
        return 0
    # small[i] indicates smallest price ending `i` (`i` included)
    # large[i] indicates largest prices after `i`
    n = len(prices)
    small = [0] * n
    large = [0] * n
    small[0] = prices[0]
    large[n - 1] = prices[n - 1]
    for i in range(1, n):
        small[i] = min(small[i - 1], prices[i])
        large[n - 1 - i] = max(large[n - 1], prices[n - 1 - i])
    max_profit = 0
    for i in range(n):
        d = large[i] - small[i]
        if d > max_profit:
            max_profit = d
    return max_profit


def get_max_profit(prices):
    if not prices:
        return 0
    max_profit = 0
    min_price = prices[0]
    for i, p in enumerate(prices, 0):
        max_profit = max(max_profit, (p - min_price))
        min_price = min(min_price, p)
    return max_profit


def search_insert(a, target):
    """
    Given a sorted array and a target value, return the index if the
    target is found. If not, return the index where it would be if it
    were inserted in order.
    """
    if not a:
        return 0
    n = len(a)
    left = 0
    right = n - 1
    while left <= right:
        mid = (left + right) / 2
        if a[mid] == target:
            return mid
        elif a[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left if left >= 0 else 0


def remove_element(a, element):
    """
    Given an array and a value, remove all instances of that value in place
    and return the new length.

    The order of elements can be changed. It doesn't matter what you leave
    beyond the new length.

    Implemented the C way.
    """
    n = len(a)
    m = 0  # new length
    for i in range(n):
        a[m] = a[i]
        if a[i] == element:
            pass
        else:
            m += 1
    return m


def backtrack_binary(n, A):
    if n < 1:
        print(A)
    else:
        A[n - 1] = 0
        backtrack_binary(n - 1, A)
        A[n - 1] = 1
        backtrack_binary(n - 1, A)


def get_gcd(a, b):
    while b != 0:
        (a, b) = (b, a % b)
    return a


def get_lcm(a, b):
    return a * b / get_gcd(a, b)


if __name__ == '__main__':
    assert reverse_integer(-173) == -371
    assert reverse_integer(976) == 679
    assert reverse_integer(500) == 5
    assert reverse_integer(0) == 0
    a = [2, 5, 5, 8, 9, 6, 2, 3, 9, 3, 6]
    assert get_single_integer(a) == 8
    b = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    c = [-3, -4, -5, -1, -9]
    assert max_subarray(b) == 6
    assert max_subarray_alt(b) == 6
    assert max_subarray(c) == -1
    assert max_subarray_alt(c) == -1
    d = [4, 2, 5, 7, 4, 3, 3, 6, 9]
    e = [3, 2, 1]
    f = [6, 1, 3, 2, 4, 7]
    g = [2, 4, 1]
    assert get_max_profit(d) == 7
    assert get_max_profit(e) == 0
    assert get_max_profit(f) == 6
    assert get_max_profit(g) == 2
    assert(get_max_profit_ii_alt(d) == 11)
    assert(get_max_profit_ii(d) == 11)
    assert(get_max_profit_ii_alt(f) == 7)
    assert(get_max_profit_ii(f) == 7)
    assert(get_max_profit_ii_alt(g) == 2)
    assert(get_max_profit_ii(g) == 2)
    s = [1, 3, 5, 6]
    assert(search_insert(s, 5) == 2)
    assert(search_insert(s, 2) == 1)
    assert(search_insert(s, 7) == 4)
    assert(search_insert(s, 0) == 0)
    assert remove_element([3, 1, 2, 4, 5, 1, 7], 1) == 5
    A = [0] * 5
    #backtrack_binary(5, A)
    h = [6, 1, 3, 2, 4, 7]
    assert get_max_profit_iii(h) == 7
    assert get_max_profit_iii(d) == 11
    assert get_gcd(48, 18) == 6
    assert get_gcd(18, 48) == 6
    assert get_lcm(48, 18) == 144
