class BinaryTree:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


def find_max_diameter(root: BinaryTree):
    max_diameter = 0
    if root.left is None or root.right is None:
        return 0

    def find_depth(node: BinaryTree):
        nonlocal max_diameter
        if node is None:
            return 0
        left_len = find_depth(node.left)
        right_len = find_depth(node.right)
        max_diameter = max(max_diameter, left_len + right_len)
        return max(right_len, left_len) + 1

    find_depth(root)
    return max_diameter
