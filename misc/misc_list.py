from __future__ import print_function


class ListNode(object):
    def __init__(self, data):
        self.data = data
        self.next = None


def create_list(a):
    """Create a singly linked list from an array `a`"""
    if not a:
        return None
    q = p = ListNode(a[0])
    for i in range(1, len(a)):
        p.next = ListNode(a[i])
        p = p.next
    return q


def restore_list(p):
    """Return array (Python list) from a linked list"""
    res = []
    while p is not None:
        res.append(p.data)
        p = p.next
    return res


def merge_sorted_lists(l1, l2):
    if l1 is None:
        return l2
    if l2 is None:
        return l1
    q = p = ListNode(-1)
    while l1 is not None or l2 is not None:
        if l1 is not None and l2 is not None:
            if l1.data <= l2.data:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
        else:
            if l1 is not None:
                p.next = l1
                l1 = l1.next
            if l2 is not None:
                p.next = l2
                l2 = l2.next
        p = p.next
    return q.next


def has_cycle(head):
    if head is None:
        return False
    fast = slow = head
    slow = slow.next
    if slow is None:
        return False
    else:
        fast = head.next.next
    while fast is not None:
        if fast == slow:
            return True
        slow = slow.next
        if fast.next is not None:
            fast = fast.next.next
        else:
            return False
    return False


def remove_duplicates(head):
    """
    Given a sorted linked list, delete all duplicates such that
    each element appear only once.
    """
    if head is None:
        return None
    if head.next is None:
        return head
    last = head
    current = head.next
    while current is not None:
        next_node = current.next
        if current.data == last.data:
            last.next = next_node
            # free(current) in C
        else:
            last = last.next
        current = next_node
    return head


def ntolast(head, n):
    if head is None:
        return None
    elif n == 0:
        return None
    elif head.next == ntolast(head.next, n - 1):
        return head
    else:
        return ntolast(head.next, n)


def ntolast2(head, n):
    """Non-recursive"""
    p = head
    q = head
    i = 0
    while p is not None and i < n:
        p = p.next
        i += 1
    while p is not None:
        p = p.next
        q = q.next
    return q


def print_list(head):
    if head is None:
        print('(empty)')
    else:
        while head is not None:
            print(head.data, end='')
            if head.next is not None:
                print('->', end='')
            head = head.next
        print()


def reverse_list(head):
    last_node = None
    while head is not None:
        next_node = head.next
        head.next = last_node
        last_node = head
        head = next_node
    return last_node


def are_same_lists(h1, h2):
    while h1 is not None and h2 is not None:
        if h1.data != h2.data:
            return False
        h1 = h1.next
        h2 = h2.next
    if h1 is None and h2 is None:
        return True
    return False


def is_even(head):
    """Determine whether the length of a list is even"""
    while head is not None and head.next is not None:
        head = head.next.next
    if head is None:
        return True
    return False


def reverse_pair_list(head):
    """Reverse a list in pairs
    For example, 1->2->3->4 will be 2->1->4->3
    """
    if head is None or head.next is None:
        return
    else:
        # Swap data instead of nodes
        head.next.data, head.data = head.data, head.next.data
        reverse_pair_list(head.next.next)


def get_mid(head):
    """Get the middle node of the list"""
    fast = head
    slow = head
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
    return slow


def is_palindrome(head):
    # First get the middle node and determine whether
    # the length of this list is even or odd
    fast = head
    slow = head
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next

    # Head of the second half
    second = slow

    # Odd
    if fast is not None and fast.next is None:
        second = second.next

    # Reverse second half
    last_node = None
    while second is not None:
        next_node = second.next
        second.next = last_node
        last_node = second
        second = next_node

    # Compare the two halves
    p = last_node
    q = head
    while p is not None:
        if p.data != q.data:
            return False
        p = p.next
        q = q.next
    return True
    # May need to reconstruct the list


def pascal_triangle(num):
    res = []
    res.append([1])
    if num == 1:
        return res
    res.append([1, 1])
    if num == 2:
        return res
    # n is current row index (starting from 0)
    for n in range(2, num):
        cur = []
        for i in range(n + 1):
            if i == 0:
                cur.append(1)
            elif i == n:
                cur.append(1)
            else:
                c = res[n - 1][i - 1] + res[n - 1][i]
                cur.append(c)
        res.append(cur)
    return res


def reverse(head):
    if head is None or head.next is None:
        return head
    else:
        res = reverse(head.next)
        p = res
        while p.next is not None:
            p = p.next
        p.next = head
        head.next = None
        return res


if __name__ == '__main__':
    l1 = create_list([2, 4, 5, 8])
    l2 = create_list([3, 4, 6, 7])
    p = merge_sorted_lists(l2, l1)
    assert restore_list(p) == [2, 3, 4, 4, 5, 6, 7, 8]
    l3 = create_list([3, 1])
    assert not has_cycle(l2)
    assert not has_cycle(l3)
    d1 = create_list([1, 2, 3, 4, 5])
    d2 = create_list([1, 1, 2, 3, 3])
    r1 = remove_duplicates(d1)
    r2 = remove_duplicates(d2)
    assert restore_list(r1) == [1, 2, 3, 4, 5]
    assert restore_list(r2) == [1, 2, 3]
    s1 = create_list([1, 2, 3, 4, 5, 6, 7])
    s1_end = ntolast2(s1, 0)
    s1_first = ntolast2(s1, 7)
    s1_last = ntolast2(s1, 1)
    s1_mid = ntolast2(s1, 4)
    s1_out = ntolast2(s1, 8)
    assert s1_end is None
    assert s1_first.data == 1
    assert s1_last.data == 7
    assert s1_mid.data == 4
    assert s1_out.data == 1
    rr1 = create_list([])
    rr2 = create_list([1])
    assert not are_same_lists(rr1, rr2)
    p1 = create_list([1, 2, 3, 4])
    p2 = create_list([4, 3, 2, 1])
    reverse_p1 = reverse_list(p1)
    p3 = create_list([1, 2])
    p4 = create_list([2, 1])
    reverse_p3 = reverse_list(p3)
    assert are_same_lists(reverse_p1, p2)
    assert are_same_lists(reverse_p3, p4)
    even0 = None
    even1 = create_list([1, 2])
    even2 = create_list([1, 2, 3, 4])
    odd1 = create_list([1])
    odd2 = create_list([1, 2, 3])
    assert is_even(even0)
    assert is_even(even1)
    assert not is_even(odd1)
    assert not is_even(odd2)
    pr1 = create_list([1, 2, 3, 4])
    pr1_res = create_list([2, 1, 4, 3])
    reverse_pair_list(pr1)
    assert are_same_lists(pr1, pr1_res)
    m1 = create_list([])
    m2 = create_list([1])
    m3 = create_list([1, 2])
    m4 = create_list([1, 2, 3])
    mid1 = get_mid(m1)
    mid2 = get_mid(m2)
    mid3 = get_mid(m3)
    mid4 = get_mid(m4)
    assert mid1 is None
    assert mid2.data == 1
    assert mid3.data == 2
    assert mid4.data == 2
    pan = None
    pa0 = create_list([0])
    pa1 = create_list([1, 1])
    pa2 = create_list([1, 2, 1])
    pa3 = create_list([1, 2, 2, 1])
    npa1 = create_list([1, 2])
    npa2 = create_list([1, 2, 3])
    npa3 = create_list([1, 2, 3, 4])
    assert is_palindrome(pan)
    assert is_palindrome(pa0)
    assert is_palindrome(pa1)
    assert is_palindrome(pa2)
    assert is_palindrome(pa3)
    assert not is_palindrome(npa1)
    assert not is_palindrome(npa2)
    print(pascal_triangle(5))
    sl1 = create_list([1])
    sl2 = create_list([1, 2])
    rl1 = reverse(sl1)
    rl2 = reverse(sl2)
    print(restore_list(rl1))
    print(restore_list(rl2))
