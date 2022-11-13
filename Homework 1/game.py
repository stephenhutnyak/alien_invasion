import sys
import pygame
from settings import Settings
from character import Character

class GameTime:

    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Game Time")

        self.character = Character(self)

    def run_game(self):

        while True:
            self._check_events()
            self.character.update()
            self._update_screen()

    def _check_events(self):
        """Respond to keypresses and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.character.moving_right = True
                if event.key == pygame.K_LEFT:
                    self.character.moving_left = True
                if event.key == pygame.K_UP:
                    self.character.moving_up = True
                if event.key == pygame.K_DOWN:
                    self.character.moving_down = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.character.moving_right = False
                if event.key == pygame.K_LEFT:
                    self.character.moving_left = False
                if event.key == pygame.K_UP:
                    self.character.moving_up = False
                if event.key == pygame.K_DOWN:
                    self.character.moving_down = False

    def _update_screen(self):
        """Update images on the screen"""
        self.screen.fill(self.settings.bg_color)
        self.character.blitme()

        pygame.display.flip()

if __name__ == '__main__':
    ai = GameTime()
    ai.run_game()
