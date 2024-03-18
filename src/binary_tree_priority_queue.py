class Node:
    def __init__(self, value, priority):
        self.left = None
        self.right = None
        self.value = value
        self.priority = priority


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value, priority):
        if self.root is None:
            self.root = Node(value, priority)
        else:
            self.inner_insert(self.root, value, priority)

    def inner_insert(self, node, value, priority):
        if priority >= node.priority:
            if node.left is None:
                node.left = Node(value, priority)
            else:
                self.inner_insert(node.left, value, priority)
        else:
            if node.right is None:
                node.right = Node(value, priority)
            else:
                self.inner_insert(node.right, value, priority)

    def delete(self):
        if self.root is None:
            return None
        else:
            return self.inner_delete(self.root)

    def inner_delete(self, node):
        if node.left is not None:
            value, priority = self.inner_delete(node.left)
            if node.left.priority == priority:
                node.left = None
            return value, priority
        else:
            return node.value, node.priority

    def print_inorder(self, node):
        if not node:
            return
        self.print_inorder(node.left)
        print(f'({node.value}, {node.priority})', end=' ')
        self.print_inorder(node.right)



