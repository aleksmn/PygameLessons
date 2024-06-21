import pygame as pg

# Размер окна
size = (500, 500)
screen = pg.display.set_mode(size)
# Заголовок окна
pg.display.set_caption('Изображения и звук')

fps = 100
clock = pg.time.Clock()

character = pg.image.load("Character.png").convert_alpha()
character = pg.transform.scale(character, (200, 320))
character = pg.transform.flip(character, 1, 0)
# Получим прямоугольник
character_rect = character.get_rect()
character_rect.midbottom = (size[0]//2, size[1]-20)



running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill("cyan")

   

    screen.blit(character, character_rect)        


    
 
    pg.display.flip()
    clock.tick(fps)

pg.quit()
