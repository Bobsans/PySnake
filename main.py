from gui.game import Game

__author__ = 'Bobsans'

import pygame
from gui.menu import Menu
from utils.utils import Params, play_back_music

pygame.init()

display = pygame.display.set_mode((Params.WIN_WIDTH, Params.WIN_HEIGHT))
pygame.display.set_caption('Snake at name Python!')
pygame.display.set_icon(Params.IMG_APPLE)

play_back_music()

clock = pygame.time.Clock()

Menu(display, clock).run()
Game(display, clock).run()

pygame.quit()
quit()