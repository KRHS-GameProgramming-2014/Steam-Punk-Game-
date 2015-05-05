import pygame, sys, random
import pygame, sys, random
from Button import Button
from BackGround import BackGround
from Block import Block
from Player import Player
from Mouse import Pointer
from Level import Level

pygame.init()

clock = pygame.time.Clock()

width = 800 
height = 600
screenSize = width, height

screen = pygame.display.set_mode(screenSize)
fullscreen = False

bgImage = pygame.image.load("RS/Main Menu/Startscreen.png").convert()
bgRect = bgImage.get_rect()

backgrounds = pygame.sprite.Group()
blocks = pygame.sprite.Group()
players = pygame.sprite.Group()
pointers = pygame.sprite.Group()
all = pygame.sprite.OrderedUpdates()

BackGround.containers = (all, backgrounds)
Block.containers = (all, blocks)
Player.containers = (all, players)
Pointer.containers = (all, pointers)

bgColor = r,g,b = 0, 0, 10


            
run = False

startButton = Button([width/2, height-200], 
                     "RS/Main Menu/Start Base.png", 
                     "RS/Main Menu/Start Clicked.png")

while True:
    while not run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    run = True
                if event.key == pygame.K_RETURN:
                    print event.mod, pygame.KMOD_RALT
                    if event.mod & pygame.KMOD_RALT: #Binary and with KMOD_RIGHT to filter out other mod keys
                        if fullscreen:
                            pygame.display.set_mode(size)
                            fullscreen = False
                        else:
                            pygame.display.set_mode(size, pygame.FULLSCREEN)
                            fullscreen = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                startButton.click(event.pos)
            if event.type == pygame.MOUSEBUTTONUP:
                if startButton.release(event.pos):
                    run = True
            
                    
        bgColor = r,g,b
        screen.fill(bgColor)
        screen.blit(bgImage, bgRect)
        screen.blit(startButton.image, startButton.rect)
        pygame.display.flip()
        clock.tick(60)
    
    BackGround("images/background.png")
    
    level = Level("screen1", ["Dan", "Sean"], screenSize)
    level.killOldLevels(0)
    player = Player([width/2, height/2])
    
    Pointer("RS/pointer.png")
    pygame.mouse.set_visible(False)


    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    player.go("up")
                if event.key == pygame.K_RETURN:
                        print event.mod, pygame.KMOD_RALT
                        if event.mod & pygame.KMOD_RALT: #Binary and with KMOD_RIGHT to filter out other mod keys
                            if fullscreen:
                                pygame.display.set_mode(screenSize)
                                fullscreen = False
                            else:
                                pygame.display.set_mode(screenSize, pygame.FULLSCREEN)
                                fullscreen = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    player.go("stop up")
                
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    pointersHitBlocks = pygame.sprite.groupcollide(pointers, blocks, False, False)
                    
                    for pointer in pointersHitBlocks:
                        for block in pointersHitBlocks[pointer]:
                            player.rect.center = block.rect.center

        all.update(width, height)
        
        dirty = all.draw(screen)
        pygame.display.update(dirty)
        pygame.display.flip()
        clock.tick(60)
            
