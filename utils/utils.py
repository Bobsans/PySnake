import pygame
import random

pygame.init()

class Params():
    FPS = 60

    WIN_WIDTH = 800
    WIN_HEIGHT = 600

    BLOCK_SIZE = 20

    BLOCKSW = int(WIN_WIDTH / BLOCK_SIZE)
    BLOCKSH = int(WIN_HEIGHT / BLOCK_SIZE)

    IMG_BACK = pygame.image.load('assets/back.jpg')
    IMG_SNAKEHEAD = pygame.image.load('assets/head.png')
    IMG_SNAKETAIL = pygame.image.load('assets/end.png')
    IMG_APPLE = pygame.image.load('assets/apple.png')

    MENU_BACK = IMG_BACK

    FONTFILE = 'assets/font.ttf'

    MENUFONT = pygame.font.Font(FONTFILE, 64)
    SCOREFONT = pygame.font.Font(FONTFILE, 18)

    SOUNDSEAT = [pygame.mixer.Sound('assets/crunch1.wav'), pygame.mixer.Sound('assets/crunch2.wav'),
                 pygame.mixer.Sound('assets/crunch3.wav'), pygame.mixer.Sound('assets/crunch4.wav'),
                 pygame.mixer.Sound('assets/crunch5.wav'), pygame.mixer.Sound('assets/crunch6.wav'),
                 pygame.mixer.Sound('assets/crunch7.wav')]

    BACKMUSICFILE = 'assets/BoxCat.ogg'

def intersect(r1, r2):
    return r1[0] >= r2[0] and r1[0] + r1[2] <= r2[0] + r2[2] and r1[1] >= r2[1] and r1[1] + r1[3] <= r2[1] + r2[3]

def render_text(text, font, color, x, y):
    st = font.render(text, 1, color)
    sr = st.get_rect()
    sr.centerx = Params.WIN_WIDTH / 2 if x == 'c' else x
    sr.centery = Params.WIN_HEIGHT / 2 if y == 'c' else y
    return st, sr


def play_eat_sound():
    random.choice(Params.SOUNDSEAT).play()


def play_back_music():
    pygame.mixer.music.load(Params.BACKMUSICFILE)
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(-1)


class Vector():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, v):
        return Vector(self.x + v.x, self.y + v.y)

    def __sub__(self, v):
        return Vector(self.x - v.x, self.y - v.y)

    def __mul__(self, v):
        if isinstance(v, Vector):
            return Vector(self.x * v.x, self.y * v.y)
        elif isinstance(v, (int, float)):
            return Vector(self.x * v, self.y * v)
        return self

    def __eq__(self, v):
        return self.x == v.x and self.y == v.y

    def __str__(self):
        return 'Vector[%s, %s]' % (self.x, self.y)

    def __getattr__(self, item):
        if item == 'tuple':
            return (self.x, self.y)