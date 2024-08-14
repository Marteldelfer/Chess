class Piece:

    def __init__(self, iswhite, line, col) -> None:

        self.iswhite = iswhite
        self.moved = False
        self.targeted = False
        self.line = line
        self.col = col
        self.possible_moves = []

class Pawn(Piece):

    def __init__(self, iswhite) -> None:
        super().__init__(iswhite)

    def get_possible_moves(self):
        
        self.possible_moves = []

        #move forward twice if haven't moved
        if not self.moved:
            self.possible_moves.append(str(self.col) + str(self.line + 2))
        
        #move foward normally
        self.possible_moves.append(str(self.col) + str(self.line + 1))

        # TODO implement capture and en passent




