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

        self.make_combinations_of_pieces()
        print self.combination_of_pieces

if __name__ == '__main__':
    cls = HarmlessChess()
    cls.main()
