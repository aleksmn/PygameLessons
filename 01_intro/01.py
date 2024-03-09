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
fps = 1

clock = pg.time.Clock()

# Игровой цикл
while True:

    rand_color = random.choice(my_colors)
    
    screen.fill(rand_color)

    # Обновляем экран
    pg.display.flip()
    # Переходим к следующем кадру
    clock.tick(fps)