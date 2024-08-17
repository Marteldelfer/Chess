from square import *
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


def has_path_rook(start: Square, end: Square):
    """
    Function that takes two squares on the board and verify if
    there's a clear path in between them for a rook
    If end square has a piece, it's still considerede a valid
    path, allowing for captures
    """

    #See if is a possible move
    if not start.piece.possible_move(start, end):
        return False

    x = end.x - start.x
    y = end.y - start.y

    #If moving in the same column
    if x != 0:
        for i in range(1, x):
            if not isinstance(Board.board[start.x + i][start.y].piece, EmptySquare):
                print(type(Board.board[start.x + i][start.y].piece))
                return False
        return True
    
    #Else, moving in the same line
    for i in range(1, y):
        if not isinstance(Board.board[start.x][start.y + i].piece, EmptySquare):
            print(type(Board.board[start.x][start.y + i].piece))
            return False
    return True
    
def main():
    Board.create_board()

    Board.board[1][0] = Square(1,0)
    Board.print_board()

    print(has_path_rook(Board.board[0][0], Board.board[6][0]))
if __name__ == "__main__":
    main()