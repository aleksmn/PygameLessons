import pygame as pg

size = (800, 800)
screen = pg.display.set_mode(size)

small_rect = pg.Rect(0, 0, 60, 30)

# small_rect.left = 100
# small_rect.top = 200

small_rect.size = (100, 100)

small_rect.center = size[0]/2, size[1]/2



fps = 60
clock = pg.time.Clock()

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False


    small_rect.width += 1
    small_rect.height += 1
    small_rect.center = size[0]/2, size[1]/2

    screen.fill(pg.Color("cyan"))
    pg.draw.rect(screen, pg.Color("orange"), small_rect)
    
    pg.display.flip()
    clock.tick(fps)


pg.quit()