import pygame

# Ball class
class Ball:
	def __init__(self, posx, posy, radius, speed, color, screen):
		self.screen = screen
		self.screen_width = self.screen.get_size()[0]
		self.screen_height = self.screen.get_size()[1]
		self.posx = posx
		self.posy = posy
		self.radius = radius
		self.speed = speed
		self.color = color
		self.xFac = 1
		self.yFac = -1
		self.ball = pygame.draw.circle(
			self.screen, self.color, (self.posx, self.posy), self.radius)
		self.firstTime = 1

	def display(self):
		self.ball = pygame.draw.circle(
			self.screen, self.color, (self.posx, self.posy), self.radius)

	def update(self):
		self.posx += self.speed*self.xFac
		self.posy += self.speed*self.yFac

		# If the ball hits the top or bottom surfaces, 
		# then the sign of yFac is changed and 
		# it results in a reflection
		if self.posy <= 0 or self.posy >= self.screen_height:
			self.yFac *= -1

		if self.posx <= 0 and self.firstTime:
			self.firstTime = 0
			return 1
		elif self.posx >= self.screen_width and self.firstTime:
			self.firstTime = 0
			return -1
		else:
			return 0

	def reset(self):
		self.posx = self.screen_width//2
		self.posy = self.screen_height//2
		self.xFac *= -1
		self.firstTime = 1

	# Used to reflect the ball along the X-axis
	def hit(self):
		self.xFac *= -1
  
	def teleport(self, new_coords):
		self.posx = new_coords[0]
		self.posy = new_coords[1]
		
	def getRect(self):
		return self.ball