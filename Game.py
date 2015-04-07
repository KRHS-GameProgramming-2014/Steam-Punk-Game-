import pygame, sys, random
from Button import Button
from BackGround import BackGround
from Block import Block

pygame.init()

clock = pygame.time.Clock()

width = 800 
height = 600
size = width, height


bgColor = r,g,b = 0, 0, 10

screen = pygame.display.set_mode(size)

bgImage = pygame.image.load("images/Screens/Start Screen.png").convert()
bgRect = bgImage.get_rect()

backgrounds = pygame.sprite.Group()
blocks = pygame.sprite.Group()
all = pygame.sprite.OrderedUpdates()

BackGround.containers = (all, backgrounds)
Block.containers = (all, blocks)

run = False

startButton = Button([width/2, height-300], 
				     "images/Buttons/Start Base.png", 
				     "images/Buttons/Start Clicked.png")

while True:
	while not run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT: sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN:
					run = True
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
		
	BackGround("images/Screens/Main Screen.png")
	
	player = PlayerBall([width/2, height/2])
	
	


	score = Score([width-80, height-25], "Score: ", 36)
	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT: sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_w or event.key == pygame.K_UP:
					player.go("up")
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_w or event.key == pygame.K_UP:
					player.go("stop up")


		all.update(width, height)
		
		dirty = all.draw(screen)
		pygame.display.update(dirty)
		pygame.display.flip()
		clock.tick(60)
		
