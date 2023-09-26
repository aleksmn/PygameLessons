import pygame as pg

# Размер окна
size = (500, 500)
screen = pg.display.set_mode(size)
# Заголовок окна
pg.display.set_caption('Изображения и звук')

# Добавляем иконку
icon = pg.image.load('icon.png')
pg.display.set_icon(icon)

fps = 100
clock = pg.time.Clock()

character = pg.image.load("Character.png")
character = pg.transform.scale(character, (300, 477))

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill(pg.Color("cyan"))        




    pg.display.flip()
    clock.tick(fps)

pg.quit()
