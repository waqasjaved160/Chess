"""
    This module contains tests for chess.py module
"""

import unittest

import math

import constants
from chess import HarmlessChess


class HarmlessChessTests(unittest.TestCase):
    """
        Test cases for HarmlessChess class
    """

    def setUp(self):
        pass

    def test_combination_of_pieces_method(self):
        """
            This will test the method returns the required number of
            combinations
        """
        cls = HarmlessChess()
        cls.bishops = 0
        cls.knights = 0
        cls.rooks = 1
        cls.queens = 0
        cls.kings = 2

        cls.make_combinations_of_pieces()

        self.assertEqual(len(cls.combination_of_pieces), math.factorial(3))


if __name__ == '__main__':
    unittest.main()