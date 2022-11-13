import pygame

class Mario():

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load image and get its rect
        self.image = pygame.image.load("images/mario.png")
        self.image = pygame.transform.scale(self.image, (50, 75))
        self.rect = self.image.get_rect()

        # Start each image in the middle of the screen
        self.rect.center = self.screen_rect.center

    def blitme(self):
        """Draw image to screen"""
        self.screen.blit(self.image, self.rect)