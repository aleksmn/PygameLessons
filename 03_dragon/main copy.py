import pygame as pg
import random


# Инициализируем pygame
pg.init()

# Создаем игровой дисплей
WINDOW_WIDTH = 800
WINDOW_HIGHT = 600
screen = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HIGHT))
pg.display.set_caption('Hungry Dragon!')


# Устнавливаем FPS
FPS = 60
clock = pg.time.Clock()

# Объявляем цвета
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


# Скорость движения
VELOCITY = 5
# Очки
score = 0


# Игровой цикл
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False


    # Заливка экрана
    screen.fill("orange")



    # Обновляем экран
    pg.display.update()
    clock.tick(FPS)

# Выход из игры
pg.quit()