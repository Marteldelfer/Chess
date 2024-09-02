from chess import *
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import *
from kivy.core.window import Window
from kivy.properties import StringProperty, BooleanProperty

Board.create_board()

class ChessGame(BoxLayout):
    pass

class BoardGrid(GridLayout):

    iswhite = True
    ui_iswhite = StringProperty("images/white-king.png")
    selected = False
    s_x = None
    s_y = None

    w, h = Window._get_size()
    print(w, h)

    if w > h:
        board_size = h
    else:
        board_size = w
    print(w, h)
    row_force_default = True
    col_force_default = True
    row_default_height = board_size / 8
    col_default_width = board_size / 8
    
    board_list = [[] for i in range(8)]

    board_list[0].append(s00 := StringProperty(Board.board[0][0].piece.image))
    board_list[0].append(s01 := StringProperty(Board.board[0][1].piece.image))
    board_list[0].append(s02 := StringProperty(Board.board[0][2].piece.image))
    board_list[0].append(s03 := StringProperty(Board.board[0][3].piece.image))
    board_list[0].append(s04 := StringProperty(Board.board[0][4].piece.image))
    board_list[0].append(s05 := StringProperty(Board.board[0][5].piece.image))
    board_list[0].append(s06 := StringProperty(Board.board[0][6].piece.image))
    board_list[0].append(s07 := StringProperty(Board.board[0][7].piece.image))

    board_list[1].append(s10 := StringProperty(Board.board[1][0].piece.image))
    board_list[1].append(s11 := StringProperty(Board.board[1][1].piece.image))
    board_list[1].append(s12 := StringProperty(Board.board[1][2].piece.image))
    board_list[1].append(s13 := StringProperty(Board.board[1][3].piece.image))
    board_list[1].append(s14 := StringProperty(Board.board[1][4].piece.image))
    board_list[1].append(s15 := StringProperty(Board.board[1][5].piece.image))
    board_list[1].append(s16 := StringProperty(Board.board[1][6].piece.image))
    board_list[1].append(s17 := StringProperty(Board.board[1][7].piece.image))

    board_list[2].append(s20 := StringProperty(Board.board[2][0].piece.image))
    board_list[2].append(s21 := StringProperty(Board.board[2][1].piece.image))
    board_list[2].append(s22 := StringProperty(Board.board[2][2].piece.image))
    board_list[2].append(s23 := StringProperty(Board.board[2][3].piece.image))
    board_list[2].append(s24 := StringProperty(Board.board[2][4].piece.image))
    board_list[2].append(s25 := StringProperty(Board.board[2][5].piece.image))
    board_list[2].append(s26 := StringProperty(Board.board[2][6].piece.image))
    board_list[2].append(s27 := StringProperty(Board.board[2][7].piece.image))

    board_list[3].append(s30 := StringProperty(Board.board[3][0].piece.image))
    board_list[3].append(s31 := StringProperty(Board.board[3][1].piece.image))
    board_list[3].append(s32 := StringProperty(Board.board[3][2].piece.image))
    board_list[3].append(s33 := StringProperty(Board.board[3][3].piece.image))
    board_list[3].append(s34 := StringProperty(Board.board[3][4].piece.image))
    board_list[3].append(s35 := StringProperty(Board.board[3][5].piece.image))
    board_list[3].append(s36 := StringProperty(Board.board[3][6].piece.image))
    board_list[3].append(s37 := StringProperty(Board.board[3][7].piece.image))

    board_list[4].append(s40 := StringProperty(Board.board[4][0].piece.image))
    board_list[4].append(s41 := StringProperty(Board.board[4][1].piece.image))
    board_list[4].append(s42 := StringProperty(Board.board[4][2].piece.image))
    board_list[4].append(s43 := StringProperty(Board.board[4][3].piece.image))
    board_list[4].append(s44 := StringProperty(Board.board[4][4].piece.image))
    board_list[4].append(s45 := StringProperty(Board.board[4][5].piece.image))
    board_list[4].append(s46 := StringProperty(Board.board[4][6].piece.image))
    board_list[4].append(s47 := StringProperty(Board.board[4][7].piece.image))

    board_list[5].append(s50 := StringProperty(Board.board[5][0].piece.image))
    board_list[5].append(s51 := StringProperty(Board.board[5][1].piece.image))
    board_list[5].append(s52 := StringProperty(Board.board[5][2].piece.image))
    board_list[5].append(s53 := StringProperty(Board.board[5][3].piece.image))
    board_list[5].append(s54 := StringProperty(Board.board[5][4].piece.image))
    board_list[5].append(s55 := StringProperty(Board.board[5][5].piece.image))
    board_list[5].append(s56 := StringProperty(Board.board[5][6].piece.image))
    board_list[5].append(s57 := StringProperty(Board.board[5][7].piece.image))

    board_list[6].append(s60 := StringProperty(Board.board[6][0].piece.image))
    board_list[6].append(s61 := StringProperty(Board.board[6][1].piece.image))
    board_list[6].append(s62 := StringProperty(Board.board[6][2].piece.image))
    board_list[6].append(s63 := StringProperty(Board.board[6][3].piece.image))
    board_list[6].append(s64 := StringProperty(Board.board[6][4].piece.image))
    board_list[6].append(s65 := StringProperty(Board.board[6][5].piece.image))
    board_list[6].append(s66 := StringProperty(Board.board[6][6].piece.image))
    board_list[6].append(s67 := StringProperty(Board.board[6][7].piece.image))

    board_list[7].append(s70 := StringProperty(Board.board[7][0].piece.image))
    board_list[7].append(s71 := StringProperty(Board.board[7][1].piece.image))
    board_list[7].append(s72 := StringProperty(Board.board[7][2].piece.image))
    board_list[7].append(s73 := StringProperty(Board.board[7][3].piece.image))
    board_list[7].append(s74 := StringProperty(Board.board[7][4].piece.image))
    board_list[7].append(s75 := StringProperty(Board.board[7][5].piece.image))
    board_list[7].append(s76 := StringProperty(Board.board[7][6].piece.image))
    board_list[7].append(s77 := StringProperty(Board.board[7][7].piece.image))

    def click(self, x, y):

        if not BoardGrid.selected:
            BoardGrid.s_x = x
            BoardGrid.s_y = y
            BoardGrid.selected = True
            Board.board[x][y].piece.selected = True

            self.s00 = (Board.board[0][0].piece.get_selected_image())
            self.s01 = (Board.board[0][1].piece.get_selected_image())
            self.s02 = (Board.board[0][2].piece.get_selected_image())
            self.s03 = (Board.board[0][3].piece.get_selected_image())
            self.s04 = (Board.board[0][4].piece.get_selected_image())
            self.s05 = (Board.board[0][5].piece.get_selected_image())
            self.s06 = (Board.board[0][6].piece.get_selected_image())
            self.s07 = (Board.board[0][7].piece.get_selected_image())

            self.s10 = (Board.board[1][0].piece.get_selected_image())
            self.s11 = (Board.board[1][1].piece.get_selected_image())
            self.s12 = (Board.board[1][2].piece.get_selected_image())
            self.s13 = (Board.board[1][3].piece.get_selected_image())
            self.s14 = (Board.board[1][4].piece.get_selected_image())
            self.s15 = (Board.board[1][5].piece.get_selected_image())
            self.s16 = (Board.board[1][6].piece.get_selected_image())
            self.s17 = (Board.board[1][7].piece.get_selected_image())

            self.s20 = (Board.board[2][0].piece.get_selected_image())
            self.s21 = (Board.board[2][1].piece.get_selected_image())
            self.s22 = (Board.board[2][2].piece.get_selected_image())
            self.s23 = (Board.board[2][3].piece.get_selected_image())
            self.s24 = (Board.board[2][4].piece.get_selected_image())
            self.s25 = (Board.board[2][5].piece.get_selected_image())
            self.s26 = (Board.board[2][6].piece.get_selected_image())
            self.s27 = (Board.board[2][7].piece.get_selected_image())

            self.s30 = (Board.board[3][0].piece.get_selected_image())
            self.s31 = (Board.board[3][1].piece.get_selected_image())
            self.s32 = (Board.board[3][2].piece.get_selected_image())
            self.s33 = (Board.board[3][3].piece.get_selected_image())
            self.s34 = (Board.board[3][4].piece.get_selected_image())
            self.s35 = (Board.board[3][5].piece.get_selected_image())
            self.s36 = (Board.board[3][6].piece.get_selected_image())
            self.s37 = (Board.board[3][7].piece.get_selected_image())

            self.s40 = (Board.board[4][0].piece.get_selected_image())
            self.s41 = (Board.board[4][1].piece.get_selected_image())
            self.s42 = (Board.board[4][2].piece.get_selected_image())
            self.s43 = (Board.board[4][3].piece.get_selected_image())
            self.s44 = (Board.board[4][4].piece.get_selected_image())
            self.s45 = (Board.board[4][5].piece.get_selected_image())
            self.s46 = (Board.board[4][6].piece.get_selected_image())
            self.s47 = (Board.board[4][7].piece.get_selected_image())

            self.s50 = (Board.board[5][0].piece.get_selected_image())
            self.s51 = (Board.board[5][1].piece.get_selected_image())
            self.s52 = (Board.board[5][2].piece.get_selected_image())
            self.s53 = (Board.board[5][3].piece.get_selected_image())
            self.s54 = (Board.board[5][4].piece.get_selected_image())
            self.s55 = (Board.board[5][5].piece.get_selected_image())
            self.s56 = (Board.board[5][6].piece.get_selected_image())
            self.s57 = (Board.board[5][7].piece.get_selected_image())

            self.s60 = (Board.board[6][0].piece.get_selected_image())
            self.s61 = (Board.board[6][1].piece.get_selected_image())
            self.s62 = (Board.board[6][2].piece.get_selected_image())
            self.s63 = (Board.board[6][3].piece.get_selected_image())
            self.s64 = (Board.board[6][4].piece.get_selected_image())
            self.s65 = (Board.board[6][5].piece.get_selected_image())
            self.s66 = (Board.board[6][6].piece.get_selected_image())
            self.s67 = (Board.board[6][7].piece.get_selected_image())

            self.s70 = (Board.board[7][0].piece.get_selected_image())
            self.s71 = (Board.board[7][1].piece.get_selected_image())
            self.s72 = (Board.board[7][2].piece.get_selected_image())
            self.s73 = (Board.board[7][3].piece.get_selected_image())
            self.s74 = (Board.board[7][4].piece.get_selected_image())
            self.s75 = (Board.board[7][5].piece.get_selected_image())
            self.s76 = (Board.board[7][6].piece.get_selected_image())
            self.s77 = (Board.board[7][7].piece.get_selected_image())

        else:
            if turn(BoardGrid.s_x, BoardGrid.s_y, x, y, BoardGrid.iswhite):
                BoardGrid.iswhite = not BoardGrid.iswhite
                if self.ui_iswhite == "images/white-king.png":
                    self.ui_iswhite = "images/black-king.png"
                else:
                    self.ui_iswhite = "images/white-king.png"
            BoardGrid.selected = False

            Board.board[BoardGrid.s_x][BoardGrid.s_y].piece.selected = False
            Board.board[x][y].piece.selected = False

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

class Ui(BoxLayout):
    w, h = Window._get_size()
    ui_size_x = max(w, h) - min(w, h)
    ui_size_y = min(w, h)
    ui_pos_x = min(w, h)

class ChessApp(App):
    pass

ChessApp().run()