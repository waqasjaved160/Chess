"""
    Author: Waqas Javed
    Description: This module will list all chess moves provided the board size
                 and number of each chess piece without harming any piece on
                 the board
"""
import math
import time
from random import random

import constants


class HarmlessChess(object):

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
        self.combination_of_pieces = []

    def make_combinations_of_pieces(self):
        """
            We will make all the combination of pieces they can be arranged
            in a list using n! (factorial) method. Each of this combination
            can then be used to form a board
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

        total_combinations = math.factorial(len(self.pieces))
        print "Total combinations: %d" % total_combinations
        print "start: %s" % time.time()
        while True:
            combination = sorted(self.pieces, key=lambda x: random())
            print "combination: %s at time: %s" % (str(combination),
                                                   time.time())
            if combination not in self.combination_of_pieces:
                self.combination_of_pieces.append(combination)
            print "Length of combination of pieces %d" % len(
                self.combination_of_pieces)
            if len(self.combination_of_pieces) == total_combinations:
                break

    def initialize_board(self):
        """
            Just placing . (dot) to all places on the board
        """
        self.board = [
            ['.'] * self.board_size_x for _ in range(self.board_size_x)]

    def is_empty(self, x, y):
        """
            If place isn't occupied by any piece
        """
        return self.board[x][y] == "."

    def check_for_rook(self, x, y, piece):
        """
            Need to check two things:
             - if the element to be inserted is not rook then there
                should be no rook or queen on same row or column
             - if the element to be inserted is rook there should be
                no element on same row/column
        :param x:
        :param y:
        :param piece: piece to be inserted at position x,y
        """

        if constants.ROOK in piece:
            for i in xrange(self.board_size_x):
                # Check on x axis on same row as piece to be placed
                if self.board[i][y] != ".":
                    return False
            for i in xrange(self.board_size_x):
                # Check on y axis on same row as piece to be placed
                if self.board[x][i] != ".":
                    return False
        else:
            for i in xrange(self.board_size_x):
                # Check on x axis on same row as piece to be placed
                if (constants.ROOK in self.board[i][y] or
                        constants.QUEEN in self.board[i][y]):
                    return False
            for i in xrange(self.board_size_x):
                # Check on y axis on same row as piece to be placed
                if (constants.ROOK in self.board[x][i] or
                        constants.QUEEN in self.board[x][i]):
                    return False
        return True

    def check_for_bishop(self, x, y):
        for i in xrange(self.board_size_x):
            for j in xrange(self.board_size_y):
                if (self.is_empty(abs(j - y), abs(i - x)) and
                        abs(j - y) == abs(i - x) and
                        constants.BISHOP in self.board[abs(j - y)][abs(i - x)]):
                    return False
        return True

    def check_for_knight(self, x, y):
        """
            1 - If piece to be inserted is knight then there should not be
                any rook or queen on that row / column (for this this method
                should be called after check_for_rook())
            2 - If piece to be inserted is knight then it should not be in
                harm by any other knight
            3 - By inserting this piece no other piece should be in harm
        :param x: Position on horizontal rows
        :param y: Position on vertical rows
        :return:
        """
        for j in xrange(self.board_size_x):
            for i in xrange(self.board_size_y):
                if (abs(j - y) ** 2 + abs(i - x) ** 2 == 5 and
                        constants.KNIGHT in self.board[j][i]):
                    return False
        return True

    def check_for_king(self, x, y, piece):
        """
            Check if there is any king around this x,y points
        :return: False if king is present else True
        """
        for j in xrange(self.board_size_x):
            for i in xrange(self.board_size_y):
                if abs(j - y) < 2 and abs(i - x) < 2:
                    if j == x and i == y:
                        continue
                    elif (self.board[j][i] != "." and
                            constants.ROOK not in self.board[j][i] and
                            constants.KNIGHT not in self.board[j][i]):
                        return False
        return True

    def in_danger(self, x, y, piece):
        """
            Checks whether its safe to place the piece on specific
            position on board
        :param x: Position on horizontal row
        :param y: Position on vertical row
        :param piece:
        :return: True if in Danger else False
        """
        rook = self.check_for_rook(x, y, piece)
        bishop = self.check_for_bishop(x, y)
        knight = self.check_for_knight(x, y)
        king = self.check_for_king(x, y, piece)

        # Queen has powers of both Rook and Bishop

        print "Allowed by Rook: %s, Bishop: %s, Knight: %s, King: %s" % (
            str(rook), str(bishop), str(knight), str(king))
        print "Will this piece be in danger: %s" % str(
            not (rook & bishop & knight & king))
        return not (rook & bishop & knight & king)

    def place_without_harming(self, x, y, piece):
        """
            Move a chess piece to position x,y
        :param x: position on board on horizontal axis
        :param y: position on board on vertical axis
        :param piece: Chess piece
        :return: Boolean (True if piece is placed False otherwise)
        """
        if self.board[x][y] != '.':
            # Place is already occupied
            return False

        print "Checking for in danger piece at %d,%d" % (x, y)

        if not self.in_danger(x, y, piece):
            self.board[x][y] = piece
            print "%s placed at board[%d][%d]" % (piece, x, y)
            print "Board position: %s" % str(self.board)
            return True

        print "Piece found to be in danger at %d,%d" % (y, x)
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

        print "Board initialized: %s" % self.board

        for piece in combination:
            print "Checking for piece: %s" % piece
            for x in xrange(self.board_size_x):
                for y in xrange(self.board_size_y):
                    print "x,y: %d,%d" % (x, y)
                    if self.place_without_harming(x, y, piece):
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

        # self.make_combinations_of_pieces()
        # print self.combination_of_pieces

        # for combination in self.combination_of_pieces:
        #     print "Combination: %s" % str(combination)
        #     if self.make_board(combination):
        #         print "All pieces places on board %s" % str(self.board)
        #         self.boards.append(self.board)
        if self.make_board(['R1', 'N3', 'N1', 'R2', 'N4', 'N2']):
            self.boards.append(self.board)
        # print self.boards
        for board in self.boards:
            for x in board:
                print x
            print "-" * 25

        print "Total boards: %d" % len(self.boards)

if __name__ == '__main__':
    cls = HarmlessChess()
    cls.main()
