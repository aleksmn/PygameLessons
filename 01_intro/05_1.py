import pygame as pg

# Инициализируем модуль для проигрывания звуков
pg.mixer.init()

# Размер окна
size = (500, 500)
screen = pg.display.set_mode(size)
# Заголовок окна
pg.display.set_caption('Обработка событий')

fps = 100
clock = pg.time.Clock()

background = pg.image.load("background.png")
background = pg.transform.scale(background, size)

character = pg.image.load("Character.png")
character_size = (250, 427)
character = pg.transform.scale(character, character_size)

character_rect = character.get_rect(center = (size[0] // 2, size[1] // 2))

# Загружаем звуковой файл
pg.mixer.music.load("music.mp3")
# Включаем воспроизведение
pg.mixer.music.play()
pg.mixer.music.set_volume(0.01)


hello_sound = pg.mixer.Sound("hello.mp3")
hello_sound.set_volume(0.1)
hello_sound.play()

running = True
while running:
    for event in pg.event.get():

        if event.type == pg.QUIT:
            running = False

        if event.type == pg.KEYDOWN:
            
            if event.key == pg.K_LEFT:
                character_rect.x -= 10
            if event.key == pg.K_RIGHT:
                character_rect.x += 10

    screen.blit(background, (0, 0))        
    screen.blit(character, character_rect)        
    
    pg.display.flip()
    clock.tick(fps)

pg.quit()
