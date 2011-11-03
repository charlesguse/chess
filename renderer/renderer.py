import pygame, os
from pygame import constants
from input import input_state
from input.input_state import InputState

__author__ = 'Charles'


class Renderer:
    def __init__(self, state):
        self.state = state

        pygame.init()

        self.screen = pygame.display.set_mode((512,512))
        pygame.display.set_caption('Chess')

        self.white_square = pygame.image.load('gfx/white_square.png').convert()
        self.black_square = pygame.image.load('gfx/black_square.png').convert()
        self.highlight = pygame.image.load('gfx/highlight.png').convert()
        self.highlight.set_colorkey(pygame.Color(255,0,255), constants.RLEACCEL)


    def init_surface(self, path):
        surface = pygame.image.load(path).convert()
        surface.set_colorkey(pygame.Color(255,0,255), constants.RLEACCEL)
        return surface

    def update(self, board):
        display = []

        #if self.state.board_rotation == input_state.InputState.WHITE:
        display = range(len(board) - 1, -1, -1)
        #else:
        #    display = range(len(board))

        for x in display:
            for y in display:
                square_to_use = None

                if x % 2 == y % 2:
                    square_to_use = self.white_square
                else:
                    square_to_use = self.black_square

                pos = (x * square_to_use.get_width(), y * square_to_use.get_height())
                self.screen.blit(square_to_use, pos)

                if board[x][y].piece != None:
                    if board[x][y].piece.surface == None:
                        board[x][y].piece.surface = self.init_surface(board[x][y].piece.get_surface())
                    self.screen.blit(board[x][y].piece.surface, pos)

        for tile_pos in self.state.potential_place_to_move:
            x = tile_pos[0]
            y = tile_pos[1]
            pos = (x * square_to_use.get_width(), y * square_to_use.get_height())
            self.screen.blit(self.highlight, pos)

    def draw(self):
        pygame.display.update()

