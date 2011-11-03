__author__ = 'Charles'

class Tile:
    def __init__(self):
        self.piece = None

    def has_piece(self, color=None):
        if self.piece != None and (color == None or self.piece.color == color):
            return True
        elif self.piece == None or self.piece.color != color:
            return False
        #else:
        #    return True