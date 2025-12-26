import pygame as pg
import random


class Dragon(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)

        self.image = pg.image.load("images/dragon.png")
        self.image = pg.transform.scale(self.image, (80, 80))
        self.image = pg.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect()
        self.rect.topleft = (25, 25)

        self.direction = 'right'

    def update(self):
        # Список всех нажатых кнопок
        keys = pg.key.get_pressed()
        
        if keys[pg.K_LEFT] and self.rect.left > 0:
            if self.direction == "right":
                self.image = pg.transform.flip(self.image, True, False)
                self.direction = "left"
            self.rect.x -= 5
        if keys[pg.K_RIGHT] and self.rect.right < WINDOW_WIDTH:
            if self.direction == "left":
                self.image = pg.transform.flip(self.image, True, False)
                self.direction = "right"
            self.rect.x += 5
        if keys[pg.K_UP] and self.rect.top > 0:
            self.rect.y -= 5
        if keys[pg.K_DOWN] and self.rect.bottom < WINDOW_HIGHT:
            self.rect.y += 5


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