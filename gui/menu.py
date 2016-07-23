import pygame

from gui.view import View
from utils.utils import Params, Vector, render_text


class Menu(View):
    color = (240, 196, 25)
    selcolor = (149, 91, 165)
    selected = 0
    show = True

    def __init__(self, surface, clock):
        super().__init__(surface, clock)
        self.items = [MenuItem(0, 'Play'), MenuItem(1, 'Options'), MenuItem(2, 'Exit')]
        self.score = 0
        self.gameover = False
        self.surface = surface
        self.logo = [pygame.image.load('assets/logo.png')]
        lrect = self.logo[0].get_rect()
        lrect.center = Params.WIN_WIDTH / 2, 130
        self.logo.append(lrect)

        self.recalc_items_pos()

    def config(self):
        self.items[0].text = 'Play Again' if self.gameover else 'Play'
        self.recalc_items_pos()

    def onevent(self, e):
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_DOWN:
                self.selected += 1
                if self.selected > len(self.items) - 1:
                    self.selected = 0
            elif e.key == pygame.K_UP:
                self.selected -= 1
                if self.selected < 0:
                    self.selected = len(self.items) - 1
            elif e.key == pygame.K_RETURN:
                self.action(self.selected)
        if e.type == pygame.MOUSEMOTION:
            pos = pygame.mouse.get_pos()
            for item in self.items:
                if item.rect.contains(pygame.Rect(pos[0], pos[1], 1, 1)):
                    self.selected = item.id
        if e.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if e.button == 1:
                for item in self.items:
                    if item.rect.contains(pygame.Rect(pos[0], pos[1], 1, 1)):
                        self.action(item.id)

    def ondraw(self):
        self.surface.blit(Params.MENU_BACK, (0, 0))
        # self.surface.blit(Params.IMG_BACK, (0, 0))
        self.surface.blit(self.logo[0], self.logo[1])

        for item in self.items:
            text = Params.MENUFONT.render(item.text, 1, self.selcolor if self.selected == item.id else  self.color)
            self.surface.blit(text, item.position.tuple)

        if self.gameover:
            st, sr = render_text('You score: ' + str(self.score), Params.SCOREFONT, (255, 255, 255), 'c', 'c')
            self.surface.blit(st, sr)

    def recalc_items_pos(self):
        for item in self.items:
            size = item.font.size(item.text)
            rect = pygame.Rect(0, 0, size[0], size[1])
            rect.center = Params.WIN_WIDTH / 2, Params.WIN_HEIGHT / 2 + (len(self.items) + (item.id * (size[1] - 10)) + 50)
            item.position = Vector(rect.left, rect.top)
            item.rect = rect

    def action(self, iid):
        if iid == 0:
            self.stop()
        elif iid == 1:
            print('Options')
        elif iid == 2:
            quit()


class MenuItem():
    def __init__(self, id, text, position=Vector(0, 0), font=Params.MENUFONT, color=(255, 255, 255)):
        self.id = id
        self.text = text
        self.position = position
        self.font = font
        self.color = color

    def draw(self, surface):
        surface.blit(self.font.render(self.text, 1, self.color), self.position.tuple)
