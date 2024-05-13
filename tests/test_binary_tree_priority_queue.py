import unittest
from src.binary_tree_priority_queue import *


class TestBinaryTreePriorityQueue(unittest.TestCase):
    def test_delete_max_priority_node(self):
        tree = BinaryTree()
        tree.insert(1, 0.1)
        tree.insert(2.5, 4.2)
        tree.insert(3, 0.5)
        tree.insert(4.2, 2.5)
        tree.insert(5, 1)
        tree.insert(6.1, 11)
        tree.insert(7, 3.5)
        tree.insert(8, 5)
        tree.insert(9, 10)

        self.assertEqual(tree.delete(), (6.1, 11))

    def test_one_element_tree(self):
        tree = BinaryTree()
        tree.insert(1, 1)

        self.assertEqual(((tree.root.value, tree.root.priority) == (1, 1)), True)

    def test_regular_Tree(self):
        tree = BinaryTree()
        tree.insert(1, 1)
        tree.insert(2, 4)
        tree.insert(3, 2)
        tree.insert(4, 6)
        tree.insert(5, 13)
        tree.insert(6, 12)

        self.assertEqual((tree.insert(7, 16), tree.delete()), (None, (7, 16)))


if __name__ == "__main__":
    unittest.main()
