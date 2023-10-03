import pygame as pg
import random

class Character(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)

        self.image = pg.image.load("images/character.png")
        self.image = pg.transform.scale(self.image, (250, 427))

        self.rect = self.image.get_rect()

        self.rect.center = (250, 250)

    def update(self):
        keys = pg.key.get_pressed()

        if keys[pg.K_LEFT]:
            self.rect.x -= 2
        if keys[pg.K_RIGHT]:
            self.rect.x += 2


class Butterfly(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)

        self.image = pg.image.load("images/butterfly.png")
        self.image = pg.transform.scale(self.image, (50, 50))

        self.rect = self.image.get_rect()

        self.rect.x = random.randint(0, 450)
        self.rect.y = random.randint(0, 450)


    def update(self):
        if random.randint(0, 1) == 0:
            self.rect.x -= 1
        else:
            self.rect.x += 1

        if random.randint(0, 1) == 0:
            self.rect.y -= 1
        else:
            self.rect.y += 1
