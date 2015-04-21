import pygame, math

class Block(pygame.sprite.Sprite):
    def __init__(self, size, image, clickedImage = "", pos = [0,0]):
        pygame.sprite.Sprite.__init__(self, self.containers)
        if clickedImage != "":
            self.baseImage =  pygame.image.load(image)
            self.clickedImage =  pygame.image.load(clickedImage)
        else:
            self.baseImage =  pygame.image.load(image)
            self.clickedImage =  pygame.image.load(image)
            
        if size != None:
            self.baseImage = pygame.transform.scale(self.baseImage, size)
            self.clickedImage = pygame.transform.scale(self.clickedImage, size)
        self.image = self.baseImage
        self.rect = self.image.get_rect()
        self.place(pos)
        #self.pos = self.rect.center
        #print self.rect.center
        self.living = True
        self.clicked = False
        
        
        
    def place(self, pos):
        self.rect.center = pos
    
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
