import sys
import pygame

from ch12_ex1_setting import Settings
from ch12_ex1b import Ship

import ch12_ex1_game_func as gf

def run_game():
	pygame.init()

	ag_setting = Settings()

	screen = pygame.display.set_mode((ag_setting.screen_height, ag_setting.screen_width))
	pygame.display.set_caption("another game")

	
	ship = Ship(ag_setting, screen)

	while True:
		gf.check_events(ship)
		ship.update()
		gf.update_screen(ag_setting, screen, ship)


run_game()