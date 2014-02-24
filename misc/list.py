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


def print_list(p):
    res = []
    if p is None:
        print('Empty list.')
    while p is not None:
        res.append(p.data)
        p = p.next
    print(res)


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


if __name__ == '__main__':
    l1 = create_list([2, 4, 5, 8])
    l2 = create_list([3, 4, 6, 7])
    print_list(l1)
    print_list(l2)
    p = merge_sorted_lists(l2, l1)
    print_list(p)
    l3 = create_list([3, 1])
    print(has_cycle(l2))
    print(has_cycle(l3))
