import sys
import pygame
from star import Star
from settings import Settings
from random import randint


class Stars:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game and create game resources"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((1200, 600))
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Rain")

        self.stars = pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._update_stars()
            self._update_screen()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

    def _create_fleet(self):
        """Create the fleet of stars"""
        # Create a star and find the number of stars in a row
        # Spacing between each star is equal to one star width
        star = Star(self)
        star_width, star_height = star.rect.size
        available_space_x = self.settings.screen_width - (2* star_width)
        number_stars_x = available_space_x // (2 * star_width)

        # Determine the number of rows of stars that fir on the screen
        available_space_y = (self.settings.screen_height -
                             star_height - 50)
        number_rows = available_space_y // (2 * star_height)

        # Create the full fleet of stars
        for row_number in range(number_rows):
            for star_number in range(number_stars_x):
                self._create_star(star_number, row_number)

    def _create_star(self, star_number, row_number):
        # Create an star and place it in the row
        star = Star(self)
        star_width, star_height = star.rect.size
        star.x = star_width + 2 * star_width * star_number
        star.rect.x = star.x
        star.rect.y = star.rect.height + 2 * star.rect.height * row_number
        self.stars.add(star)

    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction"""
        for star in self.stars.sprites():
            star.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    # Watch for keyboard and mouse events
    def _check_events(self):
        """Respond to keypresses and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_stars(self):
        """Check if the fleet is at an edge,
        then update the positions of all aliens in the fleet"""
        self.stars.update()

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen"""
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)
        self.stars.draw(self.screen)

        # Make the most recently drawn screen visible.
        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance and run the game
    ai = Stars()
    ai.run_game()