import pygame as pg

# Размер окна
size = (500, 500)
screen = pg.display.set_mode(size)
# Заголовок окна
pg.display.set_caption('Рисуем фигуры')

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False


    screen.fill(pg.Color("cyan"))
    pg.draw.rect(screen, pg.Color("orange"), (100, 200, 80, 120))
    
    pg.display.flip()


pg.quit()