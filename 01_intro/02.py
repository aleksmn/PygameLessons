import pygame as pg
import random

# Создаем окно для игры
# Размер окна
size = (500, 500)
# Окно
screen = pg.display.set_mode(size)

# Цвета
my_colors = ["#ff00ff", "#00ff00", "#0000ff", "#ff0000"]

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

    screen.fill(my_colors[0])

    # Создадим прямоугольник
    pg.draw.rect(screen, my_colors[1], (100, 200, 80, 120))



    # Обновляем экран
    pg.display.flip()
    # Переходим к следующем кадру
    clock.tick(fps)


pg.quit()