import pieces

__author__ = 'Charles'

class InputState:
    WHITE = 1
    BLACK = -1
    TILE_SIZE_X = 64
    TILE_SIZE_Y = 64

    def __init__(self, board):
        self.board = board
        self.current_selection = None
        self.potential_place_to_move = []
        self.board_rotation = InputState.WHITE
        self.current_player = pieces.piece.Piece.WHITE

    def handle_mousedown(self, pos):
        x = pos[0] / InputState.TILE_SIZE_X
        y = pos[1] / InputState.TILE_SIZE_Y

        if (x, y) in self.potential_place_to_move:
            self.move_piece(pos)
        else:
            self.select_piece(pos)

    def select_piece(self, pos):
        x = pos[0] / InputState.TILE_SIZE_X
        y = pos[1] / InputState.TILE_SIZE_Y

        if self.board[x][y].piece != None and self.board[x][y].piece.color == self.current_player:
            self.current_selection = (x, y)
            self.potential_place_to_move = self.board[x][y].piece.can_move(x ,y)
        else:
            self.current_selection = None
            self.potential_place_to_move = []

    def move_piece(self, pos):
        x = pos[0] / InputState.TILE_SIZE_X
        y = pos[1] / InputState.TILE_SIZE_Y

        if (x, y) in self.potential_place_to_move:
            oldx = self.current_selection[0]
            oldy = self.current_selection[1]
            self.board[oldx][oldy].piece.move(oldx, oldy, x, y)
            self.current_player = self.board[x][y].piece.enemy_color()
        self.current_selection = None
        self.potential_place_to_move = []
