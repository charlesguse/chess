import pygame
from pieces import piece
from pygame import constants

__author__ = 'Charles'

class Knight(piece.Piece):
    def get_surface(self):
        if self.color == piece.Piece.WHITE:
            return 'gfx/white_knight.png'
        else:
            return 'gfx/black_knight.png'

    def name(self):
        return "n"

    def  can_move(self, x ,y):
        locations = []

        try:
            if not self.board[x][y + (1 * self.color)].has_piece(self.color):
                locations.append((x, y + (1 * self.color)))
        except IndexError:
            pass

        return locations

    def move(self, x, y, newx, newy):
        if (newx, newy) in self.can_move(x, y):
            self.board[x][y].piece = None