from pieces import *
from square import *
from board import *

def input_decoder(inp : str):
    """Decodes the input and turns into start and end Squares"""

    dec = {"a" : 0, "b" : 1, "c" : 2, "d" : 3,
           "e" : 4, "f" : 5, "g" : 6, "h" : 7}

    inp = list(inp)
    inp[0], inp[2] = dec[inp[0]], dec[inp[2]]
    inp[1], inp[3] = int(inp[1]) - 1, int(inp[3]) - 1

    return Board.board[inp[0]][inp[1]], Board.board[inp[2]][inp[3]]


def check_for_check(iswhite : bool) -> bool:

    #find the king
    for line in Board.board:
        for square in line:
            if isinstance(square.piece, King) and square.piece.iswhite == iswhite:
                king_square = square

    #check if any piece has a path to the king
    for line in Board.board:
        for square in line:
            if square.piece.iswhite == king_square.piece.iswhite or isinstance(square.piece, EmptySquare):
                continue
            if isinstance(square.piece, Rook):
                if has_path_rook(square, king_square):
                    return True
            elif isinstance(square.piece, Bishop):
                if has_path_bishop(square, king_square):
                    return True
            elif isinstance(square.piece, Queen):
                if has_path_bishop(square, king_square) or has_path_rook(square, king_square):
                    return True
            elif isinstance(square.piece, King):
                if square.piece.possible_move(square, king_square):
                    return True
            elif isinstance(square.piece, Knight):
                if square.piece.possible_move(square, king_square):
                    return True
            elif isinstance(square.piece, Pawn):
                if pawn_can_capture(square, king_square):
                    return True
    return False


def end_turn(iswhite : bool) -> None:

    for line in Board.board:
        for square in line:
            if square.piece.iswhite != iswhite and isinstance(square.piece, Pawn):
                square.piece.en_passantable = False

def turn(x1 ,y1, x2, y2, iswhite):

    start : Square = Board.board[x1][y1]
    end : Square = Board.board[x2][y2]

    if start.piece.iswhite == iswhite:
        if move_piece(start, end):

            #if move creates check in it's own king, it's ilegal
            if check_for_check(iswhite):
                Board.print_board()
                print()
                #Reverses the movement
                Board.board[start.x][start.y].piece = Board.board[end.x][end.y].piece
                Board.board[end.x][end.y] = Square(end.x, end.y)
                Board.print_board()
                print("is in check")
                print()
                return False
            
            end_turn(iswhite)
            return True
    Board.print_board()
    return False

        
    

def main():
    Board.create_board()
    Board.print_board()

    turn(True)

if __name__ == "__main__":
    main()