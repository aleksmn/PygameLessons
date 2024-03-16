import pygame as pg

# Размер окна
size = (500, 500)
screen = pg.display.set_mode(size)
# Заголовок окна
pg.display.set_caption('Изображения и звук')


# Персонаж
character = pg.image.load("Character.png")
# изменяем размер картинки
character = pg.transform.scale(character, (250, 420))
# задаем расположение
character_rect = character.get_rect()
character_rect.center = (size[0] // 2, size[1] // 2)


# FPS
fps = 100
clock = pg.time.Clock()

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    
    # Заливка фона
    screen.fill("orange")


    # Размещаем картинку на экране
    screen.blit(character, character_rect)

      
    pg.display.flip()
    clock.tick(fps)

pg.quit()
