from chess import *
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.graphics import *
from functools import partial
from kivy.properties import StringProperty, ListProperty

Board.create_board()


class BoardGrid(GridLayout):

    iswhite = True
    selected = False
    s_x = None
    s_y = None
    
    s00 = StringProperty(Board.board[0][0].piece.image)
    s01 = StringProperty(Board.board[0][1].piece.image)
    s02 = StringProperty(Board.board[0][2].piece.image)
    s03 = StringProperty(Board.board[0][3].piece.image)
    s04 = StringProperty(Board.board[0][4].piece.image)
    s05 = StringProperty(Board.board[0][5].piece.image)
    s06 = StringProperty(Board.board[0][6].piece.image)
    s07 = StringProperty(Board.board[0][7].piece.image)

    s10 = StringProperty(Board.board[1][0].piece.image)
    s11 = StringProperty(Board.board[1][1].piece.image)
    s12 = StringProperty(Board.board[1][2].piece.image)
    s13 = StringProperty(Board.board[1][3].piece.image)
    s14 = StringProperty(Board.board[1][4].piece.image)
    s15 = StringProperty(Board.board[1][5].piece.image)
    s16 = StringProperty(Board.board[1][6].piece.image)
    s17 = StringProperty(Board.board[1][7].piece.image)

    s20 = StringProperty(Board.board[2][0].piece.image)
    s21 = StringProperty(Board.board[2][1].piece.image)
    s22 = StringProperty(Board.board[2][2].piece.image)
    s23 = StringProperty(Board.board[2][3].piece.image)
    s24 = StringProperty(Board.board[2][4].piece.image)
    s25 = StringProperty(Board.board[2][5].piece.image)
    s26 = StringProperty(Board.board[2][6].piece.image)
    s27 = StringProperty(Board.board[2][7].piece.image)

    s30 = StringProperty(Board.board[3][0].piece.image)
    s31 = StringProperty(Board.board[3][1].piece.image)
    s32 = StringProperty(Board.board[3][2].piece.image)
    s33 = StringProperty(Board.board[3][3].piece.image)
    s34 = StringProperty(Board.board[3][4].piece.image)
    s35 = StringProperty(Board.board[3][5].piece.image)
    s36 = StringProperty(Board.board[3][6].piece.image)
    s37 = StringProperty(Board.board[3][7].piece.image)

    s40 = StringProperty(Board.board[4][0].piece.image)
    s41 = StringProperty(Board.board[4][1].piece.image)
    s42 = StringProperty(Board.board[4][2].piece.image)
    s43 = StringProperty(Board.board[4][3].piece.image)
    s44 = StringProperty(Board.board[4][4].piece.image)
    s45 = StringProperty(Board.board[4][5].piece.image)
    s46 = StringProperty(Board.board[4][6].piece.image)
    s47 = StringProperty(Board.board[4][7].piece.image)

    s50 = StringProperty(Board.board[5][0].piece.image)
    s51 = StringProperty(Board.board[5][1].piece.image)
    s52 = StringProperty(Board.board[5][2].piece.image)
    s53 = StringProperty(Board.board[5][3].piece.image)
    s54 = StringProperty(Board.board[5][4].piece.image)
    s55 = StringProperty(Board.board[5][5].piece.image)
    s56 = StringProperty(Board.board[5][6].piece.image)
    s57 = StringProperty(Board.board[5][7].piece.image)

    s60 = StringProperty(Board.board[6][0].piece.image)
    s61 = StringProperty(Board.board[6][1].piece.image)
    s62 = StringProperty(Board.board[6][2].piece.image)
    s63 = StringProperty(Board.board[6][3].piece.image)
    s64 = StringProperty(Board.board[6][4].piece.image)
    s65 = StringProperty(Board.board[6][5].piece.image)
    s66 = StringProperty(Board.board[6][6].piece.image)
    s67 = StringProperty(Board.board[6][7].piece.image)

    s70 = StringProperty(Board.board[7][0].piece.image)
    s71 = StringProperty(Board.board[7][1].piece.image)
    s72 = StringProperty(Board.board[7][2].piece.image)
    s73 = StringProperty(Board.board[7][3].piece.image)
    s74 = StringProperty(Board.board[7][4].piece.image)
    s75 = StringProperty(Board.board[7][5].piece.image)
    s76 = StringProperty(Board.board[7][6].piece.image)
    s77 = StringProperty(Board.board[7][7].piece.image)

    def click(self, x, y):

        if not BoardGrid.selected:
            BoardGrid.s_x = x
            BoardGrid.s_y = y
            BoardGrid.selected = True
        else:
            if turn(BoardGrid.s_x, BoardGrid.s_y, x, y, BoardGrid.iswhite):
                BoardGrid.iswhite = not BoardGrid.iswhite
            BoardGrid.selected = False
            
            self.s00 = (Board.board[0][0].piece.image)
            self.s01 = (Board.board[0][1].piece.image)
            self.s02 = (Board.board[0][2].piece.image)
            self.s03 = (Board.board[0][3].piece.image)
            self.s04 = (Board.board[0][4].piece.image)
            self.s05 = (Board.board[0][5].piece.image)
            self.s06 = (Board.board[0][6].piece.image)
            self.s07 = (Board.board[0][7].piece.image)

            self.s10 = (Board.board[1][0].piece.image)
            self.s11 = (Board.board[1][1].piece.image)
            self.s12 = (Board.board[1][2].piece.image)
            self.s13 = (Board.board[1][3].piece.image)
            self.s14 = (Board.board[1][4].piece.image)
            self.s15 = (Board.board[1][5].piece.image)
            self.s16 = (Board.board[1][6].piece.image)
            self.s17 = (Board.board[1][7].piece.image)

            self.s20 = (Board.board[2][0].piece.image)
            self.s21 = (Board.board[2][1].piece.image)
            self.s22 = (Board.board[2][2].piece.image)
            self.s23 = (Board.board[2][3].piece.image)
            self.s24 = (Board.board[2][4].piece.image)
            self.s25 = (Board.board[2][5].piece.image)
            self.s26 = (Board.board[2][6].piece.image)
            self.s27 = (Board.board[2][7].piece.image)

            self.s30 = (Board.board[3][0].piece.image)
            self.s31 = (Board.board[3][1].piece.image)
            self.s32 = (Board.board[3][2].piece.image)
            self.s33 = (Board.board[3][3].piece.image)
            self.s34 = (Board.board[3][4].piece.image)
            self.s35 = (Board.board[3][5].piece.image)
            self.s36 = (Board.board[3][6].piece.image)
            self.s37 = (Board.board[3][7].piece.image)

            self.s40 = (Board.board[4][0].piece.image)
            self.s41 = (Board.board[4][1].piece.image)
            self.s42 = (Board.board[4][2].piece.image)
            self.s43 = (Board.board[4][3].piece.image)
            self.s44 = (Board.board[4][4].piece.image)
            self.s45 = (Board.board[4][5].piece.image)
            self.s46 = (Board.board[4][6].piece.image)
            self.s47 = (Board.board[4][7].piece.image)

            self.s50 = (Board.board[5][0].piece.image)
            self.s51 = (Board.board[5][1].piece.image)
            self.s52 = (Board.board[5][2].piece.image)
            self.s53 = (Board.board[5][3].piece.image)
            self.s54 = (Board.board[5][4].piece.image)
            self.s55 = (Board.board[5][5].piece.image)
            self.s56 = (Board.board[5][6].piece.image)
            self.s57 = (Board.board[5][7].piece.image)

            self.s60 = (Board.board[6][0].piece.image)
            self.s61 = (Board.board[6][1].piece.image)
            self.s62 = (Board.board[6][2].piece.image)
            self.s63 = (Board.board[6][3].piece.image)
            self.s64 = (Board.board[6][4].piece.image)
            self.s65 = (Board.board[6][5].piece.image)
            self.s66 = (Board.board[6][6].piece.image)
            self.s67 = (Board.board[6][7].piece.image)

            self.s70 = (Board.board[7][0].piece.image)
            self.s71 = (Board.board[7][1].piece.image)
            self.s72 = (Board.board[7][2].piece.image)
            self.s73 = (Board.board[7][3].piece.image)
            self.s74 = (Board.board[7][4].piece.image)
            self.s75 = (Board.board[7][5].piece.image)
            self.s76 = (Board.board[7][6].piece.image)
            self.s77 = (Board.board[7][7].piece.image)

    def __init__(self, **kwargs):

        super().__init__(**kwargs)
        self.cols = 8

class ChessApp(App):
    pass

ChessApp().run()