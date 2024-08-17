from square import Square

class Piece:

    def __init__(self, iswhite) -> None:

        self.iswhite = iswhite
        self.moved = False
        self.targeted = False
        self.value = 0
        

class Pawn(Piece):

    def __init__(self, iswhite) -> None:
        super().__init__(iswhite)

        #Set value of the piece
        if self.iswhite:
            self.value = 1
        else:
            self.value = -1

    def __str__(self) -> str:
        if self.iswhite:
            return 'P'
        return 'p'
    
    def possible_move(self, start : Square, end : Square):
        
        #Can't move if the square is ocupied
        if end.piece.iswhite == self.iswhite:
            return False
        
        if start.y != end.y:
            return False

        # Can only move in one direction
        if not self.iswhite:
            if start.x - end.x == 1:
                return True
            # The first move can be two squares
            if start.x - end.x == 2 and not self.moved:
                return True
        else:
            if end.x - start.x == 1:
                return True
            # The first move can be two squares
            if end.x - start.x == 2 and not self.moved:
                return True 
            
        # TODO en passant and capture

        return False


class Bishop(Piece):
    
    def __init__(self, iswhite) -> None:
        super().__init__(iswhite)

        if self.iswhite:
            self.value = 3
        else:
            self.value = -3

    def __str__(self) -> str:
        if self.iswhite:
            return "B"
        return 'b'
    
    def possible_move(self, start : Square, end : Square):

        #Can't move if the square is ocupied
        if end.piece.iswhite == self.iswhite:
            return False
        
        x = abs(start.x - end.x)
        y = abs(start.y - end.y)

        #Can only move on diagonal
        if x == y:
            return True
        return False


class Knight(Piece):
    
    def __init__(self, iswhite) -> None:
        super().__init__(iswhite)

        #Set value of the piece
        if self.iswhite:
            self.value = 3
        else:
            self.value = -3

    def __str__(self) -> str:
        if self.iswhite:
            return 'N'
        return 'n'
    
    def possible_move(self, start: Square, end: Square):
        
        #Can't move if the square is ocupied
        if end.piece.iswhite == self.iswhite:
            return False
        
        x = abs(start.x - end.x)
        y = abs(start.y - end.y)

        # Can only move in a L
        if (x == 2 and y == 1) or (y == 2 and x == 1):
            return True
        return False



class Rook(Piece):
    
    def __init__(self, iswhite) -> None:
        super().__init__(iswhite)

        #Set value of the piece
        if self.iswhite:
            self.value = 5
        else:
            self.value = -5

    def __str__(self) -> str:

        if self.iswhite:
            return 'R'
        return 'r'

    def possible_move(self, start, end):

        #Can't move if the square is ocupied
        if end.piece.iswhite == self.iswhite:
            return False
        
        x = abs(start.x - end.x)
        y = abs(start.y - end.y)

        #Can only move in the same line or column
        if x == 0 or y == 0:
            return True
        return False
    


class Queen(Piece):
    
    def __init__(self, iswhite) -> None:
        super().__init__(iswhite)

        #Set value of the piece
        if self.iswhite:
            self.value = 9
        else:
            self.value = -9

    def __str__(self) -> str:

        if self.iswhite:
            return 'Q'
        return 'q'
    
    def possible_move(self, start : Square, end : Square):

        #Can't move if the square is ocupied
        if end.piece.iswhite:
            return False
        
        x = abs(start.x - end.x)
        y = abs(start.y - end.y)

        #Basically, rook and bishop combined
        if (x == 0 or y == 0) or x == y:
            return True
        return False
    


class King(Piece):
    
    def __init__(self, iswhite) -> None:
        super().__init__(iswhite)

        #Set value of the piece
        if self.iswhite:
            self.value = 100
        else:
            self.value = -100

    def __str__(self) -> str:

        if self.iswhite:
            return 'K'
        return 'k'
    
    def possible_move(self, start: Square, end: Square):
        
        #Can't move if the square is ocupied
        if end.piece.iswhite == self.iswhite:
            return False

        #Check for regular movement
        x = abs(start.x - end.x)
        y = abs(start.y - end.y)

        if x == 1 or y == y:
            return True
        
        # TODO Check for castling

        return False