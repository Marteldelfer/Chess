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

def turn():

    inp = input('Type your move: \n')
    start, end = input_decoder(inp)

    move_piece(start, end)
    Board.print_board()

def main():
    Board.create_board()
    Board.print_board()

    while True:
        turn()

if __name__ == "__main__":
    main()