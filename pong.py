import pygame
from portalpair import PortalPair
from paddle import Striker
from ball import Ball

pygame.init()

# RGB values of standard colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
PINK = (255, 20, 147)

# Basic parameters of the screen
WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Portal Pong")
print(screen.get_size())

clock = pygame.time.Clock() 
FPS = 30	

def main():
	running = True

	# Defining the objects
	player1 = Striker(posx=20, posy=0, width=10, height=100, speed=10, color=WHITE, screen=screen)
	player2 = Striker(posx=WIDTH-30, posy=0, width=10, height=100, speed=10, color=GREEN, screen=screen)
	ball = Ball(posx=WIDTH//2, posy=HEIGHT//2, radius=7, speed=14, color=WHITE, screen=screen)
	portals = PortalPair(screen=screen, height=50, width=10, color=PINK)

	listOfplayers = [player1, player2]
	list_of_portal_pairs = [portals]

	# Initial parameters of the players
	player1Score, player2Score = 0, 0
	player1YFac, player2YFac = 0, 0
 
	PORTALS_MOVE = pygame.USEREVENT + 1
	pygame.time.set_timer(PORTALS_MOVE, 5000) 

	while running:
		screen.fill(BLACK)

		# Event handling
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					player2YFac = -1
				if event.key == pygame.K_DOWN:
					player2YFac = 1
				if event.key == pygame.K_w:
					player1YFac = -1
				if event.key == pygame.K_s:
					player1YFac = 1
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
					player2YFac = 0
				if event.key == pygame.K_w or event.key == pygame.K_s:
					player1YFac = 0
			if event.type == PORTALS_MOVE:
				for portal_pair in list_of_portal_pairs:
					portal_pair.update()
				

		# Collision detection
		for player in listOfplayers:
			if pygame.Rect.colliderect(ball.getRect(), player.getRect()):
				ball.hit()
		for portal_pair in list_of_portal_pairs:
			for index, portal in enumerate(portal_pair.portal_list):
				if pygame.Rect.colliderect(ball.getRect(), portal):
					if index == 0:
						ball.teleport(portals.loc2)
					if index == 1:
						ball.teleport(portals.loc1)

		# Updating the objects
		player1.update(player1YFac)
		player2.update(player2YFac)
		point = ball.update()
		portals.draw()

		# -1 -> player_1 has scored
		# +1 -> player_2 has scored
		# 0 -> None of them scored
		if point == -1:
			player1Score += 1
		elif point == 1:
			player2Score += 1

		# Someone has scored
		# a point and the ball is out of bounds.
		# So, we reset it's position
		if point: 
			ball.reset()

		# Displaying the objects on the screen
		player1.display()
		player2.display()
		ball.display()

		# Displaying the scores of the players
		player1.displayScore("player_1 : ", 
						player1Score, 100, 20, WHITE)
		player2.displayScore("player_2 : ", 
						player2Score, WIDTH-100, 20, WHITE)

		pygame.display.update()
		clock.tick(FPS)	


if __name__ == "__main__":
	main()
	pygame.quit()
