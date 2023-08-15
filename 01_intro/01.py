import pygame as pg
import random

# Размер окна
size = (500, 500)
screen = pg.display.set_mode(size)

fps = 4

clock = pg.time.Clock()

while True:
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    screen.fill(pg.Color(r, g, b))
    
    pg.display.flip()

    clock.tick(fps)