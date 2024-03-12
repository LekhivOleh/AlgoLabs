import unittest
from src.get_max_diameter import find_max_diameter, BinaryTree


class TestBinaryTreeFunctions(unittest.TestCase):
    def test_tree_without_diameter(self):
        root = BinaryTree(1)
        root.left = BinaryTree(2)
        root.left.left = BinaryTree(3)
        root.left.left.left = BinaryTree(4)
        self.assertEqual(find_max_diameter(root), 0)

    def test_max_diameter(self):
        root = BinaryTree(1)
        root.right = BinaryTree(2)
        root.left = BinaryTree(3)
        root.left.left = BinaryTree(7)
        root.left.left.left = BinaryTree(8)
        root.left.left.left.left = BinaryTree(9)
        root.left.right = BinaryTree(4)
        root.left.right.right = BinaryTree(5)
        root.left.right.right.right = BinaryTree(6)

        self.assertEqual(find_max_diameter(root), 6)


if __name__ == 'main':
    unittest.main()
