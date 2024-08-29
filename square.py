class EmptySquare:

    def __init__(self) -> None:
        self.iswhite = None
        self.moved = None
        self.value = 0
        self.image = "images/Clear.png"

    def __str__(self) -> str:
        return '.'
    
    def possible_move(start, end):
        return False


class Square:

    def __init__(self, x, y, piece = EmptySquare()) -> None:

        self.x = x
        self.y = y
        self.piece = piece
        
    def __repr__(self) -> str:
        if self.piece == None:
            return '.'
        return self.piece.__str__()