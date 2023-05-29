import pygame

class Board(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("../graphics/img_0.png")
        self.rect = self.image.get_rect()
class Circle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("../graphics/img_1.png")
        self.rect = self.image.get_rect()
class Eks(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("../graphics/img_2.png")
        self.rect = self.image.get_rect()