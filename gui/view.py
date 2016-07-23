import pygame


class View():
    def __init__(self, surface, clock):
        self.active = False
        self.surface = surface
        self.clock = clock

    def run(self, *args, **kvargs):
        for ak in kvargs.keys():
            setattr(self, ak, kvargs[ak])

        self.config()

        self.active = True
        while self.active:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                self.onevent(e)

            self.ontick()
            self.ondraw()

            pygame.display.update()

    def config(self):
        pass

    def stop(self):
        self.active = False

    def ontick(self):
        pass

    def onevent(self, e):
        pass

    def ondraw(self):
        pass