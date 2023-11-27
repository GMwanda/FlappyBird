import pygame

from Bird import bird_class, bird_group

pygame.init()

# KEY VARIABLES
WIDTH = 864
HEIGHT = 736
HEIGHT2 = HEIGHT - 150
ground_scroll = 0
scroll_speed = 4
timer = pygame.time.Clock()
fps = 60
flying = False
game_over = False

# CREATE SCREEN
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# LOAD IMAGES
background = pygame.image.load('Assets/bg.png')
resized_background = pygame.transform.scale(background, (WIDTH, HEIGHT2))
ground = pygame.image.load('Assets/ground.png')

# CLASSES
flappy = bird_class(100, int(HEIGHT / 2))

# GROUPS
bird_group.add(flappy)


def process_scrolling_background():
    global ground, ground_scroll, game_over
    screen.blit(ground, (ground_scroll, HEIGHT2))

    if game_over == False:
        ground_scroll -= scroll_speed
        if abs(ground_scroll) > 35:
            ground_scroll = 0


def bird_ground_collision():
    global game_over, flying
    if flappy.rect.bottom >= HEIGHT2:
        game_over = True
        flying = False


def game_loop():
    global screen, HEIGHT, ground, ground_scroll, scroll_speed, flying
    running = True

    while running:
        timer.tick(fps)

        # DISPLAY ON BACKGROUND
        screen.blit(resized_background, (0, 0))

        # DISPLAY BIRD
        bird_group.draw(screen)
        bird_group.update(HEIGHT, flying, game_over)

        # BIRD AND GROUND COLLISION
        bird_ground_collision()

        # DISPLAY GROUND
        process_scrolling_background()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and flying == False and game_over == False:
                flying = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        pygame.display.update()
        pygame.display.flip()

    pygame.quit()
