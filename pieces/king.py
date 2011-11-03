import pygame
from pieces import piece
from pygame import constants

__author__ = 'Charles'

class King(piece.Piece):
    def get_surface(self):
        if self.color == piece.Piece.WHITE:
            return 'gfx/white_king.png'
        else:
            return 'gfx/black_king.png'

    def name(self):
        return "k"

    def  can_move(self, x ,y):
        locations = []
        return locations

    def move(self, x, y, newx, newy):
        if (newx, newy) in self.can_move(x, y):
            self.board[x][y].piece = None