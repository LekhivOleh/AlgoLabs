import unittest
from src.place_agressive_cows import *


class TestMaxDistanceBetweenCows(unittest.TestCase):
    def test_regular_sorted_case(self):
        result = distance_between_cows(6, 4, [1, 8, 9, 11, 15, 20])
        self.assertEqual(result, 5)

    def test_free_sections_from_test_case(self):
        result = distance_between_cows(5, 3, [1, 2, 8, 4, 9])
        self.assertEqual(result, 3)

    def test_elements_that_are_smoothly_increasing(self):
        result = distance_between_cows(20, 4, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
        self.assertEqual(result, 6)

    def test_elements_that_starts_not_with_one(self):
        result = distance_between_cows(6, 3, [8, 13, 16, 22, 26, 31])
        self.assertEqual(result, 9)


if __name__ == "__main__":
    unittest.main()
