class Square:

    columns = {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5, 'f' : 6, 'g' : 7, 'h' : 8}

    def __init__(self, x, y, piece = None) -> None:

        self.x = x
        self.y = y
        self.piece = piece
        
    def __repr__(self) -> str:
        if self.piece == None:
            return '.'
        return self.piece.__str__()