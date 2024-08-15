class EmptySquare:

    def possible_move(self, start, end):
        return False

class Square:

    def __init__(self, x, y, piece = EmptySquare) -> None:

        self.x = x
        self.y = y
        self.piece = piece
        
    def __repr__(self) -> str:
        if self.piece == None:
            return '.'
        return self.piece.__str__()