import pygame as pg

size = (800, 800)
screen = pg.display.set_mode(size)
# Заголовок окна
pg.display.set_caption('Координаты')

small_rect = pg.Rect(0, 0, 60, 30)

# small_rect.left = 100
# small_rect.top = 200

small_rect.size = (100, 100)

small_rect.center = size[0]/2, size[1]/2

direction = 'right'

fps = 60
clock = pg.time.Clock()

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # Увеличение прямоугольника
    # small_rect.width += 1
    # small_rect.height += 1
    # small_rect.center = size[0]/2, size[1]/2


    # Перемещение прямоугольника

    if small_rect.left == 0:
        direction = "right"
    if small_rect.right == size[0]:
        direction = "left"


    if direction == "right":
        small_rect.x += 1
    if direction == "left":
        small_rect.x -= 1

    screen.fill(pg.Color("cyan"))
    pg.draw.rect(screen, pg.Color("orange"), small_rect)
    
    pg.display.flip()
    clock.tick(fps)


pg.quit()