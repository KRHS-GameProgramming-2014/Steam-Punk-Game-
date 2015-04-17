import pygame, math

class Block(pygame.sprite.Sprite):
    def __init__(self, image, clickedImage = "", pos = [0,0]):
        if clickedImage != "":
            self.baseImage =  pygame.image.load(image)
            self.clickedImage =  pygame.image.load(clickedImage)
        else:
            self.baseImage =  pygame.image.load(image)
            self.clickedImage =  pygame.image.load(image)
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.place(pos)
        self.living = True
        self.clicked = False
        self.image = self.baseImage
        self.rect = self.image.get_rect()
        
    def place(self, pos):
        self.rect.topleft = pos
        
    
    
    def collidePoint(self, pt):
        if self.rect.right > pt[0] and self.rect.left < pt[0]:
            if self.rect.bottom > pt[1] and self.rect.top < pt[1]:      
                return True
        return False
    
    def click(self, pt):
        if self.collidePoint(pt):
            self.clicked = True
            self.image = self.clickedImage
        else:
            self.clicked = False
            self.image = self.baseImage
            
    def release(self, pt):
        if self.clicked and self.collidePoint(pt):
            return True
        else:
            self.clicked = False
            self.image = self.baseImage
            return False
            
    def update(*args):
        self = args[0]
