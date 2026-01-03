import pygame as pg
import random


class Dragon(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)

        self.image = pg.image.load("images/dragon.png")
        self.image = pg.transform.scale(self.image, (80, 80))

        self.rect = self.image.get_rect()
        # координаты         x    y
        self.rect.topleft = (25, 25)

    def update(self):
        # список нажатых клавишь
        keys = pg.key.get_pressed()
        # ДЗ: дописать условие, чтобы спрайт не уходил за границы экрана
        if keys[pg.K_w] and ...:
            self.rect.y -= 5
        if keys[pg.K_s] and ...:
            ...



# Инициализируем pygame
pg.init()

# Создаем игровой дисплей
WINDOW_WIDTH = 600
WINDOW_HIGHT = 375

screen = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HIGHT))
pg.display.set_caption('Hungry Dragon!')

FPS = 60
clock = pg.time.Clock()

# Создаем объекты
dragon = Dragon()


# Игровой цикл
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    dragon.update()

    # Фон
    screen.fill("black")

    # Отрисовка спрайтов
    screen.blit(dragon.image, dragon.rect)


    # Обновляем экран
    pg.display.update()
    clock.tick(FPS)