import unittest
from src.main import *


class TestGetLongestPeak(unittest.TestCase):
    def test_sorted_array(self):
        result = get_longest_peak([1, 2, 3, 4, 5])
        self.assertEqual(result, 0)

    def test_sorted_reversed_array(self):
        result = get_longest_peak([5, 4, 3, 2, 1])
        self.assertEqual(result, 0)

    def test_two_elements_array(self):
        result = get_longest_peak([2, 3])
        self.assertEqual(result, 0)

    def test_no_peak_array(self):
        result = get_longest_peak([1, 1, 1, 1, 1, 1, 1, 1])
        self.assertEqual(result, 0)

    def test_three_peaks_array(self):
        result = get_longest_peak([1, 2, 3, 4, 2, 4, 5, 6, 3, 7, 8, 9, 2, 1])
        self.assertEqual(result, 6)


if __name__ == "__main__":
    unittest.main()
