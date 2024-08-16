from square import Square
from pieces import *

class Board:

    board = []

    def create_board():

        line = [Square(0, 0 ,Rook(True)),
                Square(0, 1 ,Knight(True)),
                Square(0, 2 ,Bishop(True)),
                Square(0, 3 ,King(True)),
                Square(0, 4 ,Queen(True)),
                Square(0, 5 ,Bishop(True)),
                Square(0, 6 ,Knight(True)),
                Square(0, 7 ,Rook(True))]
        Board.board.append(line)

        line = []
        for i in range(8):
            line.append(Square(1, i, Pawn(True)))
        Board.board.append(line)

        for i in range(2, 6):
            line = []
            for j in range(8):
                line.append(Square(i, j))

            Board.board.append(line)

        line = []
        for i in range(8):
            line.append(Square(6, i, Pawn(False)))
        Board.board.append(line)

        line = [Square(7, 0 ,Rook(False)),
                Square(7, 1 ,Knight(False)),
                Square(7, 2 ,Bishop(False)),
                Square(7, 3 ,King(False)),
                Square(7, 4 ,Queen(False)),
                Square(7, 5 ,Bishop(False)),
                Square(7, 6 ,Knight(False)),
                Square(7, 7 ,Rook(False))]
        Board.board.append(line)

        
    def print_board():

        for x in Board.board:
            for y in x:
                print(y, end=' ')
            print()

    def board_value():
        """
        Returns value advantage of the board
        If positive, white has the advantage
        If negative, black has the advantage
        Else, the value is equal
        """

        value = 0
        for x in Board.board:
            for y in x:
                value += y.piece.value
        return value

def main():
    Board.create_board()
    Board.print_board()
    print(Board.board_value())

if __name__ == "__main__":
    main()