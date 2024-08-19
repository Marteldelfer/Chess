from square import *
from pieces import *

def board_range(num):

    if num > 1:
        return range(1, num)
    if num < 0:
        return range(-1, num, -1)

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
        for i in board_range(x):
            if not isinstance(Board.board[start.x + i][start.y].piece, EmptySquare):
                return False
        return True
    
    #Else, moving in the same line
    for i in board_range(y):
        if not isinstance(Board.board[start.x][start.y + i].piece, EmptySquare):
            return False
    return True

def has_path_bishop(start : Square, end : Square):
    """Same as the has_path_rook, but for the bishop"""

    if not start.piece.possible_move(start, end):
        return False
    
    x = end.x - start.x 
    y = end.y - start.y

    #Using zip because x and y absolute values are the same
    for i, j in zip(board_range(x), board_range(y)):
        if not isinstance(Board.board[start.x + i][start.y + j].piece, EmptySquare):
            return False
    return True


def pawn_can_capture(start : Square, end : Square):

    x = end.x - start.x
    y = abs(end.y - start.y)

    if not isinstance(end.piece, EmptySquare) and start.piece.iswhite != end.piece.iswhite:
        if start.piece.iswhite and x == 1 and y == 1:
            return True
        elif not start.piece.iswhite and x == -1 and y == 1:
            return True
    return False

def move_piece(start: Square, end: Square):

    # Move the rook
    if isinstance(start.piece, Rook):
        if has_path_rook(start, end):
            start.piece.moved = True
            Board.board[end.x][end.y].piece = start.piece
            Board.board[start.x][start.y] = Square(start.x, start.y)
            return True

    # Move the bishop
    elif isinstance(start.piece, Bishop):
        if has_path_bishop(start, end):
            Board.board[end.x][end.y].piece = start.piece
            Board.board[start.x][start.y] = Square(start.x, start.y)
            return True

    # Move the queen
    elif isinstance(start.piece, Queen):
        if has_path_rook(start, end) or has_path_bishop(start, end):
            Board.board[end.x][end.y].piece = start.piece
            Board.board[start.x][start.y] = Square(start.x, start.y)
            return True

    # Move the King
    elif isinstance(start.piece, King):
        if start.piece.possible_move(start, end):
            start.piece.moved = True
            Board.board[end.x][end.y].piece = start.piece
            Board.board[start.x][start.y] = Square(start.x, start.y)
            return True

    # Move the knight
    elif isinstance(start.piece, Knight):
        if start.piece.possible_move(start, end):
            Board.board[end.x][end.y].piece = start.piece
            Board.board[start.x][start.y] = Square(start.x, start.y)
            return True

    # Move the pawn
    elif isinstance(start.piece, Pawn):
        if start.piece.possible_move(start, end) or pawn_can_capture(start, end):
            start.piece.moved = True
            Board.board[end.x][end.y].piece = start.piece
            Board.board[start.x][start.y] = Square(start.x, start.y)
            return True
    return False


def main():
    Board.create_board()

    Board.board[1][0] = Square(1,0)
    Board.board[1][3] = Square(1,3)
    Board.board[6][3] = Square(6,3)
    Board.board[6][1] = Square(6,1)
    Board.print_board()

    b = Board.board

if __name__ == "__main__":
    main()