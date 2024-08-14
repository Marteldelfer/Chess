from pieces import *

columns = {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5, 'f' : 6, 'g' : 7, 'h' : 8}

p1 = Pawn(True, 2, 1)
p2 = Pawn(True, 2, 2)
p3 = Pawn(True, 2, 3)
p4 = Pawn(True, 2, 4)
p5 = Pawn(True, 2, 5)
p6 = Pawn(True, 2, 6)
p7 = Pawn(True, 2, 7)
p8 = Pawn(True, 2, 8)


board = [[ p1, p2, p3, p4, p5, p6, p7, p8],
         ['.','.','.','.','.','.','.','.'],
         ['.','.','.','.','.','.','.','.'],
         ['.','.','.','.','.','.','.','.'],
         ['.','.','.','.','.','.','.','.']]