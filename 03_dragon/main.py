import pygame as pg
import random

class Dragon(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)

        self.image = pg.image.load("images/dragon.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (25, 25)

        self.direction = 'right'

    def update(self):
        # Get a list of all keys pressed down
        keys = pg.key.get_pressed()

        # Move the dragon continuously
        if (keys[pg.K_LEFT] or keys[pg.K_a]) and self.rect.left > 0:
            if self.direction == "right":
                self.image = pg.transform.flip(self.image, True, False)
                self.direction = "left"
            self.rect.x -= VELOCITY
        if (keys[pg.K_RIGHT] or keys[pg.K_d]) and self.rect.right < WINDOW_WIDTH:
            if self.direction == "left":
                self.image = pg.transform.flip(self.image, True, False)
                self.direction = "right"
            self.rect.x += VELOCITY
        if (keys[pg.K_UP] or keys[pg.K_w]) and self.rect.top > 0:
            self.rect.y -= VELOCITY
        if (keys[pg.K_DOWN] or keys[pg.K_s]) and self.rect.bottom < WINDOW_HIGHT:
            self.rect.y += VELOCITY

class Coin(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)

        self.image = pg.image.load("images/coin.png")
        self.rect = self.image.get_rect()
        self.rect.center = (WINDOW_WIDTH//2, WINDOW_HIGHT//2)

#Initialize pg
pg.init()

# Create a display surface
WINDOW_WIDTH = 600
WINDOW_HIGHT = 300
display_surface = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HIGHT))
pg.display.set_caption('Hungry Dragon!')


# Set FPS and clock
FPS = 60
clock = pg.time.Clock()

# Define colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Load sound effects
sound_1 = pg.mixer.Sound('sounds/sound_1.wav')
sound_1.set_volume(0.1)

# Load background music
pg.mixer.music.load('sounds/music.wav')


# Play background music
pg.mixer.music.set_volume(0.1)
pg.mixer.music.play(-1, 0.0)


# Set game values
VELOCITY = 5

score = 0

# Font
font = pg.font.Font("fonts/AttackGraffiti.ttf", 22)




dragon = Dragon()
coin = Coin()

# The main game loop
running = True
while running:
    for event in pg.event.get():
        # print(event)
        if event.type == pg.QUIT:
            running = False

    dragon.update()

    # Check for collision between two rects
    if dragon.rect.colliderect(coin.rect):
        # print("Collision!!!")
        score += 1
        sound_1.play()
        coin.rect.left = random.randint(0, WINDOW_WIDTH - coin.rect.w)
        coin.rect.top = random.randint(0, WINDOW_HIGHT - coin.rect.h)

        
    # Fill display to cover old images
    display_surface.fill((BLACK))

    # Blit image
    display_surface.blit(dragon.image, dragon.rect)
    display_surface.blit(coin.image, coin.rect)

    # Update score
    score_text = font.render(str(score), True, RED)
    display_surface.blit(score_text, (10, 10))
 
    # Update the display
    pg.display.update()

    # Tick the clock 
    clock.tick(FPS)

# End the game
pg.quit()