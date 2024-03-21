import pygame as pg

# Инициализируем модуль для проигрывания звуков
pg.mixer.init()

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

# Загружаем звуковой файл
pg.mixer.music.load("music.mp3")
# Включаем воспроизведение
pg.mixer.music.play()
pg.mixer.music.set_volume(0.05)


# hello_sound = pg.mixer.Sound("hello.mp3")
# hello_sound.set_volume(0.9)
# hello_sound.play()

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # screen.fill(pg.Color("cyan"))

    screen.blit(background, (0, 0))        

    screen.blit(character, (0, size[1] - character_size[1]))        
  
    
    pg.display.flip()
    clock.tick(fps)

pg.quit()
