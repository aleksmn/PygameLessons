import pygame as pg
import random



# Создаем окно для игры
# Размер окна
size = (500, 500)
# Окно
screen = pg.display.set_mode(size)


# Количество кадров секунду
fps = 1

clock = pg.time.Clock()

# Игровой цикл
while True:

    
    screen.fill("orange")

    # Обновляем экран
    pg.display.flip()
    # Переходим к следующем кадру
    clock.tick(fps)