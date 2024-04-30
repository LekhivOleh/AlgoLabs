import unittest
from src.flowers_distribution import *


class TestMaxFlowersDistribution(unittest.TestCase):
    def test_normal_input(self):
        result = find_max_amount('roads.csv')
        self.assertEqual(result, 4)

    def test_empty_input(self):
        result = find_max_amount('roads_empty.csv')
        self.assertEqual(result, -1)


if __name__ == "__main__":
    unittest.main()
