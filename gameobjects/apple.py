import random
from utils.utils import Vector, Params


class Apple:
    def __init__(self, color=(241, 90, 90)):
        self.position = Vector(0, 0)
        self.color = color
        self.new()

    def draw(self, surface):
        surface.blit(Params.IMG_APPLE, (self.position * Params.BLOCK_SIZE).tuple)

    def new(self):
        self.position = Vector(round(random.randrange(0, (Params.WIN_WIDTH - Params.BLOCKSW) / Params.BLOCKSW)), round(random.randrange(0, (Params.WIN_HEIGHT - Params.BLOCKSH) / Params.BLOCKSH)))
