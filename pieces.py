class Piece:

    def __init__(self, iswhite) -> None:

        self.iswhite = iswhite
        self.moved = False
        self.targeted = False


class Pawn(Piece):

    def __init__(self, iswhite) -> None:
        super().__init__(iswhite)

    def __str__(self) -> str:
        return 'P'

    def get_possible_moves(self):
        # TODO implement capture and en passent
        pass

class Bishop(Piece):
    
    def __init__(self, iswhite) -> None:
        super().__init__(iswhite)

    def __str__(self) -> str:
        return "B"

class Knight(Piece):
    
    def __init__(self, iswhite) -> None:
        super().__init__(iswhite)

    def __str__(self) -> str:
        return 'N'

class Rook(Piece):
    
    def __init__(self, iswhite) -> None:
        super().__init__(iswhite)

    def __str__(self) -> str:
        return 'R'

class Queen(Rook, Bishop):
    
    def __init__(self, iswhite) -> None:
        super().__init__(iswhite)

    def __str__(self) -> str:
        return 'Q'

class King(Piece):
    
    def __init__(self, iswhite) -> None:
        super().__init__(iswhite)

    def __str__(self) -> str:
        return 'K'