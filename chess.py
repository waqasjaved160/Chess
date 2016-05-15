"""
    Author: Waqas Javed
    Description: This module will list all chess moves provided the board size
                 and number of each chess piece without harming any piece on
                 the board
"""
import time
from random import random, randint

import constants


def display_boards(boards):
    """
        Given list of boards this handy function will print in
        a readable (matrix) form
    :param boards: List of boards
    """
    for row_list in boards:
        for row in row_list:
            print row
        print "-" * 25


def display_board(board):
    """
        Given a single board this handy function will print in
        a readable (matrix) form
    :param board: List of rows containing chess pieces
    """
    for row_list in board:
        print row_list


class HarmlessChess(object):
    """
        Class for holding all methods required for Harmless Chess
    """

    def __init__(self):
        self.board_size_x = 0
        self.board_size_y = 0
        self.bishops = 0
        self.knights = 0
        self.rooks = 0
        self.queens = 0
        self.kings = 0
        self.board = []
        self.boards = []
        self.pieces = []

    def make_list_of_pieces(self):
        """
            All the pieces entered are added in a list with
            a suffix added as a number to differentiate them
        :return: List of lists
        """
        for index, _ in enumerate(xrange(self.bishops), 1):
            self.pieces.append("%s%d" % (constants.BISHOP, index))

        for index, _ in enumerate(xrange(self.knights), 1):
            self.pieces.append("%s%d" % (constants.KNIGHT, index))

        for index, _ in enumerate(xrange(self.rooks), 1):
            self.pieces.append("%s%d" % (constants.ROOK, index))

        for index, _ in enumerate(xrange(self.queens), 1):
            self.pieces.append("%s%d" % (constants.QUEEN, index))

        for index, _ in enumerate(xrange(self.kings), 1):
            self.pieces.append("%s%d" % (constants.KING, index))

        print "All pieces: %s" % str(self.pieces)

    def initialize_board(self):
        """
            Just placing . (dot) to all places on the board
        """
        self.board = [
            ['.'] * self.board_size_x for _ in range(self.board_size_x)]

    def check_for_rook(self, pos_x, pos_y, piece):
        """
            Need to check two things:
             - if the element to be inserted is not rook then there
                should be no rook or queen on same row or column
             - if the element to be inserted is rook there should be
                no element on same row/column
        :param pos_x: iterable on lists
        :param pos_y: iterable on items of a list
        :param piece: piece to be inserted at position x,y
        """

        if constants.ROOK in piece:
            for i in xrange(self.board_size_x):
                # Check on x/y axis on same row/col as piece to be placed
                if self.board[i][pos_y] != "." or self.board[pos_x][i] != ".":
                    return False
        else:
            for i in xrange(self.board_size_x):
                # Check on x axis on same row as piece to be placed
                if (constants.ROOK in self.board[i][pos_y] or
                        constants.QUEEN in self.board[i][pos_y] or
                        constants.ROOK in self.board[pos_x][i] or
                        constants.QUEEN in self.board[pos_x][i]):
                    return False
        return True

    def check_for_bishop(self, pos_x, pos_y, piece):
        """
            Need to check two things here:
             - If the piece to be inserted is Bishop then there should
               be no element in its range
             - If the piece to be inserted is not Bishop then there this
               piece should not be in the way of any Bishop present
        :param piece:
        :param pos_x: iterable on lists
        :param pos_y: iterable on items of a list
        :return: Boolean
        """
        for i in xrange(self.board_size_x):
            for j in xrange(self.board_size_y):
                if abs(j - pos_y) == abs(i - pos_x):
                    # We only need to check diagonally for Bishop
                    # if constants.BISHOP in self.board[i][j]:
                    if self.board[i][j] != '.' and constants.BISHOP in piece:
                        return False
                    elif constants.BISHOP in self.board[i][j]:
                        return False
        return True

    def check_for_queen(self, pos_x, pos_y, piece):
        """
            Need to check following things:
             - (Condition for Bishop) If queen is to be inserted then there
               should not be any element diagonally to queen
             - If piece to be inserted is not queen then that piece should
               not be in range of any queen present
             - (Condition for Rook) If queen is to be inserted then there
               should not be any piece horizontally or vertically of the queen
             - If piece to be inserted is not queen then this piece should
               not be in range of any queen horizontally or vertically
        :param pos_x: position on lists
        :param pos_y: position on item of a list
        :param piece: piece to be inserted
        :return: Boolean (True if piece can be inserted)
        """
        for i in xrange(self.board_size_x):
            for j in xrange(self.board_size_y):
                if abs(j - pos_y) == abs(i - pos_x):
                    # We only need to check diagonally for Queen
                    if self.board[i][j] != '.' and constants.QUEEN in piece:
                        return False
                    elif constants.QUEEN in self.board[i][j]:
                        return False

        if constants.QUEEN in piece:
            for i in xrange(self.board_size_x):
                # Check on x / y axis on same row / col as piece to be placed
                if self.board[i][pos_y] != "." or self.board[pos_x][i] != ".":
                    return False
        else:
            for i in xrange(self.board_size_x):
                # Check on x axis on same row as piece to be placed
                if (constants.ROOK in self.board[i][pos_y] or
                        constants.QUEEN in self.board[i][pos_y] or
                        # Check on y axis on same row as piece to be placed
                        constants.ROOK in self.board[pos_x][i] or
                        constants.QUEEN in self.board[pos_x][i]):
                    return False

        return True

    def check_for_knight(self, pos_x, pos_y, piece):
        """
            1 - If piece to be inserted is knight then there should not be
                any rook or queen on that row / column (for this this method
                should be called after check_for_rook())
            2 - If piece to be inserted is knight then it should not be in
                harm by any other knight
            3 - By inserting this piece no other piece should be in harm
        :param pos_x: Position on horizontal rows
        :param pos_y: Position on vertical rows
        :param piece: Piece to be inserted
        :return:
        """
        # Checking if piece to be inserted is Knight and it is not
        # harming any piece which will be in its range if it's inserted
        for j in xrange(self.board_size_x):
            for i in xrange(self.board_size_y):
                if abs(j - pos_x) ** 2 + abs(i - pos_y) ** 2 == 5:
                    if (self.board[j][i] != '.' and
                            (constants.KNIGHT in piece or
                             constants.KNIGHT in self.board[j][i])):
                        return False
        return True

    def check_for_king(self, pos_x, pos_y, piece):
        """
            Check if there is any king around this x,y points
        :return: False if king is present else True
        """
        for j in xrange(self.board_size_x):
            for i in xrange(self.board_size_y):
                # We need to check only on those squares that are
                # in reach of a king
                if abs(j - pos_x) < 2 and abs(i - pos_y) < 2:
                    if j == pos_x and i == pos_y:
                        # Square at which we need to place the piece
                        # its empty and already checked so we can skip
                        continue
                    # If the piece to be inserted is king then there
                    # should not be any piece in its range
                    elif self.board[j][i] != "." and constants.KING in piece:
                        return False
                    elif constants.KING in self.board[j][i]:
                        return False
        return True

    def in_danger(self, pos_x, pos_y, piece):
        """
            Checks whether its safe to place the piece on specific
            position on board
        :param pos_x: Position on horizontal row
        :param pos_y: Position on vertical row
        :param piece:
        :return: True if in Danger else False
        """
        rook = self.check_for_rook(pos_x, pos_y, piece)
        bishop = self.check_for_bishop(pos_x, pos_y, piece)
        knight = self.check_for_knight(pos_x, pos_y, piece)
        king = self.check_for_king(pos_x, pos_y, piece)
        queen = self.check_for_queen(pos_x, pos_y, piece)

        return not rook & bishop & knight & king & queen

    def place_without_harming(self, pos_x, pos_y, piece):
        """
            Move a chess piece to position x,y
        :param pos_x: position on board on horizontal axis
        :param pos_y: position on board on vertical axis
        :param piece: Chess piece
        :return: Boolean (True if piece is placed False otherwise)
        """
        if self.board[pos_x][pos_y] != '.':
            # Place is already occupied
            return False

        if not self.in_danger(pos_x, pos_y, piece):
            self.board[pos_x][pos_y] = piece
            return True

        return False

    def make_board(self, combination):
        """
            Given a combination of pieces (list) this method will try
            to make a board of it
        :param combination: List of pieces
        :return: Boolean (True if board if formed False otherwise)
        """
        piece_placed = False
        self.initialize_board()

        random_start_index = randint(0, self.board_size_x)

        for piece in combination:

            for pos_x in xrange(self.board_size_x):
                for pos_y in xrange(self.board_size_y):

                    if not pos_y >= random_start_index and pos_x == 0:
                        # For only first row of the board the place of first
                        # piece is made random so that position (0,0) of the
                        # board can be left vacant and other combinations
                        # can be made
                        continue

                    if self.place_without_harming(pos_x, pos_y, piece):
                        piece_placed = True
                        break

                if piece_placed:
                    piece_placed = False
                    break

        # Return True if all pieces from combination are present
        # on board else return False
        for piece in combination:
            if any(piece in x_row for x_row in self.board):
                continue
            else:
                return False
        return True

    def main(self):
        """
            Program execution starts from this method
             - User is asked the board size
             - User is asked about the number of pieces to be placed
               on this board
             - At the end all the boards formed from these pieces,
               their count and total execution time are displayed
        """

        while True:
            try:
                self.board_size_x = int(
                    raw_input("Please type the X size of board : "))
                self.board_size_y = int(
                    raw_input("Please type the Y size of board : "))
                print "Size of board is %sx%s" % (
                    self.board_size_x, self.board_size_y)
                break
            except ValueError:
                print "Size can only be in integer"

        while True:
            try:
                self.bishops = int(raw_input("Number of Bishops: "))
                self.knights = int(raw_input("Number of Knights: "))
                self.rooks = int(raw_input("Number of Rooks: "))
                self.queens = int(raw_input("Number of Queens: "))
                self.kings = int(raw_input("Number of Kings: "))
                print "Bishops: %d, Knights: %d, Rooks: %d" % (
                    self.bishops, self.knights, self.rooks)
                print "Queens: %d, Kings: %d" % (self.queens, self.kings)
                break
            except ValueError:
                print "Number can only be an integer"

        self.make_list_of_pieces()

        tries = 0
        total_tries = 0
        start_time = time.time()

        items = sorted(self.pieces, key=lambda k: random())

        while True:
            if self.make_board(items):
                self.boards.append(self.board)
                items = sorted(self.pieces, key=lambda k: random())
            elif tries >= 100:
                items = sorted(self.pieces, key=lambda k: random())
                tries = 0
                total_tries += 1
            else:
                tries += 1

            if total_tries >= 19:
                break

        no_duplicates = self.remove_duplicates_and_add_missing_boards()

        display_boards(no_duplicates)
        print "Total time taken: %d" % int(time.time() - start_time)

        print "Total boards: %d" % len(no_duplicates)

    def remove_duplicates_and_add_missing_boards(self):
        """
            - Integers appended will be removed
            - Duplicate boards will be removed
            - Missing boards will be added by matrix manipulation
        :return:
        """
        # Removing appended numbers from pieces
        unique_boards = list()
        for board in self.boards:
            unique_board = list()
            for item_list in board:
                for index, item in enumerate(item_list):
                    item_list[index] = item if item == '.' else item[0]
                unique_board.append(item_list)
            unique_boards.append(unique_board)

        # Removing any duplicates present
        no_duplicates = list()
        for board in unique_boards:
            if board not in no_duplicates:
                no_duplicates.append(board)

        new_boards = list()

        # Reversing the matrix
        for board in no_duplicates:
            another = list()
            for item_list in board:
                another.append(item_list[::-1])
            new_boards.append(another)

        # Appending reversed boards if they don't exist yet
        for board in new_boards:
            if board not in no_duplicates:
                no_duplicates.append(board)

        return no_duplicates


if __name__ == '__main__':
    chess = HarmlessChess()
    chess.main()
