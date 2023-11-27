import random

import pygame

from Bird import bird_class, bird_group
from Button import button_class
from Pipe import pipe_class, pipe_group

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
pipe_gap = 150
pipe_frequency = 1500
last_pipe = pygame.time.get_ticks() - pipe_frequency
score = 0
pass_pipe = False
font = pygame.font.SysFont('Helvetica', 30)
white = (255, 255, 255)

# CREATE SCREEN
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# LOAD IMAGES
background = pygame.image.load('Assets/bg.png')
resized_background = pygame.transform.scale(background, (WIDTH, HEIGHT2))
ground = pygame.image.load('Assets/ground.png')
button_img = pygame.image.load('Assets/restart.png')

# CLASSES
flappy = bird_class(100, int(HEIGHT / 2))
btn = button_class(WIDTH // 2 - 50, HEIGHT // 2 - 100, button_img)

# GROUPS
bird_group.add(flappy)


def reset_game():
    pipe_group.empty()
    flappy.rect.x = 100
    flappy.rect.y = int(HEIGHT / 2)
    score = 0
    return score


def while_game_alive():
    global ground, ground_scroll, game_over, last_pipe
    screen.blit(ground, (ground_scroll, HEIGHT2))

    if game_over == False and flying == True:
        # GENERATE THE PIPES
        time_now = pygame.time.get_ticks()
        if time_now - last_pipe > pipe_frequency:
            pipe_height = random.randint(-100, 100)
            btm_pipe = pipe_class(WIDTH, int(HEIGHT / 2) + pipe_height, -1, pipe_gap)
            top_pipe = pipe_class(WIDTH, int(HEIGHT / 2) + pipe_height, 1, pipe_gap)
            pipe_group.add(btm_pipe, top_pipe)
            last_pipe = time_now

        # DRAW AND SCROLL THE GROUND
        ground_scroll -= scroll_speed
        if abs(ground_scroll) > 35:
            ground_scroll = 0

        pipe_group.update(scroll_speed)


def while_game_dead():
    global game_over
    if game_over == True:
        if btn.draw(screen) == True:
            game_over = False
            score = reset_game()


def bird_ground_collision():
    global game_over, flying
    if flappy.rect.bottom >= HEIGHT2:
        game_over = True
        flying = False


def pipe_collision():
    global game_over
    if pygame.sprite.groupcollide(bird_group, pipe_group, False, False) or flappy.rect.top < 0:
        game_over = True


def check_score():
    global pass_pipe, score
    if len(pipe_group) > 0:
        if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.left and bird_group.sprites()[
            0].rect.right < pipe_group.sprites()[0].rect.right and pass_pipe == False:
            pass_pipe = True
        if pass_pipe == True:
            if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.right:
                score += 1
                pass_pipe = False

    draw_text(f'Score: {str(score)}', font, white, int(WIDTH / 12), 20)


def draw_text(text, font, text_color, x, y):
    img = font.render(text, True, text_color)
    screen.blit(img, (x, y))


def game_loop():
    global screen, HEIGHT, ground, ground_scroll, scroll_speed, flying, game_over, pass_pipe
    running = True

    while running:
        timer.tick(fps)

        # DISPLAY ON BACKGROUND
        screen.blit(resized_background, (0, 0))

        # DISPLAY BIRD
        bird_group.draw(screen)
        bird_group.update(HEIGHT, flying, game_over)

        # DISPLAY PIPE
        pipe_group.draw(screen)

        # CHECK SCORE
        check_score()

        # COLLISION WITH PIPE
        pipe_collision()

        # BIRD AND GROUND COLLISION
        bird_ground_collision()

        # GAME != OVER
        while_game_alive()

        # GAME OVER
        while_game_dead()

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
