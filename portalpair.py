import pygame
from random import randint

class PortalPair():
	def __init__(self, screen, height, width, color):
		self.loc1 = [300, 180]
		self.loc2 = [550, 420]
		self.loc_list = [self.loc1, self.loc2]
		self.height = height
		self.width = width
		self.color = color
		self.screen = screen
		self.screen_width = self.screen.get_size()[0]
		self.screen_height = self.screen.get_size()[1]
		self.initialize()

	def initialize(self):
		# Define rectangles
		self.portal1_rect = pygame.Rect(self.loc1[0], self.loc1[1], self.width, self.height)
		self.portal2_rect = pygame.Rect(self.loc2[0], self.loc2[1], self.width, self.height)
		# Draw portals
		self.portal1 = pygame.draw.rect(self.screen, self.color, self.portal1_rect)
		self.portal2 = pygame.draw.rect(self.screen, self.color, self.portal2_rect)
		# Save portals to a list for easier collision checking
		self.portal_list = [self.portal1, self.portal2]
  
	def draw(self):
		# Define rectangles
		self.portal1_rect = pygame.Rect(self.loc1[0], self.loc1[1], self.width, self.height)
		self.portal2_rect = pygame.Rect(self.loc2[0], self.loc2[1], self.width, self.height)
		# Draw portals again
		self.portal1 = pygame.draw.rect(self.screen, self.color, self.portal1_rect)
		self.portal2 = pygame.draw.rect(self.screen, self.color, self.portal2_rect)
	
	def update(self):
     
		### UNCOMMENT ONCE generate_location() HAS BEEN WRITTEN ###
		# self.loc1 = self.generate_location()
		# self.loc2 = self.generate_location()
  
		# Define rectangles
		self.portal1_rect = pygame.Rect(self.loc1[0], self.loc1[1], self.width, self.height)
		self.portal2_rect = pygame.Rect(self.loc2[0], self.loc2[1], self.width, self.height)
		# Draw portals again
		self.portal1 = pygame.draw.rect(self.screen, self.color, self.portal1_rect)
		self.portal2 = pygame.draw.rect(self.screen, self.color, self.portal2_rect)
  
		# Save portals to a list for easier collision checking
		self.portal_list = [self.portal1, self.portal2]


	### NEED TO GENERATE RANDOM X & Y coordinates within screen and return them as a list ###
	def generate_location(self):
		pass