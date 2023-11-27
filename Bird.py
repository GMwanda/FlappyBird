import pygame

pygame.init()


class bird_class(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images_list = []
        self.images_index = 0
        self.counter = 0
        for i in range(1, 4):
            img = pygame.image.load(f'Assets/bird{i}.png')
            self.images_list.append(img)
        self.image = self.images_list[self.images_index]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.vel = 0
        self.clicked = False

    def update(self, HEIGHT, flying, game_over):
        self.counter += 1
        flap_cooldown = 5

        if flying == True:
            # ADDING GRAVITY PULL
            self.vel += .5
            if self.vel > 8:
                self.vel = 8
            if self.rect.bottom < HEIGHT - 150:
                self.rect.y += int(self.vel)

        if game_over == False:
            # MOUSE CLICK TO JUMP
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                self.vel = -10
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

            # HANDLE BIRD ANIMATION
            if self.counter > flap_cooldown:
                self.counter = 0
                self.images_index += 1
                if self.images_index >= len(self.images_list):
                    self.images_index = 0
            self.image = self.images_list[self.images_index]

            self.image = pygame.transform.rotate(self.images_list[self.images_index], self.vel * -2)
        else:
            self.image = pygame.transform.rotate(self.images_list[self.images_index], -90)


bird_group = pygame.sprite.Group()
