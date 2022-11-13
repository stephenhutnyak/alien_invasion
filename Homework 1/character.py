import pygame
from settings import Settings

class Character():

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load image and get its rect
        self.image = pygame.image.load("images/rocket.png")
        self.image = pygame.transform.scale(self.image, (50, 75))
        self.rect = self.image.get_rect()

        # Start each image in the middle of the screen
        self.rect.center = self.screen_rect.center

        # Store current location
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Movement flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.character_speed
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.x -= self.settings.character_speed
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.y -= self.settings.character_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.character_speed

        # Update rect object
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """Draw image to screen"""
        self.screen.blit(self.image, self.rect)