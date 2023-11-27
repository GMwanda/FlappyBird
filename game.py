import pygame

pygame.init()

# KEY VARIABLES
WIDTH = 864
HEIGHT = 736
ground_scroll = 0
scroll_speed = 4
timer = pygame.time.Clock()
fps = 60

# CREATE SCREEN
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# LOAD IMAGES
background = pygame.image.load('Assets/bg.png')
resized_background = pygame.transform.scale(background, (WIDTH, HEIGHT - 150))
ground = pygame.image.load('Assets/ground.png')


def game_loop():
    global ground_scroll
    running = True

    while running:
        timer.tick(fps)

        # DISPLAY ON BACKGROUND
        screen.blit(resized_background, (0, 0))

        # DISPLAY GROUND
        screen.blit(ground, (ground_scroll, HEIGHT - 150))
        ground_scroll -= scroll_speed
        if abs(ground_scroll) > 35:
            ground_scroll = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        pygame.display.update()
        pygame.display.flip()

    pygame.quit()
