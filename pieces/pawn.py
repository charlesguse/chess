import pygame
from pieces import piece
from pygame import constants

__author__ = 'Charles'

class Pawn(piece.Piece):
    def get_surface(self):
        if self.color == piece.Piece.WHITE:
            return 'gfx/white_pawn.png'
        else:
            return 'gfx/black_pawn.png'

    def name(self):
        return "p"

    def  can_move(self, x ,y):
        locations = []

        try:
            if not self.board[x][y + (1 * self.color)].has_piece(self.enemy_color()):
                locations.append((x, y + (1 * self.color)))
        except IndexError:
            pass

        if not self.moved:
            locations.append((x, y + (2 * self.color)))

        try:
            if self.board[x + 1][y + (1 * self.color)].has_piece(self.enemy_color()):
                locations.append((x + 1, y + (1 * self.color)))
        except IndexError:
            pass

        try:
            if self.board[x - 1][y + (1 * self.color)].has_piece(self.enemy_color()):
                locations.append((x - 1, y + (1 * self.color)))
        except IndexError:
            pass

        # add en passant after notation has been added
        return locations

    def move(self, x, y, newx, newy):
        if (newx, newy) in self.can_move(x, y):
            self.moved = True
            self.board[newx][newy].piece = self.board[x][y].piece
            self.board[x][y].piece = None
