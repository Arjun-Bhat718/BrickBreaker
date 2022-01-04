import pygame


class Brick(pygame.sprite.Sprite):
    def __init__(self, xPos, yPos, width, height, color):
        super().__init__()
        self.color = color
        self.xPos = xPos
        self.yPos = yPos
        self.width = width
        self.height = height
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = xPos
        self.rect.y = yPos


class Ball(pygame.sprite.Sprite):
    def __init__(self, xPos, yPos, width, height, color):
        super().__init__()
        self.color = color
        self.xPos = xPos
        self.yPos = yPos
        self.width = width
        self.height = height
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = xPos
        self.rect.y = yPos
