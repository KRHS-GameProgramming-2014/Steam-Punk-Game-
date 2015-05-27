import pygame, math

class BackGround(pygame.sprite.Sprite):
    def __init__(self, image, size = (800,600)):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect()
