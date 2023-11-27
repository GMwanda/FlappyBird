import pygame

pygame.init()


class pipe_class(pygame.sprite.Sprite):
    def __init__(self, x, y, position, pipe_gap):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Assets/pipe.png')
        self.rect = self.image.get_rect()

        # CREATE THE PIPES AND ADDING THE GAPS
        if position == 1:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect.bottomleft = [x, y - int(pipe_gap / 2)]
        if position == -1:
            self.rect.topleft = [x, y + int(pipe_gap / 2)]

    def update(self, scroll_speed):
        # HAVE THE PIPES SCROLLING
        self.rect.x -= scroll_speed

        if self.rect.right < 0:
            self.kill()


pipe_group = pygame.sprite.Group()
