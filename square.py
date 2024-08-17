class EmptySquare:

    value = 0

    def __str__(self) -> str:
        return '.'
    
    def possible_move(start, end):
        return False

    def iswhite():
        return None

class Square:

    def __init__(self, x, y, piece = EmptySquare()) -> None:

        self.x = x
        self.y = y
        self.piece = piece
        
    def __repr__(self) -> str:
        if self.piece == None:
            return '.'
        return self.piece.__str__()