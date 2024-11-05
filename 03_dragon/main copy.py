import pygame as pg
import random


class Dragon(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)

        self.image = pg.image.load("images/dragon.png")
        # меняем размер
        self.image = pg.transform.scale(self.image, (80, 80))
        # Расположение спрайта 
        self.rect = self.image.get_rect()
        self.rect.topleft = (25, 25)



# Инициализируем pygame
pg.init()


# Создаем игровой дисплей
WINDOW_WIDTH = 600
WINDOW_HIGHT = 300
screen = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HIGHT))
pg.display.set_caption('Hungry Dragon!')


# Устнавливаем FPS
FPS = 60
clock = pg.time.Clock()


# Создаем фон
background = pg.image.load("images/background.jpg")
# Меняем размер картинки
background = pg.transform.scale(background, (WINDOW_WIDTH, WINDOW_HIGHT))


# Создаем объекты
dragon = Dragon()


# Игровой цикл
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False


    # Отрисовка фона
    screen.blit(background, (0, 0))

    # Отрисовка спрайтов
    screen.blit(dragon.image, dragon.rect)


    # Обновляем экран
    pg.display.update()

    clock.tick(FPS)

# Выход из игры
pg.quit()