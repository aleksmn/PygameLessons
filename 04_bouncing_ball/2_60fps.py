import sys, pygame
pygame.init()

# Set parameters
WINDOW_WIDTH, WINDOW_HEIGHT = 600, 400
SPEED = [8, 8]
BLACK = (0, 0, 0)

# Set FPS and clock
FPS = 60
clock = pygame.time.Clock()

# Create a display surface
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Bounce at 60 FPS!')

ball = pygame.image.load("ball.png")
ballrect = ball.get_rect()

# The main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    ballrect = ballrect.move(SPEED)

    if ballrect.left < 0 or ballrect.right > WINDOW_WIDTH:
        SPEED[0] = -SPEED[0]
    if ballrect.top < 0 or ballrect.bottom > WINDOW_HEIGHT:
        SPEED[1] = -SPEED[1]

    # Fill display to cover old images   
    screen.fill(BLACK)
    # Blit image
    screen.blit(ball, ballrect)
    # Update the display
    pygame.display.update()
    # Tick the clock 
    clock.tick(FPS)
