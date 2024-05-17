import unittest
from src.get_max_diameter import *


class TestGetMaxDiameter(unittest.TestCase):
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

    def test_new_tree(self):
        root = BinaryTree(50)
        root.right = BinaryTree(80)
        root.left = BinaryTree(31)
        root.left.left = BinaryTree(28)
        root.left.right = BinaryTree(40)
        root.left.left.left = BinaryTree(20)
        root.left.left.left.left = BinaryTree(18)
        root.left.left.left.right = BinaryTree(25)
        root.left.right.left = BinaryTree(39)
        root.left.right.right = BinaryTree(42)
        root.left.right.right.right = BinaryTree(45)
        root.left.right.right.right.right = BinaryTree(48)

        self.assertEqual(find_max_diameter(root), 7)

    def test_null_tree(self):
        result = find_max_diameter(BinaryTree(None))
        self.assertEqual(result, 0)


if __name__ == 'main':
    unittest.main()
