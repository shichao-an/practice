class TreeNode(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class TreeNodeAlt(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.next = None


def new_tree_node(data):
    return TreeNode(data)


def max_tree_depth(root):
    if root is None:
        # Counting paths instead of nodes
        return -1
    left_max_depth = max_tree_depth(root.left)
    right_max_depth = max_tree_depth(root.right)
    return max(left_max_depth, right_max_depth) + 1


def is_same_tree(a, b):
    if a is None and b is None:
        return True
    if a is None or b is None:
        return False
    return (a.data == b.data and is_same_tree(a.left, b.left) and
            is_same_tree(a.right, b.right))


def unique_num_bst_recursive(n):
    """
    Given n, how many structurally unique BST's (binary search trees) that
    store values 1...n?

    """
    if n == 0:
        return 1
    if n == 1:
        return 1
    s = 0
    for i in range(n):
        s += unique_num_bst_recursive(i) * unique_num_bst_recursive(n - i - 1)
    return s


def unique_num_bst(n):
    # Initialize extra array `t`
    t = [0] * (n + 1)
    t[0] = 1
    for i in range(1, n + 1):
        t[i] = 0
        for j in range(i):
            t[i] += t[j] * t[i - j - 1]
    return t[n]


def preorder_traverse(root):
    """
    Binary tree preorder traversal (iterative)
    """
    stack = []
    path = []
    while True:
        while root is not None:
            path.append(root.data)
            stack.append(root)
            root = root.left
        if not stack:
            break
        root = stack.pop()
        root = root.right
    return path


def preorder_traverse_alt(root):
    stack = []
    path = []
    if root is None:
        return path
    stack.append(root)
    while stack:
        root = stack.pop()
        path.append(root.data)
        if root.right is not None:
            stack.append(root.right)
        if root.left is not None:
            stack.append(root.left)
    return path


def populate_next_right_pointers(root):
    if root is None:
        return
    if root.left is not None:
        root.left.next = root.right
    if root.right is not None:
        if root.next is not None:
            root.right.next = root.next.left
        # else, root.right.next is None by default
    populate_next_right_pointers(root.left)
    populate_next_right_pointers(root.right)


if __name__ == '__main__':
    root = new_tree_node(1)
    root.left = new_tree_node(2)
    root.right = new_tree_node(3)
    root.left.left = new_tree_node(4)
    root2 = new_tree_node(1)
    root2.right = new_tree_node(2)
    root2.right.right = new_tree_node(3)
    print(max_tree_depth(root))
    print(is_same_tree(root, root.left))
    print(is_same_tree(root, root))
    print(preorder_traverse(root))
    print(preorder_traverse(root2))
    print(preorder_traverse_alt(root))
    print(preorder_traverse_alt(root2))
    assert unique_num_bst(0) == 1
    assert unique_num_bst(1) == 1
    assert unique_num_bst(2) == 2
    assert unique_num_bst(3) == 5
