from square import Square
from pieces import *

class Board:

    board = []

    def create_board():

        line = [Square(0, 0 ,Rook(True)),
                Square(0, 1 ,Knight(True)),
                Square(0, 2 ,Bishop(True)),
                Square(0, 3 ,Queen(True)),
                Square(0, 4 ,King(True)),
                Square(0, 5 ,Bishop(True)),
                Square(0, 6 ,Knight(True)),
                Square(0, 7 ,Rook(True))]
        Board.board.append(line)

        line = []
        for i in range(8):
            line.append(Square(6, i, Pawn(True)))
        Board.board.append(line)

        for i in range(2, 6):
            line = []
            for j in range(8):
                line.append(Square(i, j))

            Board.board.append(line)

    def print_board():

        for x in Board.board:
            for y in x:
                print(y, end=' ')
            print()

Board.create_board()
Board.print_board()