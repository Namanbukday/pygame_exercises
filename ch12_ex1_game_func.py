import sys

import pygame

def check_events(ship):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				ship.moving_up_flag = True
			if event.key == pygame.K_DOWN:
				ship.moving_down_flag = True

		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_UP:
				ship.moving_up_flag = False
			if event.key == pygame.K_DOWN:
				ship.moving_down_flag = False

def update_screen(ag_setting, screen, ship):
	screen.fill(ag_setting.bg_color)
	ship.blitme()
	pygame.display.flip()