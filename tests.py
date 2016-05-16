"""
    This module contains tests for chess.py module
"""

import unittest

from mock import patch, PropertyMock  # pragma: no cover

from chess import HarmlessChess


class HarmlessChessTests(unittest.TestCase):
    """
        Test cases for HarmlessChess class
    """

    def test_pieces_appended_to_a_list(self):
        cls = HarmlessChess()
        cls.bishops = 1
        cls.knights = 1
        cls.kings = 1
        cls.queens = 1
        cls.rooks = 1

        expected_result = ['B1', 'N1', 'K1', 'Q1', 'R1']
        cls.make_list_of_pieces()

        self.assertItemsEqual(expected_result, cls.pieces)

    def test_board_initialize_method(self):
        cls = HarmlessChess()
        cls.board_size_x = 3
        expected_result = [
            ['.', '.', '.'],
            ['.', '.', '.'],
            ['.', '.', '.']
        ]
        cls.initialize_board()

        self.assertEqual(expected_result, cls.board)

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

    def test_check_for_rook_with_two_different_piece_on_same_row(self):
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
            ['.', '.', 'K1'],
            ['R1', '.', '.'],
            ['.', '.', '.'],
        ]
        x, y = 2, 2

        self.assertTrue(cls.check_for_rook(x, y, 'K2'))

        x, y = 1, 2
        self.assertFalse(cls.check_for_rook(x, y, 'K2'))

    def test_check_for_king_with_one_nearby_piece(self):
        """
            There should be no king with distance of one square
            of current position
        """
        cls = HarmlessChess()
        cls.board_size_x = 3
        cls.board_size_y = 3
        cls.board = [
            ['R1', '.', '.'],
            ['.', '.', '.'],
            ['.', '.', '.'],
        ]
        x, y = 0, 1
        self.assertFalse(cls.check_for_king(x, y, 'K'))

        x, y = 0, 2
        self.assertTrue(cls.check_for_king(x, y, 'K'))

        x, y = 1, 0
        self.assertFalse(cls.check_for_king(x, y, 'K'))

        x, y = 1, 1
        self.assertFalse(cls.check_for_king(x, y, 'K'))

        x, y = 2, 2
        self.assertTrue(cls.check_for_king(x, y, 'K'))

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
        self.assertFalse(cls.check_for_king(x, y, 'K'))

        x, y = 1, 2
        self.assertFalse(cls.check_for_king(x, y, 'K'))

        x, y = 1, 0
        self.assertFalse(cls.check_for_king(x, y, 'R'))

        x, y = 1, 1
        self.assertFalse(cls.check_for_king(x, y, 'R'))

        x, y = 2, 2
        self.assertTrue(cls.check_for_king(x, y, 'K'))

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
        self.assertFalse(cls.check_for_king(x, y, 'R'))

        x, y = 1, 2
        self.assertFalse(cls.check_for_king(x, y, 'B'))

        x, y = 1, 0
        self.assertFalse(cls.check_for_king(x, y, 'K'))

        x, y = 1, 1
        self.assertFalse(cls.check_for_king(x, y, 'R'))

        x, y = 2, 2
        self.assertTrue(cls.check_for_king(x, y, 'R'))

    def test_check_for_knight_with_another_knight(self):
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
        self.assertFalse(cls.check_for_knight(x, y, 'N'))

        x, y = 3, 1
        self.assertTrue(cls.check_for_knight(x, y, 'N'))

    def test_check_for_knight_with_another_piece(self):
        """

        """
        cls = HarmlessChess()
        cls.board_size_x = 4
        cls.board_size_y = 4
        cls.board = [
            ['R1', '.', '.', '.'],
            ['.', 'R2', '.', '.'],
            ['.', '.', '.', '.'],
            ['.', '.', '.', '.'],
        ]

        x, y = 2, 3
        self.assertFalse(cls.check_for_knight(x, y, 'N'))

    def test_check_for_queen_with_one_piece_places(self):
        cls = HarmlessChess()
        cls.board_size_x = 4
        cls.board_size_y = 4
        cls.board = [
            ['R1', '.', '.', '.'],
            ['.', 'R2', '.', '.'],
            ['.', '.', '.', '.'],
            ['.', '.', '.', '.'],
        ]

        x, y = 2, 3
        self.assertTrue(cls.check_for_queen(x, y, 'Q'))

    def test_check_for_queen_with_queen_piece_placed(self):
        cls = HarmlessChess()
        cls.board_size_x = 4
        cls.board_size_y = 4
        cls.board = [
            ['R1', '.', '.', '.'],
            ['.', '.', 'Q1', '.'],
            ['.', '.', '.', '.'],
            ['.', '.', '.', '.'],
        ]

        x, y = 2, 3
        self.assertFalse(cls.check_for_queen(x, y, 'K'))

    def test_check_for_queen_with_queen_affecting_diagonally(self):
        cls = HarmlessChess()
        cls.board_size_x = 4
        cls.board_size_y = 4
        cls.board = [
            ['R1', '.', '.', '.'],
            ['.', '.', '.', '.'],
            ['.', '.', '.', '.'],
            ['.', '.', '.', '.'],
        ]

        x, y = 2, 2
        self.assertFalse(cls.check_for_queen(x, y, 'Q'))

    def test_check_for_queen_with_queen_affecting_row_col(self):
        cls = HarmlessChess()
        cls.board_size_x = 4
        cls.board_size_y = 4
        cls.board = [
            ['R1', '.', '.', '.'],
            ['.', '.', '.', '.'],
            ['.', '.', '.', '.'],
            ['.', '.', '.', '.'],
        ]

        x, y = 2, 0
        self.assertFalse(cls.check_for_queen(x, y, 'Q'))

        x, y = 0, 3
        self.assertFalse(cls.check_for_queen(x, y, 'K'))

    def test_check_for_bishop_with_one_piece(self):
        cls = HarmlessChess()
        cls.board_size_x = 3
        cls.board_size_y = 3
        cls.board = [
            ['K2', '.', '.'],
            ['.', '.', '.'],
            ['.', '.', '.'],
        ]
        x, y = 0, 2

        self.assertTrue(cls.check_for_bishop(x, y, 'B1'))

    def test_check_for_bishop_with_bishop_in_piece(self):
        cls = HarmlessChess()
        cls.board_size_x = 3
        cls.board_size_y = 3
        cls.board = [
            ['K1', '.', 'B1'],
            ['.', '.', '.'],
            ['.', '.', '.'],
        ]
        x, y = 1, 1
        self.assertFalse(cls.check_for_bishop(x, y, 'R1'))

        x, y = 2, 0
        self.assertFalse(cls.check_for_bishop(x, y, 'B2'))

    def test_piece_in_danger(self):
        cls = HarmlessChess()
        cls.board_size_x = 3
        cls.board_size_y = 3
        cls.board = [
            ['K1', '.', 'B1'],
            ['.', '.', '.'],
            ['.', '.', '.'],
        ]
        x, y = 2, 1
        self.assertFalse(cls.in_danger(x, y, 'K2'))

    def test_piece_can_be_placed_on_board_without_any_harm(self):
        cls = HarmlessChess()
        cls.board_size_x = 3
        cls.board_size_y = 3
        cls.board = [
            ['K1', '.', 'B1'],
            ['.', '.', '.'],
            ['.', '.', '.'],
        ]
        x, y = 2, 1

        expected_result = [
            ['K1', '.', 'B1'],
            ['.', '.', '.'],
            ['.', 'K2', '.'],
        ]

        self.assertTrue(cls.place_without_harming(x, y, 'K2'))
        self.assertEqual(cls.board, expected_result)

    def test_piece_can_be_placed_on_board_on_preoccupied_place(self):
        cls = HarmlessChess()
        cls.board_size_x = 3
        cls.board_size_y = 3
        cls.board = [
            ['K1', '.', 'B1'],
            ['.', '.', '.'],
            ['.', 'K2', '.'],
        ]
        x, y = 2, 1

        self.assertFalse(cls.place_without_harming(x, y, 'K2'))

    def test_piece_can_be_placed_on_board_on_in_danger_place(self):
        cls = HarmlessChess()
        cls.board_size_x = 3
        cls.board_size_y = 3
        cls.board = [
            ['K1', '.', 'B1'],
            ['.', '.', '.'],
            ['.', '.', '.'],
        ]
        x, y = 2, 0

        self.assertFalse(cls.place_without_harming(x, y, 'K2'))

    def test_make_board_of_a_combination_of_pieces(self):
        cls = HarmlessChess()
        cls.board_size_x = 3
        cls.board_size_y = 3
        combination = ['K1', 'K2', 'R1']
        expected_result = [
            ['K1', '.', 'K2'],
            ['.', '.', '.'],
            ['.', 'R1', '.']
        ]

        while True:
            if cls.make_board(combination):
                break
        self.assertEqual(cls.board, expected_result)

    def test_remove_duplicates(self):
        cls = HarmlessChess()
        cls.board_size_x = 3
        cls.board_size_y = 3
        cls.boards = [
            [
                ['K1', '.', 'K2'],
                ['.', '.', '.'],
                ['.', 'R1', '.'],
            ],
            [
                ['K1', '.', '.'],
                ['.', '.', 'R1'],
                ['K2', '.', '.'],
            ]
        ]

        expected_result = [
            [
                ['K', '.', 'K'],
                ['.', '.', '.'],
                ['.', 'R', '.'],
            ],
            [
                ['K', '.', '.'],
                ['.', '.', 'R'],
                ['K', '.', '.'],
            ],
            [
                ['.', '.', 'K'],
                ['R', '.', '.'],
                ['.', '.', 'K'],
            ]
        ]

        self.assertEqual(cls.remove_duplicates_and_add_missing_boards(),
                         expected_result)

    @patch('chess.raw_input', return_value=1)   # pragma: no cover
    def test_user_input(self, return_ans):
        cls = HarmlessChess()

        self.assertEqual(cls.bishops, 0)
        self.assertEqual(cls.kings, 0)
        self.assertEqual(cls.knights, 0)

        cls.get_user_input()

        self.assertEqual(cls.bishops, 1)
        self.assertEqual(cls.kings, 1)
        self.assertEqual(cls.knights, 1)

    @patch('chess.HarmlessChess.get_user_input')
    @patch('chess.HarmlessChess.__init__', return_value=None)
    def test_main_program_execution(self, a, b):
        cls = HarmlessChess()

        cls.board_size_x = 3
        cls.board_size_y = 3

        cls.bishops = 0
        cls.knights = 0
        cls.rooks = 1
        cls.queens = 0
        cls.kings = 2
        cls.board = []
        cls.boards = []
        cls.pieces = []

        cls.main()

        boards = [
            [
                ['K', '.', 'K'],
                ['.', '.', '.'],
                ['.', 'R', '.']
            ],
            [
                ['.', 'R', '.'],
                ['.', '.', '.'],
                ['K', '.', 'K']
            ],
            [
                ['K', '.', '.'],
                ['.', '.', 'R'],
                ['K', '.', '.']
            ],
            [
                ['.', '.', 'K'],
                ['R', '.', '.'],
                ['.', '.', 'K']
            ]
        ]
        self.assertItemsEqual(cls.final_boards, boards)

if __name__ == '__main__':
    unittest.main()