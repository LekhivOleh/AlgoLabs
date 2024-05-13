import unittest
from src.shortest_safe_route import *


class TestShortestSafeRoute(unittest.TestCase):
    def test_given_matrix(self):
        find_the_shortest_safe_route('input_shortest_safe_route.txt', 'output_shortest_safe_route.txt')
        with open("../resources/output_shortest_safe_route.txt", "r") as output_file:
            output = output_file.read().strip()
        output_file.close()
        self.assertEqual(int(output), 11)

    def test_no_zeros_matrix(self):
        find_the_shortest_safe_route('input_shortest_safe_route_no_zeros.txt', 'output_shortest_safe_route_no_zeros.txt')
        with open("../resources/output_shortest_safe_route_no_zeros.txt", "r") as output_file:
            output = output_file.read().strip()
        output_file.close()
        self.assertEqual(int(output), 9)

    def test_empty_matrix(self):
        find_the_shortest_safe_route('input_shortest_safe_route_empty.txt', 'output_shortest_safe_route_empty.txt')
        with open("../resources/output_shortest_safe_route_empty.txt", "r") as output_file:
            output = output_file.read().strip()
        output_file.close()
        self.assertEqual(int(output), -1)

    def test_all_zeros_matrix(self):
        find_the_shortest_safe_route('input_shortest_safe_route_all_zeros.txt', 'output_shortest_safe_route_all_zeros.txt')
        with open("../resources/output_shortest_safe_route_all_zeros.txt", "r") as output_file:
            output = output_file.read().strip()
        output_file.close()
        self.assertEqual(int(output), -1)


if __name__ == "__main__":
    unittest.main()
