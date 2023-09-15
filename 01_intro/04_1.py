import pygame as pg

# Размер окна
size = (500, 500)
screen = pg.display.set_mode(size)
# Заголовок окна
pg.display.set_caption('Изображения и звук')

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

    screen.blit(character, (0, 0))        
    

    pg.display.flip()
    clock.tick(fps)

pg.quit()
