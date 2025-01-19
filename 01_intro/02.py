import pygame as pg
import random

# Создаем окно для игры
# Размер окна
size = (500, 500)
# Окно
screen = pg.display.set_mode(size)


# Количество кадров секунду
fps = 60

clock = pg.time.Clock()


# Игровой цикл
running = True
while running:
    # События
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill("orange")

    # Создадим прямоугольник
    pg.draw.rect(screen, "cyan", (100, 200, 80, 120))



    # Создадим линию
    pg.draw.line(screen, "blue", (0, 250), (500, 250))



    # Обновляем экран
    pg.display.flip()
    # Переходим к следующем кадру
    clock.tick(fps)


pg.quit()