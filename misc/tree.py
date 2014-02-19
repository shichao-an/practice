class TreeNode(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


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


if __name__ == '__main__':
    root = new_tree_node(1)
    root.left = new_tree_node(2)
    root.right = new_tree_node(3)
    root.left.left = new_tree_node(4)
    print(max_tree_depth(root))
    print(is_same_tree(root, root.left))
    print(is_same_tree(root, root))
