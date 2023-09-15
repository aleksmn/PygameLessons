import pygame as pg

# Размер окна
size = (500, 500)
screen = pg.display.set_mode(size)
# Заголовок окна
pg.display.set_caption('Изображения и звук')

fps = 100
clock = pg.time.Clock()

background = pg.image.load("background.png")
background = pg.transform.scale(background, size)

character = pg.image.load("Character.png")
character_size = (250, 427)
character = pg.transform.scale(character, character_size)

character2 = pg.transform.flip(character, True, False)
character2_rect = character2.get_rect(center = (size[0] // 2, size[1] // 2))


running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # screen.fill(pg.Color("cyan"))

    screen.blit(background, (0, 0))        

    screen.blit(character, (0, size[1] - character_size[1]))        

    screen.blit(character2, character2_rect)        
    
 
    pg.display.flip()
    clock.tick(fps)

pg.quit()
