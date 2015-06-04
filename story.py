import pygame, sys
from BackGround import BackGround


    
class TextWindow(pygame.sprite.Sprite):
    def __init__(self, textFile, bgImage, pos):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.textSurface = self.makeTextImage(textFile)
        self.image = pygame.image.load(bgImage)
        self.rect = self.image.get_rect(center = pos)
        self.textRect = [0,0,600,200]
        self.subTextSurface = self.textSurface.subsurface(self.textRect)
        self.image.blit(self.subTextSurface, pygame.Rect(4,4,600,200))
        self.speedx = 0
        self.speedy = 1
        self.waitCount = 0
        self.waitMax = 3
        self.done = False
    
    def makeTextImage(self, textFile):
        f = open(textFile, 'r')
        textLines = f.readlines()
        f.close()
        
        newlines = []
        for line in textLines:
            newline = ""
            for character in line:
                if character != "\n":
                    newline += character
            newlines += [newline]
        
        textLines = newlines
        
        tsize = 600, 3500
        
        background = pygame.Surface(tsize)
        background = background.convert()
        background.fill((0, 0, 0))
        
        ySize = 30 
        font = pygame.font.Font(None, 30)
        for lineNum, line in enumerate(textLines):
            text = font.render(textLines[lineNum], 1, (255, 255, 255))
            textpos = text.get_rect(topleft =  [10,(ySize*lineNum) +5])
            background.blit(text, textpos)
        
        return  background
    
    def update(*args):
        self = args[0]
        self.move()
        
    def move(self):
        if self.textRect[1] < 3300:
            if self.waitCount < self.waitMax:
                self.waitCount += 1
            else:
                self.waitCount = 0
                print self.textRect
                self.textRect[1] += self.speedy
                print self.textRect
                self.subTextSurface = self.textSurface.subsurface(self.textRect)
                self.image.blit(self.subTextSurface, pygame.Rect(4,4,600,200))
        else:
            self.done = True
    
    def skip(self):
        self.done = True
        
        
        
if __name__ == '__main__':
    pygame.init()
    clock = pygame.time.Clock()

    width = 800 
    height = 600
    size = width, height
    
    bgColor = r,g,b = 200, 0, 0

    screen = pygame.display.set_mode(size)

    backgrounds = pygame.sprite.Group()
    all = pygame.sprite.OrderedUpdates()

    TextWindow.containers = (all, backgrounds)
    BackGround.containers = (all, backgrounds)

    BackGround("images/Screens/europeMap1.png")

    TextWindow("RS/Story.txt", "RS/TextGB.png", [width/2,100])
    


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
        
        all.update(width, height)
        
        dirty = all.draw(screen)
        pygame.display.update(dirty)
        pygame.display.flip()
        clock.tick(60)

    
