__author__ = 'Bobsans'

import pygame
from utils.utils import Vector, Params, play_eat_sound


class Snake:
    nexttick = 0

    def __init__(self, position=Vector(0, 0), direction=Vector(0, -1), speed=10, color=(78, 186, 111)):
        self.speed = speed
        self.color = color
        self.direction = direction
        self.position = position
        self.blocklist = []
        self.nexttick = Params.FPS / speed
        self.reset()

    def draw(self, surface):
        self.blocklist[-1].draw(surface, Params.IMG_SNAKEHEAD)
        for block in self.blocklist[1:-1]:
            block.draw(surface, Params.IMG_APPLE)
            # pygame.draw.rect(surface, self.color, (block.position.x * Params.BLOCK_SIZE, block.position.y * Params.BLOCK_SIZE, Params.BLOCK_SIZE, Params.BLOCK_SIZE))

        self.blocklist[0].draw(surface, Params.IMG_SNAKETAIL)

    def move(self):
        if self.nexttick == 0:
            self.blocklist[-1].direction = self.direction

            block = self.blocklist.pop(0)
            block.position = self.blocklist[-1].position + self.direction
            block.direction = self.direction
            self.blocklist.append(block)

            for block in self.blocklist:
                block.check_outside()

            self.nexttick = Params.FPS / self.speed
        self.nexttick -= 1

    def change_direction(self, direction):
        if direction == 'right':
            self.direction = Vector(1, 0) if self.direction != Vector(-1, 0) else self.direction
        elif direction == 'left':
            self.direction = Vector(-1, 0) if self.direction != Vector(1, 0) else self.direction
        elif direction == 'up':
            self.direction = Vector(0, 1) if self.direction != Vector(0, -1) else self.direction
        elif direction == 'down':
            self.direction = Vector(0, -1) if self.direction != Vector(0, 1) else self.direction
        else:
            self.direction = Vector(0, 0)

    def check_eat_apple(self, apple):
        if apple.position == self.blocklist[-1].position:
            apple.new()
            self.blocklist.reverse()
            self.blocklist.append(SnakeBlock(self.blocklist[-1].position - self.blocklist[-1].direction, self.blocklist[-1].direction))
            self.blocklist.reverse()
            play_eat_sound()

    def self_collision(self):
        for block in self.blocklist[:-1]:
            if block.position == self.blocklist[-1].position:
                return True
        return False

    def reset(self):
        self.blocklist.clear()
        for i in range(2):
            self.blocklist.append(SnakeBlock(Vector(0, -i) + self.position, self.direction))


class SnakeBlock():
    def __init__(self, position, direction):
        self.position = position
        self.direction = direction

    def draw(self, surface, image):
        image = pygame.transform.rotate(image, 270 if self.direction.x > 0 else (90 if self.direction.x < 0 else (180 if self.direction.y > 0 else 0)))
        surface.blit(image, (self.position * Params.BLOCK_SIZE).tuple)

    def check_outside(self):
        self.position.x = 0 if self.position.x > Params.BLOCKSW - 1 else (Params.BLOCKSW - 1 if self.position.x < 0 else self.position.x)
        self.position.y = 0 if self.position.y > Params.BLOCKSH - 1 else (Params.BLOCKSH - 1 if self.position.y < 0 else self.position.y)

    def __repr__(self):
        return str(self.position)