import pygame
from random import randint
import os
os.chdir(os.path.dirname(__file__))
pygame.init()
speed = 10
disp_x = 600
disp_y = 600
skyBlue = (0,255,255)
yellow = (255, 242, 0)
black = (0,0,0)
white = (255,255,255)
green = (0,200,50)
red = (200,0,0)
brightRed = (255,0,0)
brightGreen = (0,255,0)
gameDisp = pygame.display.set_mode((disp_x,disp_y))
pygame.display.set_caption("Hungry Snake")
clock = pygame.time.Clock()
def detectCollisions(x1,y1,w1,h1,x2,y2,w2,h2):
    if (x2+w2>=x1>=x2 and y2+h2>=y1>=y2):
        return True
    elif (x2+w2>=x1+w1>=x2 and y2+h2>=y1>=y2):
        return True
    elif (x2+w2>=x1>=x2 and y2+h2>=y1+h1>=y2):
        return True
    elif (x2+w2>=x1+w1>=x2 and y2+h2>=y1+h1>=y2):
        return True
    else:
        return False
def text_object(text, font):
	textSurface = font.render(text, True , black)
	return textSurface,textSurface.get_rect()
def pointTxt(amount):
	txtSize = pygame.font.SysFont('Comic Sans MS',22)
	textSurf,textRect = text_object(("point:" + amount),txtSize)
	textRect = (10,0)
	gameDisp.blit(textSurf,textRect)
def debugTxt(amount):
	txtSize = pygame.font.SysFont('Comic Sans MS',22)
	textSurf,textRect = text_object((amount),txtSize)
	textRect = (0,22)
	gameDisp.blit(textSurf,textRect)
def menuTxt():
	txtSize = pygame.font.SysFont('Comic Sans MS',50)
	textSurf,textRect = text_object("Hungry Snake",txtSize)
	textRect.center = ((disp_x/2),(disp_y/2.5))
	gameDisp.blit(textSurf,textRect)
def redBtnTxt():
	txtSize = pygame.font.SysFont('Comic Sans MS',30)
	textSurf,textRect = text_object("Quit",txtSize)
	textRect = (420,305)
	gameDisp.blit(textSurf,textRect)
def greenBtnTxt():
	txtSize = pygame.font.SysFont('Comic Sans MS',25)
	textSurf,textRect = text_object("Start",txtSize)
	textRect = (115,305)
	gameDisp.blit(textSurf,textRect)
def dot(x,y):
	pygame.draw.rect(gameDisp, white,(x,y,36,36))
def food(x,y):
	pygame.draw.rect(gameDisp, yellow,(x,y,36,36))
def gameIntro(state):
	stage = state
	intro = True
	if stage == 1:
		pygameImg = pygame.image.load("pygame.png")
		logoimage = gameDisp.blit(pygameImg,(50,50))
		pygame.display.update()
		pygame.time.delay(2000)
		stage = 2
	if stage == 2:
		while intro:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					quit()
				if event.type == pygame.MOUSEBUTTONDOWN:
					if greenBtn:
						gameLoop()
						intro = False
					if redBtn:
						quit()
			gameDisp.fill(white)
			menuTxt()
			mouse_x, mouse_y = pygame.mouse.get_pos()
			pygame.draw.rect(gameDisp, green,(100,300,100,50))
			if detectCollisions(mouse_x,mouse_y,10,10,100,300,100,50):
				pygame.draw.rect(gameDisp, brightGreen,(100,300,100,50))
				greenBtn = True
			else:
				greenBtn = False
			pygame.draw.rect(gameDisp, red,(400,300,100,50))
			if detectCollisions(mouse_x,mouse_y,10,10,400,300,100,50):
				pygame.draw.rect(gameDisp, brightRed,(400,300,100,50))
				redBtn = True
			else:
				redBtn = False
			redBtnTxt()
			greenBtnTxt()
			pygame.display.update()
def gameLoop():
	tail = []
	point = 0
	x = (disp_x * 0.5)
	y = (disp_y * 0.5)
	xChange = 0
	yChange = 0
	dirs = 0
	""" 1 = up
	2 = down
	3 = right
	4 = left """
	crashed = False
	foody = randint(0,(disp_y - 36))
	foodx = randint(0,(disp_x - 36))
	while not crashed:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				crashed = True
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT and dirs != 3:
					yChange = 0
					xChange = -36
					dirs = 4
				elif event.key == pygame.K_RIGHT and dirs != 4:
					yChange = 0
					xChange = 36
					dirs = 3
				elif event.key == pygame.K_UP and dirs != 2:
					xChange = 0
					yChange = -36
					dirs = 1
				elif event.key == pygame.K_DOWN and dirs != 1:
					xChange = 0
					yChange = 36
					dirs = 2
		tail = [(x, y)] + tail
		x += xChange
		y += yChange
		if detectCollisions(x,y,36,36,foodx,foody,36,36):
			foodx = randint(0,(disp_x - 36))
			foody = randint(0,(disp_y - 36))
			point += 1
		gameDisp.fill(skyBlue)
		pointTxt(str(point))
		dot(x,y)
		for	i in range(point):
			dot(tail[i][0],tail[i][1])
			if dirs == 1:
				if detectCollisions(x+1,y,34,1,tail[i][0],tail[i][1],36,36):
					gameIntro(2)
			elif dirs == 2:
				if detectCollisions(x+1,y+36,34,1,tail[i][0],tail[i][1],36,36):
					gameIntro(2)
			elif dirs == 3:
				if detectCollisions(x+36,y+1,1,34,tail[i][0],tail[i][1],36,36):
					gameIntro(2)
			elif dirs == 4:
				if detectCollisions(x,y+1,1,34,tail[i][0],tail[i][1],36,36):
					gameIntro(2)
		if x < 0 or x > disp_x-36:
			gameIntro(2)
		if y < 0 or y > disp_y-36:
			gameIntro(2)
		food(foodx,foody)
		pygame.display.update()
		clock.tick(speed)
gameIntro(1)
gameLoop()

pygame.quit()
quit()