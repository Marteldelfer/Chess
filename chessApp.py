from chess import *
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.graphics import *
from kivy.core.window import Window
from functools import partial

Board.create_board()

iswhite = True
selected = False
s_x = None
s_y = None

def click(self, x, y):

    global selected
    global iswhite
    global s_x
    global s_y

    if not selected:
        s_x = x
        s_y = y
        selected = True
    else:
        if turn(s_x, s_y, x, y, iswhite):
            iswhite = not iswhite
        selected = False

class BoardGrid(GridLayout):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)
        self.cols = 8

        for i in range(7, -1, -1):
            for j in range(8):
                
                b = Button()
                b.on_press = partial(click, self, i, j)

                if not isinstance(Board.board[i][j].piece, EmptySquare):
                    b.background_normal = Board.board[i][j].piece.image
                else:
                    b.background_color = 0,0,0,0
                    
                self.add_widget(b)


class ChessApp(App):
    pass

ChessApp().run()