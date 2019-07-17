import pygame

class Ship():

	def __init__(self, ag_setting, screen):

		self.screen = screen
		
		self.ag_setting = ag_setting

		self.image = pygame.image.load('C:/Users/nbukd/Desktop/PROJECTS/my_game_exercises/image/ship.bmp')

		self.rect = self.image.get_rect()

		self.screen_rect = screen.get_rect()

		self.rect.centery = self.screen_rect.centery
		self.rect.left = self.screen_rect.left	

		self.centery = float(self.rect.centery)

		self.moving_up_flag = False
		self.moving_down_flag = False

	def update(self):
		if self.moving_up_flag and self.rect.top > self.screen_rect.top:
			self.centery -= ag_setting.ship_speed_factor
		if self.moving_down_flag and self.rect.bottom < self.screen_rect.bottom:
			self.centery += ag_setting.ship_speed_factor
	
		self.rect.centery = self.centery

	def blitme(self):
		self.screen.blit(self.image, self.rect)