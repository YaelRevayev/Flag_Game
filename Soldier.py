import pygame


class Player(pygame.sprite.Sprite):

    def __init__(self):
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)
        self.image = pygame.image.load("/path/to/image_file.png")