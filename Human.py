import pygame, math

class Human(pygame.sprite.Sprite):
    def __init__(self, image, speed = [0,0], pos = [0,0]):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        '''self.moveRadius = 
        self.attackRadius =
        self.health = 
        self.maxHealth = '''
        self.speedx = speed[0]
        self.speedy = speed[1]
        self.speed = [self.speedx, self.speedy]
        self.place(pos)

        self.living = True
        
    def place(self, pos):
        self.rect.center = pos
        
    def update(*args):
        self = args[0]
        width = args[1]
        height = args[2]

        self.speed = [self.speedx, self.speedy]
        self.move()
        
    def move(self):
        self.rect = self.rect.move(self.speed)

    def attack(self):
        pass

    def distance(self, pt):
        x1 = self.rect.center[0]
        y1 = self.rect.center[1]
        x2 = pt[0]
        y2 = pt[1]
        return math.sqrt(((x2-x1)**2) + ((y2-y1)**2))
