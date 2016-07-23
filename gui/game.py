import pygame

from gameobjects import Apple
from gameobjects import Snake
from gui.menu import Menu
from gui.view import View
from utils.utils import Vector, Params


class Game(View):
    def __init__(self, surface, clock):
        super().__init__(surface, clock)
        self.snake = Snake(Vector(Params.BLOCKSH / 2, Params.BLOCKSW / 2))
        self.apple = Apple()

    def ontick(self):
        self.snake.move()
        self.snake.check_eat_apple(self.apple)
        self.clock.tick(Params.FPS)

        if self.snake.self_collision():
            Params.MENU_BACK = pygame.Surface(self.surface.get_size())
            Params.MENU_BACK.blit(self.surface, (0, 0))
            Menu(self.surface, self.clock).run(gameover=True, score=len(self.snake.blocklist) - 2)
            self.snake.reset()

    def onevent(self, e):
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_RIGHT:
                self.snake.change_direction('right')
            if e.key == pygame.K_LEFT:
                self.snake.change_direction('left')
            if e.key == pygame.K_DOWN:
                self.snake.change_direction('up')
            if e.key == pygame.K_UP:
                self.snake.change_direction('down')

    def ondraw(self):
        self.surface.blit(Params.IMG_BACK, (0, 0))
        self.snake.draw(self.surface)
        self.apple.draw(self.surface)
        self.surface.blit(Params.SCOREFONT.render('SCORE: ' + str(len(self.snake.blocklist) - 2), 1, (255, 255, 255)), (5, 5))
