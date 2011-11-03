import pygame, sys
from pygame import locals

class InputHandler:
    def __init__(self, state):
        self.state = state
        self.pos_selected = None

    def update(self):
        for event in pygame.event.get():
            if event.type == locals.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == locals.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.state.handle_mousedown(event.pos)
            #if event.type == locals.MOUSEBUTTONUP:
            #    if event.button == 1:
            #        self.pos_selected = None
            #if self.pos_selected != None:
            #    print self.pos_selected