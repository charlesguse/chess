import pygame
import sys
from board import board
from renderer import renderer
from input import input_handler, input_state

from pygame import locals


#print board[0][0]

board = board.Board()
board.print_board()

state = input_state.InputState(board.board)
input = input_handler.InputHandler(state)

renderer = renderer.Renderer(state)


fpsClock = pygame.time.Clock()

#mousex, mousey = 0, 0
#
#fontObj = pygame.font.Font('freesansbold.ttf', 32)
#msg = 'Hello World!'


while True:

    input.update()

    renderer.update(board.board)
    renderer.draw()

    fpsClock.tick(30)
#