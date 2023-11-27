import pygame

pygame.init()

# KEY VARIABLES
WIDTH = 864
HEIGHT = 736

# CREATE SCREEN
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# LOAD IMAGES
background = pygame.image.load('Assets/bg.png')
resized_background = pygame.transform.scale(background, (WIDTH, HEIGHT - 150))


def game_loop():
    running = True

    while running:

        # DISPLAY ON SCREEN
        screen.blit(resized_background, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        pygame.display.update()
        pygame.display.flip()

    pygame.quit()
