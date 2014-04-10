import sys

MAX_INT = sys.maxint
MIN_INT = -sys.maxint - 1


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


def level_order_traverse(root):
    path = []
    queue = []
    if root is None:
        return path
    queue.append(root)
    while queue:
        t = queue.pop(0)
        path.append(t.data)
        if t.left is not None:
            queue.append(t.left)
        if t.right is not None:
            queue.append(t.right)
    return path


def inorder_traverse(root):
    stack = []
    path = []
    while True:
        while root is not None:
            stack.append(root)
            root = root.left
        if not stack:
            break
        root = stack.pop()
        stack.append(root)
        root = root.right
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


def find_max(root):
    if root is None:
        return MIN_INT
    else:
        left_max = find_max(root.left)
        right_max = find_max(root.right)
        return max(left_max, right_max, root.data)


def find_max_alt(root):
    """Non-recursive using level order traversal"""
    max_data = MIN_INT
    if root is None:
        return max_data
    queue = []
    queue.append(root)
    while queue:
        root = queue.pop(0)
        max_data = max(root.data, max_data)
        if root.left is not None:
            queue.append(root.left)
        if root.right is not None:
            queue.append(root.right)
    return max_data


def find_node(root, data):
    if root is None:
        return False
    else:
        if root.data == data:
            return True
        else:
            return find_node(root.left, data) or find_node(root.right, data)


def get_height(root):
    """Non-recursive variant of max_tree_depth()"""
    height = -1
    if root is None:
        return height
    queue = []
    queue.append(root)
    queue.append(None)
    while queue:
        root = queue.pop(0)
        if root is None:
            if queue:
                queue.append(None)
            height += 1
        else:
            if root.left is not None:
                queue.append(root.left)
            if root.right is not None:
                queue.append(root.right)
    return height


def get_num_leaves(root):
    """Non-recursive"""
    n = 0
    if root is None:
        return n
    queue = []
    queue.append(root)
    while queue:
        root = queue.pop(0)
        if root.left is None and root.right is None:
            n += 1
        else:
            if root.left is not None:
                queue.append(root.left)
            if root.right is not None:
                queue.append(root.right)
    return n


def get_diameter(root):
    if root is None:
        return 0
    else:
        left_d = get_diameter(root.left)
        right_d = get_diameter(root.right)
        left_h = get_height(root.left) + 1
        right_h = get_height(root.right) + 1
        d = max(left_d, right_d)
        return max(d, left_h + right_h + 1)


def get_paths_aux(root, path, paths):
    """
    Get all root-to-leave paths
    Return a list of list of intgers
    """
    if root is None:
        return
    path.append(root.data)
    if root.left is None and root.right is None:
        paths.append(path[:])
    else:
        get_paths_aux(root.left, path, paths)
        get_paths_aux(root.right, path, paths)
    path.pop()


def get_paths(root):
    path = []
    paths = []
    get_paths_aux(root, path, paths)
    return paths


def tree_mirror(root):
    if root is None:
        return
    else:
        tree_mirror(root.left)
        tree_mirror(root.right)
        root.left, root.right = root.right, root.left


def get_lca(root, a, b):
    """
    Get the least common ancestor of `a` and `b` in `root`
    """
    if root is None:
        return None
    if root == a or root == b:
        return root
    left_lca = get_lca(root.left, a, b)
    right_lca = get_lca(root.right, a, b)
    if left_lca is not None and right_lca is not None:
        return root
    else:
        return left_lca if left_lca is not None else right_lca


def _tree1():
    """
            1
           /
          2
         / \
        3   4
       /   /
      6   5
    """
    root = new_tree_node(1)
    q = root
    q.left = new_tree_node(2)
    q = q.left
    q.left = new_tree_node(3)
    q.right = new_tree_node(4)
    q.right.left = new_tree_node(5)
    q = q.left
    q.left = new_tree_node(6)
    return root

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
    print(level_order_traverse(root))
    print(find_max(root))
    print(find_max_alt(root))
    print(find_node(root, 4))
    print(find_node(root, 5))
    print(get_height(root))
    print(get_height(root.left))
    print(get_num_leaves(root))
    print(get_num_leaves(root.left))
    print(get_diameter(root))
    print(get_diameter(_tree1()))
    print(get_paths(root))
    t1 = _tree1()
    tree_mirror(t1)
