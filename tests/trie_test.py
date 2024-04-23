import unittest
from src.trie import *


class TestTrieFunctions(unittest.TestCase):
    def test_normal_patters_trie_search(self):
        normal_patterns_search = ['apple', 'app', 'banana', 'cherry', 'grape', 'kiwi', 'lemon', 'car', 'cat',
                    'can', 'circle', 'colossus', 'plum', 'player', 'plane', 'platinum', 'plastic']
        normal_trie_search = create_trie_from_patterns(normal_patterns_search)
        result = normal_trie_search.search('colossus')
        self.assertEqual(result, True)

    def test_normal_patters_trie_search_prefix(self):
        normal_patterns_search_prefix = ['apple', 'app', 'banana', 'cherry', 'grape', 'kiwi', 'lemon', 'car', 'cat',
                           'can', 'circle', 'colossus', 'plum', 'player', 'plane', 'platinum', 'plastic']
        normal_trie_search_prefix = create_trie_from_patterns(normal_patterns_search_prefix)
        result = normal_trie_search_prefix.search_prefix('plu')
        self.assertEqual(result, True)

    def test_empty_trie_search(self):
        empty_patterns_search = []
        empty_trie_search = create_trie_from_patterns(empty_patterns_search)
        result = empty_trie_search.search('apple')
        self.assertEqual(result, False)

    def test_empty_trie_search_prefix(self):
        empty_patterns_search_prefix = []
        empty_trie_search_prefix = create_trie_from_patterns(empty_patterns_search_prefix)
        result = empty_trie_search_prefix.search_prefix('app')
        self.assertEqual(result, False)


if __name__ == "__main__":
    unittest.main()
