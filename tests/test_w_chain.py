import unittest
from src.w_chain import *


class TestWChainGame(unittest.TestCase):
    def test_normal_input(self):
        find_w_chain_length("w_chain_normal_input.txt", "w_chain_normal_output.txt")
        with open("../resources/w_chain_normal_output.txt", "r", encoding="utf-8") as file:
            result = file.readline()
        self.assertEqual(int(result), 6)

    def test_second_normal_input(self):
        find_w_chain_length("w_chain_second_normal_input.txt", "w_chain_second_normal_output.txt")
        with open("../resources/w_chain_second_normal_output.txt", "r", encoding="utf-8") as file:
            result = file.readline()
        self.assertEqual(int(result), 6)

    def test_empty_input(self):
        find_w_chain_length("w_chain_empty_input.txt", "w_chain_empty_output.txt")
        with open("../resources/w_chain_empty_output.txt", "r", encoding="utf-8") as file:
            result = file.readline()
        self.assertEqual(int(result), -1)


if __name__ == "__main__":
    unittest.main()
