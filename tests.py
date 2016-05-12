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

    def test_check_for_rook_with_piece_on_same_row(self):
        """
            When placing a piece on board
             - If it's a rook then there should be no other piece on same
                row or column
             - If it's not a rook then there should be other rook or queen
                on same row or column
        """
        cls = HarmlessChess()
        cls.board_size_x = 3
        cls.board_size_y = 3
        cls.board = [
            ['K2', '.', '.'],
            ['.', '.', '.'],
            ['.', '.', '.'],
        ]
        x, y = 0, 2

        self.assertFalse(cls.check_for_rook(x, y, 'R1'))

    def test_check_for_rook_with_no_piece_on_same_row(self):
        """
            When placing a piece on board
             - If it's a rook then there should be no other piece on same
                row or column
             - If it's not a rook then there should be other rook or queen
                on same row or column
        """
        cls = HarmlessChess()
        cls.board_size_x = 3
        cls.board_size_y = 3
        cls.board = [
            ['K2', '.', '.'],
            ['.', '.', '.'],
            ['.', '.', '.'],
        ]
        x, y = 1, 2

        self.assertTrue(cls.check_for_rook(x, y, 'R1'))

    def test_check_for_rook_with_two_piece_on_same_row(self):
        """
            When placing a piece on board
             - If it's a rook then there should be no other piece on same
                row or column
             - If it's not a rook then there should be other rook or queen
                on same row or column
        """
        cls = HarmlessChess()
        cls.board_size_x = 3
        cls.board_size_y = 3
        cls.board = [
            ['K2', '.', 'K1'],
            ['.', '.', '.'],
            ['.', '.', '.'],
        ]
        x, y = 2, 2

        self.assertFalse(cls.check_for_rook(x, y, 'R1'))

    def test_check_for_king_with_one_nearby_piece(self):
        """
            There should be no king with distance of one square
            of current position
        """
        cls = HarmlessChess()
        cls.board_size_x = 3
        cls.board_size_y = 3
        cls.board = [
            ['K2', '.', '.'],
            ['.', '.', '.'],
            ['.', '.', '.'],
        ]
        x, y = 0, 1
        self.assertFalse(cls.check_for_king(x, y))

        x, y = 0, 2
        self.assertTrue(cls.check_for_king(x, y))

        x, y = 1, 0
        self.assertFalse(cls.check_for_king(x, y))

        x, y = 1, 1
        self.assertFalse(cls.check_for_king(x, y))

        x, y = 2, 2
        self.assertTrue(cls.check_for_king(x, y))

    def test_check_for_king_with_two_nearby_pieces(self):
        """
            There should be no king with distance of one square
            of current position
        """
        cls = HarmlessChess()
        cls.board_size_x = 3
        cls.board_size_y = 3
        cls.board = [
            ['K2', '.', 'K1'],
            ['.', '.', '.'],
            ['.', '.', '.'],
        ]
        x, y = 0, 1
        self.assertFalse(cls.check_for_king(x, y))

        x, y = 1, 2
        self.assertTrue(cls.check_for_king(x, y))

        x, y = 1, 0
        self.assertFalse(cls.check_for_king(x, y))

        x, y = 1, 1
        self.assertFalse(cls.check_for_king(x, y))

        x, y = 2, 2
        self.assertTrue(cls.check_for_king(x, y))

        x, y = 0, 2
        self.assertTrue(cls.check_for_king(x, y))

    def test_check_for_king_with_three_pieces_on_board(self):
        """
            There should be no king with distance of one square
            of current position
        """
        cls = HarmlessChess()
        cls.board_size_x = 3
        cls.board_size_y = 3
        cls.board = [
            ['K2', '.', 'K1'],
            ['.', '.', '.'],
            ['K3', '.', '.'],
        ]
        x, y = 0, 1
        self.assertFalse(cls.check_for_king(x, y))

        x, y = 1, 2
        self.assertFalse(cls.check_for_king(x, y))

        x, y = 1, 0
        self.assertFalse(cls.check_for_king(x, y))

        x, y = 1, 1
        self.assertFalse(cls.check_for_king(x, y))

        x, y = 2, 2
        self.assertTrue(cls.check_for_king(x, y))

    def test_check_for_knight_with_with_piece(self):
        """

        """
        cls = HarmlessChess()
        cls.board_size_x = 4
        cls.board_size_y = 4
        cls.board = [
            ['R1', '.', '.', '.'],
            ['.', '.', '.', '.'],
            ['.', '.', '.', '.'],
            ['.', '.', 'N1', '.'],
        ]

        x, y = 1, 1
        self.assertFalse(cls.check_for_knight(x, y))

        x, y = 3, 1
        self.assertFalse(cls.check_for_knight(x, y))


if __name__ == '__main__':
    unittest.main()