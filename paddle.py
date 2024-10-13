import pygame


class Striker:
		# Take the initial position, dimensions, speed and color of the object
	def __init__(self, posx, posy, width, height, speed, color, screen):
		self.font = pygame.font.Font('freesansbold.ttf', 20)
		self.screen = screen
		self.screen_width = self.screen.get_size()[0]
		self.screen_height = self.screen.get_size()[1]
		self.posx = posx
		self.posy = posy
		self.width = width
		self.height = height
		self.speed = speed
		self.color = color
		# Rect that is used to control the position and collision of the object
		self.geekRect = pygame.Rect(posx, posy, width, height)
		# Object that is blit on the screen
		self.geek = pygame.draw.rect(self.screen, self.color, self.geekRect)

	# Used to display the object on the self.screen
	def display(self):
		self.geek = pygame.draw.rect(self.screen, self.color, self.geekRect)

	def update(self, yFac):
		self.posy = self.posy + self.speed*yFac

		# Restricting the striker to be below the top surface of the self.screen
		if self.posy <= 0:
			self.posy = 0
		# Restricting the striker to be above the bottom surface of the self.screen
		elif self.posy + self.height >= self.screen_height:
			self.posy = self.screen_height-self.height

		# Updating the rect with the new values
		self.geekRect = (self.posx, self.posy, self.width, self.height)

	def displayScore(self, text, score, x, y, color):
		text = self.font.render(text+str(score), True, color)
		textRect = text.get_rect()
		textRect.center = (x, y)

		self.screen.blit(text, textRect)

	def getRect(self):
		return self.geekRect