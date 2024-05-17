import unittest
from src.penguin_gas_distribution import *


class TestFindPenguinGasDistribution(unittest.TestCase):
    def test_normal_input(self):
        check_gas_distribution_between_cities('../resources/input_gas_normal.txt', '../resources/output_gas_normal.txt')
        with open('../resources/output_gas_normal.txt', 'r', encoding='utf-8') as file:
            result = file.readline().strip('( )').split(')(')
            expected = ["'sh1', ['lviv', 'morshyn', 'dolyna', 'zhytomyr', 'sh2']", "'sh2', ['stryi', 'lviv', 'morshyn', 'dolyna', 'zhytomyr', 'sh1']"]
        self.assertEqual(result, expected)

    def test_empty_input(self):
        check_gas_distribution_between_cities('../resources/input_gas_empty.txt', '../resources/output_gas_empty.txt')
        with open('../resources/output_gas_empty.txt', 'r', encoding='utf-8') as file:
            result = file.readline().strip('( )').split(')(')
        self.assertEqual(result, ["-1"])

    def test_all_accessible_input(self):
        check_gas_distribution_between_cities('../resources/input_gas_all_accessible.txt', '../resources/output_gas_all_accessible.txt')
        with open('../resources/output_gas_all_accessible.txt', 'r', encoding='utf-8') as file:
            result = file.readline().strip('( )').split(')(')
            expected = ["'sh1', ['sh2']", "'sh2', ['sh1']"]
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
