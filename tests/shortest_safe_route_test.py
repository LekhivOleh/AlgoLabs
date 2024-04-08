import unittest
from src.shortest_safe_route import *


class TestShortestSafeRoute(unittest.TestCase):
    def test_given_matrix(self):
        main('../resources/input.txt', '../resources/output.txt')
        with open("../resources/output.txt") as output_file:
            output = output_file.read()
        output_file.close()
        self.assertEqual(int(output), 11)

    def test_no_zeros_matrix(self):
        main('../resources/input_no_zeros.txt', '../resources/output_no_zeros.txt')
        with open("../resources/output_no_zeros.txt") as output_file:
            output = output_file.read()
        output_file.close()
        self.assertEqual(int(output), 9)

    def test_empty_matrix(self):
        main('../resources/input_empty.txt', '../resources/output_empty.txt')
        with open("../resources/output_empty.txt") as output_file:
            output = output_file.read()
        output_file.close()
        self.assertEqual(int(output), -1)


if __name__ == "__main__":
    unittest.main()
