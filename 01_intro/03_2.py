import pygame as pg

size = (800, 800)
screen = pg.display.set_mode(size)

small_rect = pg.Rect(0, 0, 60, 30)

small_rect.size = (100, 100)

small_rect.center = size[0]/2, size[1]/2

left_eye = pg.Rect(0, 0, 20, 30)
right_eye = pg.Rect(0, 0, 20, 30)

left_eye.midright = (size[0] // 2 - 10, size[1] // 2)
right_eye.midleft = (size[0] // 2 + 10, size[1] // 2)

direction = 'right'

fps = 60
clock = pg.time.Clock()

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # Перемещение прямоугольника

    if small_rect.left == 0:
        direction = "right"
    if small_rect.right == size[0]:
        direction = "left"


    if direction == "right":
        small_rect.x += 1
        left_eye.x += 1
        right_eye.x += 1
    if direction == "left":
        small_rect.x -= 1
        left_eye.x -= 1
        right_eye.x -= 1

    screen.fill(pg.Color("cyan"))
    pg.draw.rect(screen, pg.Color("orange"), small_rect)
    pg.draw.rect(screen, pg.Color("white"), left_eye)
    pg.draw.rect(screen, pg.Color("white"), right_eye)
    
    pg.display.flip()
    clock.tick(fps)


pg.quit()