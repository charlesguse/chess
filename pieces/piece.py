__author__ = 'Charles'

class Piece:
    WHITE = 1
    BLACK = -1

    def __init__(self, board, color):
        self.color = color
        self.board = board
        #self.x = x
        #self.y = y
        self.color = color
        self.moved = False
        self.surface = None
        #self.surface.set_colorkey(pygame.Color(255,0,255), constants.RLEACCEL)

    def enemy_color(self):
        if self.color == Piece.WHITE:
            return Piece.BLACK
        else:
            return Piece.WHITE

    def get_surface(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def name(self):
        raise NotImplementedError("Subclass must implement abstract method")
    
    def  can_move(self, x, y):
        raise NotImplementedError("Subclass must implement abstract method")

    def move(self, x, y, newx, newy):
        raise NotImplementedError("Subclass must implement abstract method")

    #def check_bounds(self, x, y):
    #    return 0 <= x < Board.SIZE_X and 0 <= y < Board.SIZE_Y